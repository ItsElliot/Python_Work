
int led = 13;


void setup() {                

  pinMode(led, OUTPUT);   
  Serial.begin(9600);  
}


void loop() {
  
    if(Serial.available()>0) {
      char command = Serial.read();
      if(command == '1') {
        digitalWrite(led, HIGH);
        Serial.println("Light is now ON")  
      } 
      else if(command == '0') {
        digitalWrite(led, LOW);
        Serial.println("Light is now OFF")  
    }
      
    }
    
    

//  digitalWrite(led, HIGH);  
//  delay(1000);               
//  digitalWrite(led, LOW);    
//  delay(1000);              
}


