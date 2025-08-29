def sum_of_multiples(limit, numbers):
    return sum(
        {
            m for n in numbers if n for m in range(n,limit,n) 
        }
    )
                