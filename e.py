import math
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np

plt.ion()

n=1000000
totalnumber=np.zeros(n)

for i in tqdm(range(n)):

    sum=0
    number=0

    while sum < 1:
        number+=1 
        sum += np.random.uniform(0,1)
    
    if i ==0:
        totalnumber[i] = number
    if i > 0 :
        totalnumber[i] = totalnumber[i-1]+number

plt.semilogx(np.arange(1,n+1), totalnumber/np.arange(1,n+1))

plt.plot([1,n], [math.e, math.e])

plt.grid()
plt.xlim(10,n)
#plt.ylim(2,3)


plt.savefig('e.png')

plt.show();
