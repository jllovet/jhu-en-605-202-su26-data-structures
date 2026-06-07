def gcd(x, y):
    if y <= x and x % y == 0:
        return y
    if x < y:
        return gcd(y,x)
    else:
        return gcd(y, x%y)


print(f"gcd(1,1): {gcd(1,1)}")
print(f"gcd(2,1): {gcd(2,1)}")
print(f"gcd(5,2): {gcd(5,2)}")
print(f"gcd(10,2): {gcd(10,2)}")
print(f"gcd(10,5): {gcd(10,5)}")
print(f"gcd(26,13): {gcd(26,13)}")
print(f"gcd(147,23): {gcd(147,23)}")
print(f"gcd(952,12): {gcd(952,12)}")