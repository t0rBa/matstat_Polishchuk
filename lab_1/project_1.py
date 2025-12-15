a = int(input())
b = int(input())

print("ТАК" * (a % b == 0) + "НІ" * (a % b != 0))
