#include <ESP8266HTTPClient.h>
#include "ESP8266WiFi.h"

#define LED_PIN 13

int sensorPin = 0;    // select the input pin for the potentiometer
int sensorValue = 0;  // variable to store the value coming from the sensor
 
int sensorVCC = 12;

const char* ssid = "Marotzke";
const char* password = "12345678";

void setup(void)
{
  Serial.begin(9600);
  // Connect to WiFi
  pinMode(LED_PIN, OUTPUT);
  WiFi.begin(ssid, password);
  
   pinMode(sensorVCC, OUTPUT); 
   digitalWrite(sensorVCC, LOW);

  // while wifi not connected yet, print '.'
  // then after it connected, get out of the loop
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  //print a new line, then print WiFi connected and the IP address
  Serial.println("");
  Serial.println("WiFi connected");
  // Print the IP address
  Serial.println(WiFi.localIP());
}
void loop() {
  digitalWrite(LED_PIN, LOW);
  delay(1000);

  // power the sensor
  digitalWrite(sensorVCC, HIGH);
  delay(100); //make sure the sensor is powered
  // read the value from the sensor:
  sensorValue = analogRead(sensorPin); 
  //stop power 
  digitalWrite(sensorVCC, LOW);  
 
  HTTPClient http;
  http.begin("http://192.168.43.84:5000/set/"+String(sensorValue));
  http.GET();
  digitalWrite(LED_PIN, HIGH);
  delay(200);
  Serial.println(http.getString());
  http.end();

  //wait
  delay(5*1000);          
  Serial.print("Soil Humidity = " );                       
  Serial.println(sensorValue);  
}
