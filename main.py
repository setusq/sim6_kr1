#М3О-234Б-22 Симонова,Матвеенко 6 группа
import numpy as np
import matplotlib.pyplot as plt

# Создаем массивы x1 и x2
x1 = np.linspace(0, 40, 100)
x2 = np.linspace(0, 40, 100)

# Создаем сетку X1 и X2
X1, X2 = np.meshgrid(x1, x2)

# Определяем функцию Z
plt.figure(figsize=(8, 6))
plt.xlabel('x1')
plt.ylabel('x2')

plt.plot(x1, (141 - 4 * x1) / 5, label='4*X1 + 5*X2 = 141', color='red', linestyle='dashed')

plt.axvline(x=19, color='gray', linestyle='dashed', label='x1=19')
plt.axhline(y=17, color='gray', linestyle='dashed', label='x2=17')

plt.arrow(0, 0, 3, 5, head_width=0.5, head_length=0.7, fc='black', ec='black', label='вектор z (3, 5)')

perpendicular_x = np.array([5, -5])
perpendicular_y = np.array([-3, 3])
plt.plot(perpendicular_x, perpendicular_y, linestyle='dashed', color='green', label='перпендикуляр')

plt.title('Линейная функция')

plt.text(10, 17, 'Ограничение', fontsize=10, color='red', rotation=-38)
plt.text(20, 10, 'x1=19', fontsize=10, color='gray')
plt.text(5, 17.5, 'x2=17', fontsize=10, color='gray')
plt.text(3, 2.5, 'z (3, 5)', fontsize=10, color='black')
plt.text(-4, 2, 'Перпендикуляр', fontsize=10, color='green')

plt.grid(True)
plt.legend()
plt.show()
