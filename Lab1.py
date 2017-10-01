from numpy import *

penalty = 5000


def file_reader():

    f = open('coordinates.txt', 'r')
    file = f.read().split("\n")

    a = []

    for i in range(len(file)):
        a.append(file[i].split())

    for i in range(len(a)):
        for j in range(2):
            a[i][j] = float(a[i][j])

    print(a)
    f.close()

    return a


def start():
    a = file_reader()

    result_penalty = 0
    x = [0, 0]

    for y in a:
        scalar = cross(y, x)
        x = y
        if scalar > 0:
            result_penalty += penalty

    print('Итоговая сумма штрафов: ', result_penalty)

    return


start() # точка входа в программу