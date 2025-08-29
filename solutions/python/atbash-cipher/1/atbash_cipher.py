def encode(plain_text):
    text = ''.join(ch for ch in plain_text if ch.isnumeric() or ch.isalpha()).lower()
    result = ''
    for ch in text:
        if 'a'<= ch <= 'z':
            reversed_char_code = ord('a') + (ord('z') - ord(ch))
            result += chr(reversed_char_code)
        else:
            result += ch
    result_list = []
    if len(result) > 5:
        for i in range(0,len(result),5):
            result_list.append(result[i:i+5])
        return ' '.join(result_list)
    return result                       
    
        
def decode(ciphered_text):
    text = ''.join(ch for ch in ciphered_text if ch.isnumeric() or ch.isalpha()).lower()
    result = ''
    for ch in text:
        if 'a'<= ch <= 'z':
            reversed_char_code = ord('a') + (ord('z') - ord(ch))
            result += chr(reversed_char_code)
        else:
            result += ch
    return result
