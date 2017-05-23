#include <ESP8266HTTPClient.h>

#include <DHT_U.h>

#include <DHT.h>
#include "ESP8266WiFi.h"

#define DHTTYPE DHT11   // DHT 22  (AM2302), AM2321
#define DHTPIN  12
#define LED_PIN 13

const char* ssid = "Marotzke";
const char* password = "12345678";
DHT dht(DHTPIN, DHTTYPE);

void setup(void)
{
  Serial.begin(9600);
  // Connect to WiFi
  pinMode(LED_PIN, OUTPUT);
  dht.begin();
  WiFi.begin(ssid, password);

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
  float t = dht.readTemperature();
  float h = dht.readHumidity();
  String data = "temperature=" + String(t) + "&humidity=" + String(h);
  
  HTTPClient http;
  http.begin("http://192.168.43.33:5000/set/"+String(t)+"/"+String(h));
  http.GET();//"temp="+ String(t) +"&hum="+ String(h));
  digitalWrite(LED_PIN, HIGH);
  delay(200);
  Serial.println(http.getString());
  http.end();
  
  Serial.print("Humidity (%): ");
  Serial.println(h);
  Serial.print("Temperature (°C): ");
  Serial.println(t);
}
