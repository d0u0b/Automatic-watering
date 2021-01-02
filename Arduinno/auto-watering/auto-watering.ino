#include <DHT.h>
#include <DHT_U.h>

#include <ArduinoJson.h>

StaticJsonDocument<200> jsonbuffer;
String outputBuffer;

DHT dht(8, DHT11);

int getSoilMoisture() {
  return analogRead(A0);
}

double getTemp(){
  return dht.readTemperature();
}

double getHumi(){
  return dht.readHumidity();
}

void watering(){
  digitalWrite(9, LOW);
  delay(3000);
  digitalWrite(9, HIGH);
}

void setup() {
  pinMode(A0, INPUT);
  digitalWrite(9, HIGH);
  pinMode(9, OUTPUT);
  dht.begin();
  Serial.begin(9600);
  Serial1.begin(9600);
}

void loop() {
  int moisture = getSoilMoisture();
  jsonbuffer["SM"] = moisture;
  jsonbuffer["temp"] = getTemp();
  jsonbuffer["humi"] = getHumi();
  jsonbuffer["water"] = moisture > 800;
  outputBuffer = "";
  serializeJson(jsonbuffer, outputBuffer);
  Serial.println(outputBuffer);
  Serial1.println(outputBuffer);
  if(moisture > 800) {
    watering();
  }
  delay(30000);
}
