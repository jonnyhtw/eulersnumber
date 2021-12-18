import matplotlib.pyplot as plt
import numpy as np

n=10000
totalnumber=np.zeros(n)

for i in range(n):

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

plt.savefig('e.png')

plt.show();
