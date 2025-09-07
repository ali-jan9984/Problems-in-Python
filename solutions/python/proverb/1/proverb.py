def proverb(*input_data, qualifier=None):
    if not input_data:
        return []

    if qualifier:
        final_line = f"And all for the want of a {qualifier} {input_data[0]}."
    else:
        final_line = f"And all for the want of a {input_data[0]}."

    result = []
    for A, B in zip(input_data, input_data[1:]):
        result.append(f"For want of a {A} the {B} was lost.")
    result.append(final_line)
    return result