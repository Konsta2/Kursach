# реализация оптимизации роя частиц на python (PSO)
# минимизация функции растригина

import random
import math  # cos() для Растригина
import copy  # удобное копирование массива
import sys  # чтобы узнать максимальное значение, которое может быть сохранено внутри переменной float


# -------fitness functions---------

# Функция Растригина
def fitness_rastrigin(position):
    fitnessVal = 0.0
    for i in range(len(position)):
        xi = position[i]
        #Формула растригина
        fitnessVal += (xi * xi) - (10 * math.cos(2 * math.pi * xi)) + 10
    return fitnessVal

# -------------------------

# Класс Частицы
class Particle:
    def __init__(self, fitness, dim, minx, maxx, seed):
        self.rnd = random.Random(seed)

        # инициализируем положение частицы значением 0.0
        self.position = [0.0 for i in range(dim)]

        # инициализируем скорость частицы значением 0.0
        self.velocity = [0.0 for i in range(dim)]

        # инициализируем наилучшее положение частицы со значением 0.0
        self.best_part_pos = [0.0 for i in range(dim)]

        # вычисление случайного положения и скорости
        # диапазон положения и скорости равен [minx, maxx]
        for i in range(dim):
            self.position[i] = ((maxx - minx) *
                                self.rnd.random() + minx)
            self.velocity[i] = ((maxx - minx) *
                                self.rnd.random() + minx)

        # вычислить пригодность частицы
        self.fitness = fitness(self.position)  # curr fitness

        # инициализировать наилучшее положение и пригодность этой частицы
        self.best_part_pos = copy.copy(self.position)
        self.best_part_fitnessVal = self.fitness  # best fitness


# функция оптимизации роя частиц
def pso(fitness, max_iter, n, dim, minx, maxx):
    # гиперпараметры
    w = 0.729  # инерция
    c1 = 1.49445  # когнитивный (частица)
    c2 = 1.49445 # социальный (рой)

    rnd = random.Random(0)
    # создать n случайных частиц
    swarm = [Particle(fitness, dim, minx, maxx, i) for i in range(n)]

    # вычислите значение best_position и best_fitness в swarm
    best_swarm_pos = [0.0 for i in range(dim)]
    best_swarm_fitnessVal = sys.float_info.max  # swarm best

    # computer best particle of swarm and it's fitness
    for i in range(n): # проверьте каждую частицу
        if swarm[i].fitness < best_swarm_fitnessVal:
            best_swarm_fitnessVal = swarm[i].fitness
            best_swarm_pos = copy.copy(swarm[i].position)

    # основной цикл pso
    Iter = 0
    while Iter < max_iter:

        # после каждых 10 итераций
        # выведите номер итерации и наилучшее значение пригодности на данный момент
        if Iter % 10 == 0 and Iter > 1:
            print("Iter = " + str(Iter) + " best fitness = %.3f" % best_swarm_fitnessVal)

        for i in range(n): # обрабатывайте каждую частицу

            # вычислить новую скорость частицы curr
            for k in range(dim):
                r1 = rnd.random()  # рандомизация
                r2 = rnd.random()
                #корреляция для скорости c учетом инерции
                swarm[i].velocity[k] = (
                        (w * swarm[i].velocity[k]) +
                        (c1 * r1 * (swarm[i].best_part_pos[k] - swarm[i].position[k])) +
                        (c2 * r2 * (best_swarm_pos[k] - swarm[i].position[k]))
                )

                # если скорость[k] не находится в [minx, max]
                # затем обрежьте его
                if swarm[i].velocity[k] < minx:
                    swarm[i].velocity[k] = minx
                elif swarm[i].velocity[k] > maxx:
                    swarm[i].velocity[k] = maxx
            # вычислить новое положение, используя новую скорость

            for k in range(dim):
                swarm[i].position[k] += swarm[i].velocity[k]

            # вычислить пригодность новой позиции
            swarm[i].fitness = fitness(swarm[i].position)

            # является ли новое положение новым наилучшим для частицы?
            if swarm[i].fitness < swarm[i].best_part_fitnessVal:
                swarm[i].best_part_fitnessVal = swarm[i].fitness
                swarm[i].best_part_pos = copy.copy(swarm[i].position)

            # является ли новая позиция новым лучшим результатом в целом?
            if swarm[i].fitness < best_swarm_fitnessVal:
                best_swarm_fitnessVal = swarm[i].fitness
                best_swarm_pos = copy.copy(swarm[i].position)

        # для-каждой частицы
        Iter += 1
    # конец цикла
    return best_swarm_pos


# конец pso


# ----------------------------
# Вывод минимизации функции растригина

print("\nНачните оптимизацию роя частиц с помощью функции растригина\n")
dim = 3
fitness = fitness_rastrigin

print("Цель состоит в том, чтобы минимизировать функцию Растригина в " + str(dim) + " переменные")
print("Функция имеет известное значение min = 0.0 при (", end="")
for i in range(dim - 1):
    print("0, ", end="")
print("0)")

num_particles = 80
max_iter = 100

print("Установка num_particles =" + str(num_particles))
print("Установка max_iter    = " + str(max_iter))
print("\nНачало PSO алгоритма\n")

best_position = pso(fitness, max_iter, num_particles, dim, -4.0, 4.0)

print("\nPSO завершен\n")
print("\nНайдено лучшее решение:")
print(["%.6f" % best_position[k] for k in range(dim)])
fitnessVal = fitness(best_position)
print("пригодность наилучшего решения = %.6f" % fitnessVal)

