x = float(input("x:	"))
def y():
    y = m * x + b
    if x < 0:
        print(f" {x} | {y}")
    else:
        print(f" {x} | {y}")
print("-----------")
m = float(input("What is m: "))
b = float(input("What is b: "))
print("  x  |  y")
print("-----|-----")
x -= 5
for _ in range(10):
    y()
    x +=1
