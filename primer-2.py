sekundy = int(input())
sek = sekundy % 60
min = sekundy // 60 % 60
hour = sekundy // 3600 % 24
print(f" {hour}:{min}:{sek}")


