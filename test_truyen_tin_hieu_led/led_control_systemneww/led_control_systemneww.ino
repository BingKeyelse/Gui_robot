# define ledPin 13  // assign I/O pin to the internal Led of Arduino
float pos =0,desired_pos;
float end_pos,t_on,t_off;
int count;
void setup() {
 Serial.setTimeout(50); // tạo timer
 Serial.begin(115200);  //tốc độ truyền 
 while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  } 
 pinMode(LED_BUILTIN, OUTPUT);

}// lệnh auto đúng
void recieve_str()
{
  int pos=0,k[3];  

  String symbol;
  String readStr;
  char buffer[50]={};
  if(Serial.available()>0) // check serial Ocupation 
  {
    Serial.readBytes(buffer,50);
    String data = buffer;
    int lengthData = data.length();
    for (int i=0; i<lengthData;i++)
      {
        symbol = data.charAt(i);
        if( symbol.equals(",") == true)
        {
          k[pos]=i+1;
          pos++;
        }
      }
     String str1 = data.substring(0,k[0]);
     String str2 = data.substring(k[0],k[1]);
     String str3 = data.substring(k[1],lengthData);
     end_pos   = str1.toFloat();
     t_on      = str2.toFloat();
     t_off     = str3.toFloat();
     desired_pos = end_pos;
     count =0;
  }
}

void OnOffBlink(int tOn, int tOff){

static int timer=tOn;
  static long previousMillis;
  
  if ((millis() - previousMillis) >= timer) {
    
    if (digitalRead(ledPin) == HIGH) {
      timer = tOff;
    } else {
      timer = tOn;
    }

digitalWrite(ledPin, !digitalRead(ledPin));
     previousMillis = millis();
  }
}

void loop() {
  float Delta = 1.0;
  recieve_str();
  if(pos<desired_pos)
  {
       pos +=Delta;
       OnOffBlink(t_on,t_off);
       count+=1;
  }
  else if(pos>desired_pos)
  {
       pos -= Delta;
       OnOffBlink(t_on,t_off);
       count+=1;
  }
  else{    }
  Serial.print(pos);
  Serial.print(",");
  Serial.print(t_on);
  Serial.print(",");
  Serial.print(t_off);
  Serial.print(",");
//  Serial.print((t_on/(t_on+t_off))*100);
//  Serial.print(",");
  Serial.println(count);
  delay(500);
//  Serial.flush() ; 
  
  
}
