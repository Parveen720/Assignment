from cProfile import label

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

subject=['java','python','maths','physics','c++']
sem1=[80,90,90,80,79]
sem2=[89,90,79,89,70]

#pltting with diffrent lines style

plt.plot(subject,sem1,label='semester1',linestyle='-.',marker='o',color='red')
plt.plot(subject,sem2,label='semester2',linestyle='--',marker='x',color='yellow')

plt.xlabel("subject")
plt.ylabel("marks")
plt.title("semester marks comperision")
plt.grid(True)
plt.legend()
plt.show()