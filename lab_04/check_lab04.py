import numpy as np

def check_p02a(q):
    if np.abs((q-272.358 )/272.358 )<0.05:
        points = 2
        print('Nice work!')
        return points
    else:
        points = 0
        print('Whoops, try again')
        return points

def check_p02b(Tho, Tco):
    if (np.abs((Tho-68.428 )/68.428 )<0.05) & (np.abs((Tco-99.894 )/99.894 )<0.05):
        points = 2
        print('Nice work!')
        return points
    else:
        points = 0
        print('Whoops, try again')
        return points
    
def check_p03(eps):
    if np.abs((eps-0.39 )/0.39 )<0.05:
        points = 2
        print('Nice work!')
        return points
    else:
        points = 0
        print('Whoops, try again')
        return points
