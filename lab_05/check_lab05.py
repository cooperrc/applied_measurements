import numpy as np

def check_p02(a, b):
    if (np.abs((a--3.163 )/3.163 )<0.05) & (np.abs((b-1.647 )/1.6474 )<0.05):
        points = 2
        print('Nice work!')
        return points
    else:
        points = 0
        print('Whoops, try again')
        return points
    
