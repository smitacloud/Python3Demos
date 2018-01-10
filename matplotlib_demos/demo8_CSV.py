'''
here major new things are importing numpy, and then using numpy's loadtxt function. Loadtxt can be used to load more than just .txt files. It's just load things with text, that's all. Here, we are unpacking the contents of exampleFile.csv, using the delimiter of a comma. It's important to note here that you MUST unpack the exact same number of columns that will come from the delimiter that you state. If not, you'll get an error.
'''
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

x,y = np.loadtxt('exampleFile.csv',
                 unpack=True,
                 delimiter = ',')

plt.plot(x,y)

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()
