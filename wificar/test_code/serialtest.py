from time import sleep
import serial


ser = serial.Serial('/dev/tty.usbmodem1d11', 9600) # Establish the connection on a specific port
#counter = 32 # Below 32 everything in ASCII is gibberish
while True:
     #counter +=1
     #ser.write(str(chr(counter))) # Convert the decimal number to ASCII then send it to the Arduino
     print ser.readline() # Read the newest output from the Arduino
     sleep(.1) # Delay for one tenth of a second
     #if counter == 255:
      #  counter = 32


#void setup() {
#    Serial.begin(9600); // set the baud rate
#    Serial.println("Ready"); // print "Ready" once
#}
#void loop() {
#    char inByte = ' ';
#    if(Serial.available()){ // only send data back if data has been sent
#        char inByte = Serial.read(); // read the incoming data
#        Serial.println(inByte); // send the data back in a new line so that it is not all one long line 
#    }
#    delay(100); // delay for 1/10 of a second
#}