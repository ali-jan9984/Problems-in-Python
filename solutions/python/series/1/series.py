def slices(series: str, length: int) -> list[str]:
    validate_inputs(series, length)
    return [series[i : i + length] for i in range(len(series) - length + 1)]


def validate_inputs(s: str, n: int) -> None:
    if n == 0:
        raise ValueError("slice length cannot be zero")
    if n < 0:
        raise ValueError("slice length cannot be negative")
    if not s:
        raise ValueError("series cannot be empty")
    if n > len(s):
        raise ValueError("slice length cannot be greater than series length")
    return None