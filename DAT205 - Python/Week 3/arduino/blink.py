#Import libraries
import serial
import mosquitto 

#Connect serial port of the Arduino
port = serial.Serial("/dev/cu.usbmodem1421",9600,timeout=2) 

#Create a client
client = mosquitto.Mosquitto("Elliot")

#Connect to broker using local host
client.connect("127.0.0.1")

#Subscribe to lights 
client.subscribe("lights")

#This method deals with the messages recived
def messageReceived (broker, obj, msg):
    #Make the client global
    golbal client
    
    #Create var that holds the payload of either ON or OFF
    LonLoff = msg.payload
    
    #If payload message is equal to "ON" send "1" which will turn LED on 
    if (LonLoff == "ON"):
        port.write("1")
        
    #If payload message is equal to "OFF" send "0" which will turn LED off    
    elif (LonLoff == "OFF"):
        port.write("0")

#Run client
while True:
    client.loop()
    
    
    