import time
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x * x - 5 * x + 5


def df(x):
    return 2 * x - 5


N = 20  # число итераций
xx = 0  # начальное значение
lmd = 0.9  # шаг сходимости
x_plt = np.arange(0, 5.0, 0.1)
f_plt = [f(x) for x in x_plt]

plt.ion()  # включение интерактивного режима для отображения для графиков
fig, ax = plt.subplots()  # создание осей для графика
ax.grid(True)  # создание сетки для графика
ax.plot(x_plt, f_plt)  # отображение параболы
point = ax.scatter(xx, f(xx), c="red")  # отображение точки красным цветом

for i in range(N):
    xx = xx - lmd * df(xx)  # изменение аргумента на текущей позиции
    point.set_offsets([xx, f(xx)])  # отображение нового положения точки

    # перерисовка графика и задержка на 20 секунд
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.02)

plt.ioff()  # выключение интерактивного режима отображения графиков
print(xx)
ax.scatter(xx, f(xx), c="blue")
plt.show()
