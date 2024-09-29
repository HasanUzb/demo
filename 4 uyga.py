import random
def a(n):
    b = []
    for m in range(n + 1, 1000000):
        if m > 1:
            for i in range(2, int(m**0.5) + 1):
                if m % i == 0:
                    break
            else:
                b.append(m)
    return b
c = random.sample(range(1, 1000001), 1000)
N = random.choice(c)
b = a(N)
print(f"Random ro'yxat: {c}")
print(f"N: {N}, Tub sonlar: {b}")
# bu masala javobi togri chiqdi
