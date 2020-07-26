import serial
import time

Serial = serial.Serial('com5',9600)
time.sleep(2)

fromHardware = Serial.readline().decode()
print (fromHardware)
print ("Enter turn ON to LED on and turn OFF to LED off")

if __name__ == '__main__':
    while True:
 
        # query = input("enter")
        # if query == 'turn on':
        #     Serial.write(b'ON') #send 1 to arduino
        #     print("LED turned ON")
        #     time.sleep(1)

        # if query == 'turn off':
        #     Serial.write(b'OFF') #send 0 to arduino
        #     print("LED turned OFF")
        #     time.sleep(1)

        Serial.write(b'turn on') #send 1 to arduino
        print("LED turned ON")
        time.sleep(3)

        Serial.write(b'turn off') #send 1 to arduino
        print("LED turned OFF")
        time.sleep(2)
    
    