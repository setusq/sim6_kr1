#М3О-234Б-22 Симонова,Матвеенко 6 группа
import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 30, 100)
x2 = np.linspace(0, 30, 100)

X1, X2 = np.meshgrid(x1, x2)

constraint = 4*X1 + 5*X2

plt.figure(figsize=(8, 6))
plt.xlabel('x1')
plt.ylabel('x2')
contour = plt.contour(X1, X2, constraint, levels=[141], colors='red', linestyles='dashed')
plt.axhline(color='red', linestyle='dashed', label='4*X1 + 5*X2')
plt.axvline(x=19, color='gray', linestyle='dashed', label='x1=19')
plt.axhline(y=17, color='gray', linestyle='dashed', label='x2=17')





plt.grid(True)
plt.legend()
plt.show()