##CODE written by Ferrulli Massimiliano


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from scipy.special import factorial


fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(121)



x, y = symbols('x y')
y = sin(x)
x0 = 3
n = 10
total_sum = 0
i = 1000
x_vals = np.linspace(-10, 10, i)
y_or = np.sin(x_vals)
for i in range(n + 1):
    derivative = diff(y, x, i)
    value_at_x0 = derivative.subs(x, x0)
    result = value_at_x0 * (x - x0)**i * factorial(i, exact=True)**(-1)
    total_sum += result

    print("Total Sum:", total_sum)


# Convert the symbolic expression to a numeric function
total_sum_numeric = lambdify(x, total_sum)

# Evaluate the numeric function using the x values
y_vals = total_sum_numeric(x_vals)

# Plot the total sum function

plt.plot(x_vals, y_or)
plt.plot(x_vals, y_vals)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polinomio di Taylor')
plt.grid(True)

plt.xlim(x0 - 13, x0 + 7)

plt.ylim(-3, 3)

plt.show()





