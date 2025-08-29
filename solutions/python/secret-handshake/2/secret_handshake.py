def commands(binary_str):
    t = ''
    if len(binary_str) > 5:
        t = binary_str[-5:]
    else:
        t = binary_str.zfill(5)
    actions = []
    if t[4] == '1':
        actions.append('wink')
    if t[3] == '1':
        actions.append('double blink')
    if t[2] == '1':
        actions.append('close your eyes')
    if t[1] == '1':
        actions.append('jump')
    if t[0] == '1':
        actions = list(reversed(actions))
    return actions
        