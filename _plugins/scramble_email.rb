require 'liquid'

module ScrambleTextFilter
  
  def scramble_chars(text)
    enc = [] 
    enc << rand(255)
    
    text.split("").each do |c|
      enc << c.unpack('c')[0] - enc.last
    end
    enc
  end

  # Scramble the text so it is unreadable to spammers.
  def scramble_text(text)
    chars = scramble_chars(text)
    "<script>var t=[#{chars.join(',')}]; for (var i=1; i<t.length; i++) { document.write(String.fromCharCode(t[i]+t[i-1])); }</script>"
  end

end

Liquid::Template.register_filter(ScrambleTextFilter)