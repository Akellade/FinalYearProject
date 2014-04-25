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
  
  

    
         powerReq = Serial.parseInt();
       
  else{
    Serial.print("1"); //Vin
    //delay(500);
    Serial.print("2"); //Power OUT
    //delay(500);
    Serial.print(powerReq); //Power Needed
    //delay(500);
    Serial.print("4"); //PWM
    //delay(500);
    }
}
