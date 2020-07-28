#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ThingSpeak.h>

const char* ssid = "Param"; 
const char* password = "9582@paramsingh";

int Relay = D2;

WiFiServer server(80);
WiFiClient client;

unsigned long myChannelNumber =  1107673; //Your Channel Number (Without Brackets)
const char * myReadAPIKey = "xxxxxxxxxx"; //Your Write API Key

void setup() {
  Serial.begin (115200);
  delay (10);

  pinMode(Relay, OUTPUT);
  digitalWrite(Relay, LOW);
  
  //CONNECT TO WIFI NETWORK 
  Serial.println();
  Serial.println();
  Serial.println("connecting to");
  Serial.println(ssid);
  
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED){
    delay(1000);
    Serial.print(".");
  }
  
  Serial.println("");
  Serial.println("WiFi connected");
  
  //START THE SERVER
  server.begin ();
  Serial.println("Server Started");
  
  //Print the IP address 
  Serial.println("Use this URL to connect:");
  Serial.print("http://");
  Serial.print(WiFi.localIP());
  Serial.println("/");
  
  ThingSpeak.begin(client);
  }
  
void loop(){
  
  long temp = ThingSpeak.readLongField(myChannelNumber, 1, myReadAPIKey);
  int statusCode = ThingSpeak.getLastReadStatus();

  if(statusCode == 200){
    if(temp == 1)
    {
      digitalWrite(Relay, HIGH);
      Serial.println("HIGH");
      Serial.println(temp);
    }
    if (temp == 0)
    {
      digitalWrite(Relay, LOW);
      Serial.println("LOW");
      Serial.println(temp);
    } 
  } 
  else
  {
    Serial.println("Unable to read channel / No internet connection");
  }
  delay(100);
}
