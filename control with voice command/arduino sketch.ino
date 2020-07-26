String data;
int LED = 12;

void setup() {
  Serial.begin(9600);
  pinMode(LED,OUTPUT);
  Serial.println("Hi!, I am Arduino");
}

void loop() {
  
  while(Serial.available()==0){
//    Serial.println(data);
  }
  
  data = Serial.readString(); 
   
  if (data == "turn on"){
    digitalWrite(LED,HIGH);
  }
  
  if(data == "turn off"){
    digitalWrite(LED,LOW);
}
}
