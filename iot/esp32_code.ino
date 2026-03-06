#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "YOUR_WIFI";
const char* password = "PASSWORD";

int trigPin = 5;
int echoPin = 18;

long duration;
int distance;

void setup() {

Serial.begin(115200);

pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);

WiFi.begin(ssid,password);

while(WiFi.status()!=WL_CONNECTED){
delay(500);
Serial.println("Connecting...");
}

Serial.println("Connected");
}

void loop(){

digitalWrite(trigPin, LOW);
delayMicroseconds(2);

digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);

duration = pulseIn(echoPin, HIGH);
distance = duration * 0.034 / 2;

int level = map(distance,20,0,0,100);

if(WiFi.status()==WL_CONNECTED){

HTTPClient http;

http.begin("http://SERVER_IP:5000/update");
http.addHeader("Content-Type","application/json");

String data = "{\"level\":" + String(level) + "}";

http.POST(data);
http.end();
}

delay(5000);
}
