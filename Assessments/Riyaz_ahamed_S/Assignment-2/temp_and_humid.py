import random

#function to check humidity and temperature
def detect(temperature,humidity):
    if(humidity<30):
        if(temperature>30):
            print("Humidity : ",humidity,"Temperature : ",temperature,"Alarm Turned On")
        else:
            print("Humidity : ",humidity,"Temperature : ",temperature,"Alarm Turned OFF")
    else:
        print("Humidity : ",humidity,"Temperature : ",temperature,"Alarm Turned OFF")
            
#for generating random humidity and temperature values
for i in range(0,15):
    temperature = random.randint(15,50)
    humidity = random.randint(15,50)
    detect(temperature,humidity)
