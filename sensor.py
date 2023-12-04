
import random



class sensor():
    def __init__(self,codeSensor,nameSensor,ifOn):
        self.nameSensor = nameSensor;
        self.codeSensor=codeSensor;
        self.ifOn=ifOn;
    def readSense(self):
            value = random.randint(0, 1)
            return value;


sensorCars=[sensor(1,"carForA",0)
    ,sensor(2,"carForB",0)
    ,sensor(3,"carForC",0)
    ,sensor(4,"carForD",0)];

sensorMens=[sensor(5,"menForA1",0)
    ,sensor(6,"menForA2",0)
    ,sensor(7,"menForB1",0)
    ,sensor(8,"menForB2",0)
    ,sensor(9,"menForC1",0)
    ,sensor(9,"menForC2",0)
    ,sensor(10,"menForD1",0)
    ,sensor(11,"menForD2",0),];











