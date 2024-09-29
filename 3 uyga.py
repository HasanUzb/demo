import random
a = random.sample(range(100, 1001), 100)
N = random.choice(a)
juftlar = [num for num in range(N + 1) if num % 2 == 0]
print(f"Random son: {a}")
print(f"N: {N}, Juft sonlar: {juftlar}")