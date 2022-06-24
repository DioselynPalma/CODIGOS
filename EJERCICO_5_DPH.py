import numpy as np

ar = np.random.randint(0, 100, size=(100, 1)) 
ar2 = np.random.randint(0, 100, size=(100, 1)) 

sumtol = (np.sum(ar, axis=0)) + (np.sum(ar2, axis=0))
print (sumtol)