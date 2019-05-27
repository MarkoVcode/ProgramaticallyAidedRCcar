//https://wiki.dfrobot.com/Beetle_SKU_DFR0282
//Silkscreen  Digital Pin PWM Channel Analog Channel  UART  I2C
//RX  0     Serial1 
//TX  1       
//SDA 2       SDA
//SCL 3 3     SCL
//9 9 9 A9    
//10  10  10  A10   
//11  11  11      
//A0  A0    A0    
//A1  A1    A1    
//A2  A2    A2    

#define CH1A     A2
#define CH1B     A1
#define CH2A     A0
#define CH2B     2
#define CH2C     3
#define CH2D     11


void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(CH1A, OUTPUT);
  pinMode(CH1B, OUTPUT);
  pinMode(CH2A, OUTPUT);
  pinMode(CH2B, OUTPUT);
  pinMode(CH2C, OUTPUT);
  pinMode(CH2D, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(CH1A, HIGH);
  digitalWrite(CH1B, HIGH);
  digitalWrite(CH2A, HIGH);
  digitalWrite(CH2B, HIGH);
  digitalWrite(CH2C, HIGH);
  digitalWrite(CH2D, HIGH);  
  delay(1000);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW);
  digitalWrite(CH1A, LOW);
  digitalWrite(CH1B, LOW);
  digitalWrite(CH2A, LOW);
  digitalWrite(CH2B, LOW);
  digitalWrite(CH2C, LOW);
  digitalWrite(CH2D, LOW);  // turn the LED off by making the voltage LOW
  delay(1000);                       // wait for a second
}
