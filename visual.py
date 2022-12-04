import math
import matplotlib.pyplot as plt
import numpy as np
def rastrigin(*X, **kwargs):
    A = kwargs.get('A', 10)
    return A + sum([(x**2 - A * np.cos(2 * math.pi * x)) for x in X])
def FunctionVisualizationRastrigin():
    '(Начальное значение , конечное значение, кол-во образцов для генерации)'
    X = np.linspace(-4, 4, 100)
    Y = np.linspace(-4, 4, 100)
    '''Функция meshgrid() создает список массивов координатных сеток N-мерного координатного 
     для указанных одномерных массивов координатных векторов. 
     Координатное пространство - это пространство N-мерных точек-координат, причем каждой точке в таком 
     пространстве соответствует комбинация одного значения из каждого координатного массива.'''
    X, Y = np.meshgrid(X, Y)

    Z = rastrigin(X, Y, A=10)

    fig = plt.figure('Rastrigin')
    ax = fig.add_subplot(projection='3d')
    'показатели x,y,z на графике'
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    'my_cmap - радужная расцветка'
    my_cmap = plt.get_cmap('hsv')

    fig2 = plt.figure('Plosk')
    ax2 = fig2.add_subplot(projection='3d')
    ax2.contourf(X, Y, Z, zdir='z', offset=-4, cmap='hsv')
    ax2.set(xlim=(-4, 4), ylim=(-4,4), zlim=(-4,4),
            xlabel='X', ylabel='Y', zlabel='Z')
    'построение поверхности в трёхмерном пространстве'
    ax.plot_surface(X, Y, Z, cmap = my_cmap, edgecolor ='none')
    'построение проекции на ось z'
    plt.show()
FunctionVisualizationRastrigin()