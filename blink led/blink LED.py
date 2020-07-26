import serial
import time

Serial = serial.Serial('com5',9600)
time.sleep(2)

fromHardware = Serial.readline().decode()
print (fromHardware)

if __name__ == '__main__':
    while True:
        Serial.write(b'turn on') #send 1 to arduino
        print("LED turned ON")
        time.sleep(3)

        Serial.write(b'turn off') #send 1 to arduino
        print("LED turned OFF")
        time.sleep(2)
    
    
