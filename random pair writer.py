import numpy as np
import time

with open('example.txt', 'w') as fo:
    fo.write('')
with open('example2.txt', 'w') as fo:
    fo.write('')
with open('example3.txt', 'w') as fo:
    fo.write('')
with open('examplen.txt', 'w') as fo:
    fo.write('')
with open('rexample.txt', 'w') as fo:
    fo.write('')

i = 0
angle = 0
x = 0
y = 0
z = 0

while True:
    with open('example.txt', 'a') as fo:
        fo.write(str(i) + ',' + str(np.random.randint(0, 8)) + '\n')

    with open('example2.txt', 'a') as fo:
        fo.write(str(i) + ',' + str(np.random.randint(0, 8)) + '\n')

    with open('example3.txt', 'a') as fo:
        fo.write(str(i) + ',' + str(np.random.randint(0, 8)) + '\n')
    i += 1

    with open('examplen.txt', 'a') as fo:
        fo.write(str(np.random.randint(0, 100)) + ',' + str(np.random.randint(0, 100)) + ',' + str(
            np.random.randint(0, 100)) + ',' + 't' + ',' + str(
            np.random.randint(0, 100)) + ',' + str(np.random.randint(0, 100)) + ',' + str(
            np.random.randint(0, 100)) + ',' + 'f' + ',' + str(
            np.random.randint(0, 100)) + ',' + str(np.random.randint(0, 100))+ '\n')

    angle = angle + np.random.randint(-15, 15)
    x = (x + np.random.random())/i
    y = (y + np.random.random())/i
    z = (z + np.random.random())/i
    with open('rexample.txt', 'a') as fo:
        fo.write(str(angle) + ',' + str(x) + ',' + str(y) + ',' + str(z) + '\n')

    time.sleep(0.5)
