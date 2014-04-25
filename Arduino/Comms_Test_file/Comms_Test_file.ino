/*
Serial comms python test file
*/
int powerReq = 0;

void setup() {
  // put your setup code here, to run once:
 Serial.begin(9600);
 
 
}

void loop() {
  // put your main code here, to run repeatedly:
  
  

    
       
 
    Serial.print("1"); //Vin
    //delay(500);
    Serial.print("2"); //Power OUT
    //delay(500);
    Serial.print(powerReq); //Power Needed
    //delay(500);
    Serial.print("4"); //PWM
    //delay(500);
    
}

void serialEvent() { // repeats once, every time a loop completes. 
  while (Serial.available()) {
                    // get the new byte:
                     powerReq = Serial.parseInt(); // converts ASCII into int, since 'O' =48,
                     
                     digitalWrite(13,HIGH);
                     delay(10);
                     digitalWrite(13,LOW); 
                   
                    // add it to the inputString:
                    
                    // if the incoming character is a newline, set a flag
                    // so the main loop can do something about it:
                   
                   }
}

