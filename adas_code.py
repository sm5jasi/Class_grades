
def read_data(f):
    
    import numpy as np
   
    g = np.loadtxt(f, delimiter = ",", skiprows = 1, unpack = True, dtype = "str")
    grades = g[1]
    
    return grades 
