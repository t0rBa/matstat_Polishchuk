import numpy as np

A = np.array([1, 2, 3, 4])
B = np.array([5, 6, 7, 8])

print("Арифметичні операції поелементно:")

print("Сума A + B:", A + B)
print("Різниця A - B:", A - B)
print("Добуток A * B:", A * B)
print("Ділення A / B:", A / B)
print("Цілочисельне ділення A // B:", A // B)
print("Остача A % B:", A % B)
print("Піднесення до степеня A ** B:", A ** B)

C = np.concatenate((A, B))
print("\nНовий масив C (A + B):", C)

print("Максимальний елемент C:", np.max(C))
print("Мінімальний елемент C:", np.min(C))

print("Сума елементів C:", np.sum(C))

print("Добуток елементів C:", np.prod(C))
