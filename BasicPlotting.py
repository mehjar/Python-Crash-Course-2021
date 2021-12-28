import matplotlib.pyplot as plt
import numpy as np

# plt.plot()
# plt.show()

x = np.linspace(1,10,10)
y = x

plt.figure(dpi = 300)
plt.plot(x,y,'bo-')
plt.xlabel('x')
plt.ylabel('y')

# plt.show()
plt.savefig('myfig2.pdf')
