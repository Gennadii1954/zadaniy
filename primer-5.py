v = int(input("Введите значение выручки: "))  # выручка, может быть float
i = int(input("Введите значение издержек: "))  # издержки, может быть float
resultat = v - i
if resultat > 0:
    print("Фирма работает с прибылью")
    rentab = resultat / v
    print('рентабельность = ', round(rentab, 2))  # сделал округление
    sotrudn=int(input("Введите количество сотрудников: "))
    print("Прибыль на одного сотрудника: ", round(
        v / sotrudn, 2))  # сделал округление
else:
    print("Фирма работает с убытком")



