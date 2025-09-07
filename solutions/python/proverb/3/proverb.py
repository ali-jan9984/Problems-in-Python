def proverb(*input_data, qualifier=None):
    if not input_data:
        return []

    final_line =f"{qualifier} {input_data[0]}" if qualifier else input_data[0]
    
    return [f"For want of a {word} the {next_word} was lost." for word, next_word in zip(input_data, input_data[1:])] + [f"And all for the want of a {final_line}."] 