import numpy as np
from sklearn.preprocessing import Imputer

f = open('train.mv.txt')
out = open('train-v2.txt', 'w')

for line in f:
    out.write(line.replace('?', 'nan'))

f.close()
out.close()


f = np.loadtxt('train-v2.txt')
imp = Imputer(strategy='most_frequent')
imp.fit(f)
imputed = imp.transform(f)

np.savetxt('train-imputed.txt', imputed, fmt='%.6f')

