import random
import matplotlib.pyplot as plt
import numpy as np


# Unique değerleri bulmak için yardımcı bir fonksiyon
def get_unique_numbers(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    return unique


def findfunctionmaxmin(find, matrix):
    """
    Fonksiyon, hesaplanması gereken fonksiyonun katsayılarını array şeklinde almaktadır.
    Eşitsizlikleri matrix şeklinde almaktadır.
    Örneğin:
    z = 6x1 + 8x2

    7x1 + 3x2 <= 21
    6x1 + 7x2 <= 42
    x1 <= 3
    x2 <= 4

    için verilmesi gereken değerler şöylerdir.
    find: [6, 8]

    matrix: [[7, 3, 21, 1],
            [6, 7, 42, 1],
            [1, 0, 3, 1],
            [0, 1, 4, 1],
            ]
    Matrix dizisinde ki her satır sonu eşitsizliğin <= veya >= olduğunu gösteririr.
     kullanınız.

    :param find: Hesaplanması gereken fonksiyonun katsayıları
    :param matrix: Verilen eşitliklerin katsayıları ve min max durumu
    :return:
    """

    allFunctionValues = []
    crossXAxesAll = None
    crossYAxesAll = None
    coordinates = []

    # Eşitliklerin x1 ve x2 eksenlerini kestiği noktaları bulma
    for func in matrix:
        x1, x2, value, minMax = func
        if x1 != 0:
            crossXAxes = value / x1
        if crossXAxesAll is None or crossXAxes > crossXAxesAll:
            crossXAxesAll = crossXAxes
        if (x2 != 0) and (crossYAxesAll is None or value / x2 > crossYAxesAll):
            crossYAxesAll = value / x2

    # Eşitliklerin x2 değerlerini bulma
    x_values = np.arange(0, int(crossXAxesAll) + 1, 0.01)
    for func in matrix:
        x1, x2, value, minMax = func
        f = [[]]
        if x2 == 0:
            f[0].append((value / x1))
            f.append(minMax)
            f.append(True)
            allFunctionValues.append(f)
            continue
        for x in x_values:
            f[0].append((value - x1 * x) / x2)
        f.append(minMax)
        allFunctionValues.append(f)

    # Koordinat sistemini oluşturma ve grafikleri çizme
    fig, ax = plt.subplots()
    ax.set_ylim(bottom=0, top=crossYAxesAll)
    ax.set_xlim(left=0, right=crossXAxesAll)
    for values in allFunctionValues:
        r = random.random()
        b = random.random()
        g = random.random()
        color = (r, g, b)
        if len(values[0]) == 1 and len(values) == 2:
            ax.plot(x_values, [values[0][0] for i in range(len(x_values))], c=color)
        elif len(values) == 3:
            ax.plot([values[0][0], values[0][0]], [0, crossYAxesAll], c=color)
        else:
            ax.plot(x_values, values[0], c=color)

    # Grafikteki taralı alanı bulma
    between1 = np.array([])
    between2 = np.array([0 for i in range(len(x_values))])
    for values in allFunctionValues:
        if len(values[0]) == 1:
            continue
        if len(between1) == 0:
            between1 = values[0].copy()
            continue
        if values[1] == 1:
            i = 0
            for value in values[0]:
                if value < between1[i]:
                    between1[i] = value
                i = i + 1
        if values[1] == 0:
            i = 0
            for value in values[0]:
                if value > between2[i]:
                    between2[i] = value
                i = i + 1
    ax.fill_between(x_values, between1, between2,
                    facecolor="red", alpha=0.5)
    for index_values, values in enumerate(allFunctionValues):
        if len(values[0]) == 1:
            value = values[0][0]
            index = np.where(x_values == float(value))
            index = index[0][0]
            if values[1] == 1:
                x_values = x_values[0: index + 1]
                between1 = between1[0: index + 1]
                between2 = between2[0: index + 1]
            else:
                x_values = x_values[index + 1:]
                between1 = between1[index + 1:]
                between2 = between2[index + 1:]
            allFunctionValues.pop(index_values)

    # Eşitliklerin kesişen noktalarını bulma
    for index, values in enumerate(allFunctionValues):
        idx = np.argwhere(np.diff(np.sign(0 - np.array(values[0])))).flatten()
        if len(idx) != 0 and len(x_values) - 1 > idx[0]:
            idx = idx[0]
            coordinates.append([x_values[idx], values[0][idx]])
        for i in range(index + 1, len(allFunctionValues)):
            idx = np.argwhere(np.diff(np.sign(np.array(values[0]) - np.array(allFunctionValues[i][0])))).flatten()
            if len(idx) != 0:
                idx = idx[0]
                coordinates.append([x_values[idx], values[0][idx]])
    for values in allFunctionValues:
        coordinates.append([0, values[0][0]])
    if between1[0] > 0 and between2[0] == 0:
        coordinates.append([0, 0])

    coordinates = get_unique_numbers(coordinates)

    solution_coordinates = []

    # Taralı alanı oluşturan noktaları bulma
    for x, y in coordinates:
        if (y - 0.1 <= between1[int(x / 0.01)] <= y + 0.1) or (y - 0.1 <= between2[int(x / 0.01)] <= y + 0.1):
            if solution_coordinates.count([x, y]) == 0:
                solution_coordinates.append([x, y])

    # Değerleri hesaplayıp konsola yazdırma
    solutionMin = None
    solutionMax = None
    minCoordinate = None
    maxCoordinate = None
    for x1, x2 in solution_coordinates:
        value = find[0] * x1 + find[1] * x2
        if solutionMin is None or solutionMin > value:
            solutionMin = value
            minCoordinate = [x1,x2]
        if solutionMax is None or solutionMax < value:
            solutionMax = value
            maxCoordinate = [x1, x2]

    plt.plot(minCoordinate[0], minCoordinate[1], 'ro', color="green", label="Min Value Coordinate")
    plt.plot(maxCoordinate[0], maxCoordinate[1], 'ro', color="blue", label="Max Value Coordinate")

    print("Max Value: ", solutionMax)
    print("Min Value: ", solutionMin)

    ax.set_xlabel('x1')
    ax.set_ylabel('x2')

    plt.legend()
    plt.show()


matrix = np.array([[7, 3, 21, 1],
                   [6, 7, 42, 1],
                   [1, 0, 3, 1],
                   [0, 1, 4, 1],
                   ])

findfunctionmaxmin([6, 8], matrix)
