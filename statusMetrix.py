import numpy as np
import numpy.ma as ma
import sensor
rightStatus=[[1,0,1,0,0,0,1,1,0,0,1,1],
             [0,1,0,1,1,1,0,0,1,1,0,0],
             [1,0,1,0,0,0,1,1,0,0,1,1],
             [0,1,0,1,1,1,0,0,1,1,0,0],
             [0,1,0,1,1,1,1,1,1,1,1,1],
             [1,0,1,0,1,1,1,1,1,1,1,1],
             ];
nowStatus=np.zeros(shape=(6, 12))

collision1=np.matrix([[1,0,1,0,0,0,1,1,0,0,1,1],[0,1,0,1,1,1,0,0,1,1,0,0],
[1,0,1,0,0,0,1,1,0,0,1,1],[0,1,0,1,1,1,1,1,1,1,1,1],[0,1,0,1,1,1,1,1,1,1,1,1],[1,0,1,1,1,1,1,1,1,1,1,1],])
maskCollision1 = ma.masked_array(collision1, mask= [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,1,0,0,1,1],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0]])

collision2=[]
collision3=[]
collision4=[]
collision5=[]
collision6=[]
collision7=[]
collision8=[]
listSensor=np.array([0,0,0,0,0,0,0,0,0,0,0,0]);
nowStatus=np.insert(listSensor,listSensor,listSensor);
nowStatus=np.insert(listSensor,listSensor,listSensor);

def statusNow(ListSensor):
    i = 0;
    while i < 4:
        listSensor[i] = sensor.sensorCars[i].readSense();
        if (listSensor[i] == 0):
            # This is not the actual value of the sensor
            sensor.sensorCars[i].ifOn = 0;
        else:
            sensor.sensorCars[i].ifOn = 1;
    while i < 12:
        listSensor[i] = sensor.sensorMens[i].readSense();
        if (listSensor[i] == 0):
            # This is not the actual value of the sensor
            sensor.sensorMens[i].ifOn = 0;
        else:
            sensor.sensorMens[i].ifOn = 1;

#new metrix



#def collisions:
#השוואה לכל סוגי ההתנגשויות
#def prioroty2cars:
#פונקציה לחישוב עדיפות של 2 מכוניות
#def priorotyMenandcar:
#פונקציה לחישוב עדיפות של מכונית והולך רגל
#def priorityBusyIntersection:
#פונקציה לחישוב עדיפויות שכל הצומת מלאה
