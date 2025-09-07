def proverb(*input_data, qualifier=None):
    if not input_data:
        return []

    if qualifier:
        final_line = [f"And all for the want of a {qualifier} {input_data[0]}."]
    else:
        final_line = [f"And all for the want of a {input_data[0]}."]
    
    result = [f"For want of a {w} the {l} was lost." for w, l in zip(input_data, input_data[1:])]
    return result + final_line