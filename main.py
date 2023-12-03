import sensor
import numpy

trrafics = ["RED","RED","RED","RED"];
listSensor=[12];
while('true'):
    #after I do the package of numpy
    i=0;
    while i<4:
        listSensor[i] = sensor.sensorCars[i].readSense();
        if(listSensor[i]==0):
            #This is not the actual value of the sensor
            sensor.sensorCars[i].ifOn=0;
        else:
            sensor.sensorCars[i].ifOn = 1;
    while i<12:
        listSensor[i]=sensor.sensorMens[i].readSense();
        if(listSensor[i]==0):
            # This is not the actual value of the sensor
            sensor.sensorMens[i].ifOn = 0;
        else:
            sensor.sensorMens[i].ifOn = 1;
    statusMetrix=listSensor;










