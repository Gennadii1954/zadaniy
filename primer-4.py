n = int(input())
naib = 0  # наибольшее число
while n > 0:
    c = n % 10  # последняя цифра
    n = n // 10  # число без последней цифры
    if c > naib:
        naib = c

print(naib)




