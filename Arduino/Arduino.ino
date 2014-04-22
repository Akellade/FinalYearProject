/*
Author: Aaronn Kelly
Date began: 15/3/14
Made for Arduino Uno

*/

int val = 0;
int powerreq =0 ; // value received from pc for ideal power out.
const float feedbackFactor = 0.009765624; //given by (5/1024)*2  or Vout/analogRead max * 2
int resVal = /*=1;//*/ 82;
float Vout =0;
float powerOut = 0 ;
char inChar ;
int stringComplete = 0;

void setup(){
  // configure hardware timer2 to generate a fast PWM on OC2B (Arduino digital pin 3)
  // set pin high on overflow, clear on compare match with OCR2B
  TCCR2A = 0x23;
  TCCR2B = 0x09;  // select timer2 clock as unscaled 16 MHz I/O clock
  OCR2A = 159;  // top/overflow value is 159 => produces a 100 kHz PWM
  pinMode(3, OUTPUT);  // enable the PWM output (you now have a PWM signal on digital pin 3)
  pinMode(A0, INPUT);
  Serial.begin(4800);
  
}

void loop()
{
  serialEvent();
  
  
 Vout = analogRead(A0) * (feedbackFactor);
 Serial.print("Vout:");
 Serial.print(Vout,3);
 Serial.print("\t");
 
 powerOut = (Vout * Vout) / resVal; //calculate power P=V^2/r
 
 //compare Actual power reading with the power requirement from system
	Serial.print("Power Reading:");
	Serial.print(powerOut,3);
	Serial.print("Watts");
        Serial.print("\n");
	
	
 if (powerOut > powerreq){ 		// if powerout too high 
	OCR2B = --val;  			// decrease the PWM 
	}
 if (powerOut < powerreq){ 		//if powerout too low
         OCR2B = ++val;			// increase the PWM 
	}
 else{	 // else something? ?? not decided yet	
	}
	Serial.print(OCR2B);
        Serial.print("\t\n");

if(OCR2B >159){
         OCR2B = 159;
        }
        


}

void serialEvent() { // repeats once, every time a loop completes. 
  while (Serial.available()) {
                    // get the new byte:
                     powerreq = Serial.parseInt(); // converts ASCII into int, since 'O' =48,
                     Serial.print("\t\t");
                     Serial.print(powerreq);
                     Serial.print("\n\n");
                    // add it to the inputString:
                    
                    // if the incoming character is a newline, set a flag
                    // so the main loop can do something about it:
                    if (inChar == '\n') {
                                    stringComplete = 1;
                                         } 
                   }
}


