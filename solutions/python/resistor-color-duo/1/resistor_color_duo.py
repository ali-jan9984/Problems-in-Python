COLORS = {"black":'0',"brown":'1',"red":'2',"orange":'3',"yellow":'4',"green":'5',"blue":'6',"violet":'7',"grey":'8',"white":'9'}

def value(colors):
    code = ''
    if len(colors) > 2:
       colors = colors[:2] 
    for color in colors:
        code += COLORS[color]
    return int(code)   
