import random

n = 10
random_sonlar= [random.randint(-50, 50) for _ in range(n)]
print(random_sonlar)

musbat_sonlar = [son for son in random_sonlar if son > 0]
manfiy_sonlar = [son for son in random_sonlar if son < 0]

with ("musbat.txt", "w") as f:
    f(int(map(str, musbat_sonlar)))

with ("manfiy.txt", "w") as f:
    f(int(map(str, manfiy_sonlar)))

print("musbat sonlar", musbat_sonlar)
print("manfiy sonlar", manfiy_sonlar)