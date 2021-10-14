import matplotlib.pyplot as plt
import numpy as np
import math as m

#sin(x)/x
x=np.linspace(-m.pi*3, m.pi*3, 100)
y=[m.sin(i)/i for i in x]
plt.title("sin(x)/x")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()     
plt.plot(x, y)
plt.show()

#(x^3-6x^2+3x)/|x|
x=np.linspace(-10, 10, 100)
y=[(i**3-6*i**2+3*i)/abs(i) for i in x]
plt.title("(x^3-6x^2+3x)/|x|")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()     
plt.plot(x, y)
plt.show()

#2^sinx and 2^x
x = np.linspace(-m.pi, m.pi, 100)
y1 = [2**m.sin(i) for i in x]
y2 = [2**i for i in x]
plt.title("2^sin(x) && 2^x")
plt.xlabel("x")
plt.ylabel("y1, y2")
plt.grid()     
plt.plot(x, y1, label='2^sin(x)')
plt.plot(x, y2, label='2^x')
plt.legend(loc='best', fontsize=14)
plt.show()

#x^2-2x-4-|x^+x-2|
x=np.linspace(-10, 10, 100)
y=[i**2-2*i-4-abs(i**2+i-2) for i in x]
plt.title("x^2-2x-4-|x^+x-2|")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()     
plt.plot(x, y)
plt.show()

#1/(x-2) +1
x=np.linspace(-10, 10, 100)
y=[1/(i-2)+1 for i in x]
plt.title("1/(x-2) +1")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()     
plt.plot(x, y)
plt.show()

#sqrt(x)*sqrt(1-x)
x=np.linspace(0, 1, 100)
y=[m.sqrt(i)*m.sqrt(1-i) for i in x]
plt.title("sqrt(x)*sqrt(1-x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()     
plt.plot(x, y)
plt.show()
