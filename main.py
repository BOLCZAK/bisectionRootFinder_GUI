import matplotlib.pyplot as plt
import numpy as np

# inquirer

def licz(funkcja, przedzial, epsilon, max_iter, nazwa):
    a, b = przedzial
    i = 0
    while i < max_iter:
        # print(abs(a-b))
        if not abs(a - b) < epsilon:
            if funkcja(a) * funkcja(b) < 0:
                x = (a + b) / 2
                if funkcja(x) == 0:
                    print(f'{x} jest miejscem zerowym funkcji')
                else:
                    if funkcja(a) * funkcja(x) < 0:
                        a, b = a, x
                        print(x)
                    else:
                        a, b = x, b
                        print(x)
            else:
                print('Na podanym przedziale funkcja nie ma miejsc zerowych !!!')
        else:
            print('Osiągnięto zamierzoną dokładność lecz nie znaleziono miejsc zerowych')
            i = max_iter
        i += 1
    print('Przekroczono maksymalną zadaną ilość iteracji')

    # print(a, b, 'DZIALA', f'{x} = X')

    x_values = np.linspace(przedzial[0], przedzial[1], num=100)
    y_values = [funkcja(x) for x in x_values]

    plt.figure(1)
    plt.plot(x_values, y_values)
    try:
        plt.scatter(x, funkcja(x), c='red')
    except NameError:
        pass
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(nazwa)
    plt.grid()
    plt.show()


def wielomian(x):
    return 5 * x ** 3 + 4 * x ** 2 - 4 * x - 7


def trygonometryczna(x):
    return np.sin(x) ** 2 - np.cos(x) + 3 * x - 7


def wykladnicza(x):
    return 5 ** x - 4


print('====WYBIERZ FUNKCJĘ====')
print('Podaj odpowiedni numer opcji')
print('1) Weilomian 5x^3+4x^2-4x-7')
print('2) Trygonometryczna sin(x)^2-cos(x)+3x-7')
print('3) Wykładnicza 5^x-4')
func = input('Podaj funckję jaką chcesz wybrać: ')
print('Podaj przedział na jakim chcesz zbadać funkcję: ')
przedzial = tuple([float(input()) for x in range(2)])
epsilon = float(input('Podaj dokładność epsilon wyniku: '))
max_iter = float(input('Podaj maksymalną ilość iteracji: '))

print(type(przedzial), '\t\t', przedzial)
print(type(epsilon), '\t\t', epsilon)
print(type(max_iter), '\t\t', max_iter)

if func == str(1):
    licz(wielomian, przedzial, epsilon, max_iter, '5x^3+4x^2-4x-7')
elif func == str(2):
    licz(trygonometryczna, przedzial, epsilon, max_iter, 'sin(x)^2-cos(x)+3x-7')
elif func == str(3):
    licz(wykladnicza, przedzial, epsilon, max_iter, '5^x-4')
