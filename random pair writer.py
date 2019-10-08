import numpy as np
import time

i = 0

while True:
    with open('example.txt', 'a') as fo:
        fo.write(str(i) + ',' + str(np.random.randint(0, 8)) + '\n')
    i += 1
    time.sleep(0.5)
