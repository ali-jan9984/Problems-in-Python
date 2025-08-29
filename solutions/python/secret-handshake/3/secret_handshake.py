def commands(binary_str):
    t = ''
    if len(binary_str) > 5:
        t = binary_str[-5:]
    else:
        t = binary_str.zfill(5)
    shakes = 'jump','close your eyes','double blink','wink'
    actions = [shake for b,shake in zip(binary_str[1:],shakes) if b == '1']
    if t[0] == '0':
        actions = list(reversed(actions))
    return actions
        