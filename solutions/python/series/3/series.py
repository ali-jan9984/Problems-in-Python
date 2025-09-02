def slices(series: str, length: int) -> list[str]:
    """Extract all contiguous substrings of specified length from series."""
    _validate_inputs(series, length)
    return [series[i : i + length] for i in range(len(series) - length + 1)]


def _validate_inputs(series: str, length: int) -> None:
    """Validate the inputs; series and length."""
    if not series:
        raise ValueError("series cannot be empty")
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")