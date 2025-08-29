import re
RE = re.compile(r'[a-z0-9]')


def encode(plain_text):
    text = RE.findall(plain_text.lower())
    encode_list = []
    for ch in text:
        if 'a'<= ch <= 'z':
            encode_list.append(chr(ord('a') + (ord('z') - ord(ch))))
        else:
            encode_list.append(ch)
    result_list = []
    if len(encode_list) >= 5:
        for i in range(0,len(encode_list),5):
            result_list.append(''.join(encode_list[i:i+5]))
        return ' '.join(result_list)
    return ''.join(encode_list)                      
    
        
def decode(ciphered_text):
    text = RE.findall(ciphered_text.lower())
    decode_list = []
    for ch in text:
        if 'a'<= ch <= 'z':
            decode_list.append(chr(ord('z') + (ord('a') - ord(ch))))
        else:
            decode_list.append(ch)
    return ''.join(decode_list)