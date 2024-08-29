import math

def polysum(n, s):
    area = (0.25*n*s*s)/math.tan(math.pi/n)
    perimeter = n*s
    return area + perimeter

if __name__ == "__main__":
    n = int(input("Please input value for n:    "))
    s = int(input("Please input value for s:    "))
    print(polysum(n,s))