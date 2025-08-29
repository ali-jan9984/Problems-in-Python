def square_root(number):
    x = number / 2 
    for _ in range(20):
        x_new = (x + number // x) // 2
        if x_new * x_new == number:
            return x_new
        x = x_new
    raise ValueError("not found")

