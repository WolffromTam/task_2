import matplotlib.pyplot as plt
import numpy as np
import os
import requests
import scipy.special as sp

def hn(n, x):
    return sp.spherical_jn(n, x) + 1j * sp.spherical_yn(n, x)
def an(n, x):
    return sp.spherical_jn(n, x) / hn(n, x)
def bn(n, x):
    return (x * sp.spherical_jn(n - 1, x) - n * sp.spherical_jn(n, x)) \
    / (x * hn(n - 1, x) - n * hn(n, x))





path = 'results'
if not os.path.exists(path):
    os.mkdir(path)
file = open(r'results\uploaded.txt','wb')
ufr = requests.get("https://jenyay.net/uploads/Student/Modelling/task_02.txt")
file.write(ufr.content)
file.close()
file = open(r'results\uploaded.txt','r')
fline = file.read().split('\n')
flinelist = fline[5].split(" ")
D = float(flinelist[1][2:-1])
fmin = float(flinelist[2][5:-1])
fmax = float(flinelist[3][5:])
F = np.linspace(fmin, fmax, num = 1000)
r = D*0.5 
L = 3e8 / F
k = 2 * np.pi / L 
Sum_arr = [((-1) ** n) * (n + 0.5) * (an(n, k * r) - bn(n, k * r)) \
    for n in range(1, 50)]
Sum = np.sum(Sum_arr, axis=0) 
Sigma = (L ** 2) / np.pi * (np.abs(Sum) ** 2)
fig, ax = plt.subplots()
x = F
y = Sigma
file = open(r'results\task_02_307_VOLKOVSKIY_6.txt','w')
count = 0
while count < x.size:
    file.write(str(x[count]))
    file.write("   ")
    file.write(str(y[count]))
    file.write("\n")
    count += 1
file.close()
ax.plot(x, y)
plt.xlabel('$f, Гц$')
plt.ylabel('$\sigma, м^2$')
plt.show()

