import os
import os.path
import re
import shutil

BUILD_DIR = '_site'

BLOCK_TAG_START = '{%'
BLOCK_TAG_END = '%}'
VARIABLE_TAG_START = '{{'
VARIABLE_TAG_END = '}}'

tag_re = re.compile('(%s.*?%s|%s.*?%s)' %
        (re.escape(BLOCK_TAG_START), re.escape(BLOCK_TAG_END),
         re.escape(VARIABLE_TAG_START), re.escape(VARIABLE_TAG_END)))

def _merge_dicts(a, b, path=None):
    """Merge the items of the two dictionaries.
    Items in b will override items in a with the same key."""
    if path is None: path = []
    a = dict(a)
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                a[key] = _merge_dicts(a[key], b[key], path + [str(key)])
            else:
                a[key] = b[key]
        else:
            a[key] = b[key]
    return a

def parse_metadata(s):
    """Given the metadata as a string, parse out key/value pairs."""
    meta = {}
    for line in s.split('\n'):
        k, v = line.split(':')
        meta[k.strip()] = v.strip()
    return meta

def extract_metadata(s):
    """Split the page into metadata and HTML.
    The returned metadata is a dictionary with the key/value pairs.
    The HTML is just a string.
    The metadata is specified using ---."""
    # Split the page in lines.
    lines = s.split('\n')
    if lines[0] == '---':
        end = lines.index('---', 1)
        if end <= 1:
            raise 'Page metadata is not specified correctly.'
        meta = '\n'.join(lines[1:end])
        meta = {'page': parse_metadata(meta)}
        page = '\n'.join(lines[end+1:])
        return meta, page
    else:
        return {'page': {}}, s

def parse_template(html):
    """Parse out the template tags."""
    tokens = []
    for chunk in tag_re.split(html):
        if chunk.startswith(BLOCK_TAG_START):
            tokens.append({'type': 'block', 'body': chunk[2:-2].strip()})
        elif chunk.startswith(VARIABLE_TAG_START):
            tokens.append({'type': 'var', 'body': chunk[2:-2].strip()})
        else:
            tokens.append({'type': 'text', 'body': chunk})
    return tokens

def lookup_var(ctx, var):
    """Look up the variable in the given context."""
    scope = ctx
    for v in var.split('.'):
        scope = scope.get(v)
        if scope is None:
            return ''
    return scope

def eval_template(template, ctx):
    """Evaluate the template using the given context."""
    s = ''
    for token in template:
        if token['type'] == 'text':
            s += token['body']
        elif token['type'] == 'var':
            v = lookup_var(ctx, token['body'])
            s += '%s' % v
        elif token['type'] == 'block':
            s += '==ERR BLOCK=='
        else:
            raise 'Unknown token %s' % token
    return s

def parse_page(fname, ctx=None):
    s = open(fname).read()
    meta, html = extract_metadata(s)
    template = parse_template(html)
    if ctx is not None:
        merged_meta = _merge_dicts(ctx, meta)
    else:
        merged_meta = meta
    html = eval_template(template, merged_meta)
    layout = meta['page'].get('layout')
    if layout is not None:
        ctx = _merge_dicts(merged_meta, {'content': html})
        return parse_page('_layouts/%s.html' % layout, ctx)
    else:
        return merged_meta, html

def _ensure_directory(d):
    try:
        os.makedirs(d)
    except OSError, e:
        if e.errno == 17:
            pass
        else:
            raise e

def process_file(source_file, target_file):
    """Copy the file from the source to the target, processing it."""
    ext = os.path.splitext(source_file)[1]
    if ext == '.md':
        try:
            meta, html = parse_page(source_file)
        except Exception, e:
            print 'ERROR while parsing page %s' % source_file
            raise e
        target_base = os.path.splitext(target_file)[0]
        target_file = '%s.html' % target_base
        with open(target_file, 'w') as f:
            f.write(html)
    else:
        shutil.copy(source_file, target_file)

def build(path='.'):
    for f in os.listdir(path):
        file_path = os.path.join(path, f)
        if os.path.isfile(file_path):
            target_dir = os.path.join(BUILD_DIR, path)
            _ensure_directory(target_dir)
            target_file = os.path.join(target_dir, f)
            process_file(file_path, target_file)
        elif os.path.isdir(file_path):
            if f.startswith('.git'): continue
            if f.startswith('_'): continue
            build(os.path.join(path, f))
        else:
            print 'Unsupported file type', file_path

if __name__=='__main__':
    build()
