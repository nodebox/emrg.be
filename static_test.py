import unittest

import static

class UtilTest(unittest.TestCase):

    def test_merge_dicts(self):
        a = {'a': {'aa': 11, 'ab': 12}, 'b': 2}
        b = {'a': {'aa': 666, 'ac': 999}, 'c': 333}
        m = static._merge_dicts(a, b)
        self.assertEqual(m, {'a': {'aa': 666, 'ab': 12, 'ac': 999}, 'b': 2, 'c': 333})

class TemplateTest(unittest.TestCase):

    def test_vars(self):
        s = '{{ a }} + {{ b }} = {{ c }}'
        t = static.parse_template(s)
        r1 = static.eval_template(t, {})
        self.assertEqual(r1, ' +  = ')
        r2 = static.eval_template(t, {'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(r2, '1 + 2 = 3')

    def test_nested_vars(self):
        s = '<title>{{ page.title }}</title>'
        t = static.parse_template(s)
        r1 = static.eval_template(t, {})
        self.assertEqual(r1, '<title></title>')
        r2 = static.eval_template(t, {'page': {'title': 'Foo'}})
        self.assertEqual(r2, '<title>Foo</title>')


if __name__ == '__main__':
    unittest.main()
