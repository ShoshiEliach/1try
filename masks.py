import numpy as np
import numpy.ma as ma
import statusMetrix
def maskCollision1(nowStatus):
    mx = ma.masked_array(nowStatus, mask=[[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,1,0,0,1,1],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0]])
    if(mx==statusMetrix.maskCollision1):
        return 1;
        return 0;

