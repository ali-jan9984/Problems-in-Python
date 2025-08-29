def equilateral(sides):
    a,b,c = sides
    if a > 0 and b > 0 and c > 0:
        if a + b >= c and b + c >= a and a + c >= b:
            #Now to check what type of triangle
            return a==b==c
    return False
print(equilateral([4,4,4]))


def isosceles(sides):
    a,b,c = sides
    if a > 0 and b > 0 and c > 0:
        if a + b >= c and b + c >= a and a + c >= b:
            return (a==b) or (b==c) or (c==a)
    return False
print(isosceles([4,4,3]))
    


def scalene(sides):
    a,b,c = sides
    if a > 0 and b > 0 and c > 0:
        if a + b >= c and b + c >= a and a + c >= b:
            return (a != b) and (b != c) and (c != a)
    return False
print(scalene([3,5,7]))
