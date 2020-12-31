

//String sendData(String command, const int timeout) {
//  String response = "";
//  Serial1.println(command);
//  long int time = millis();
//  while ((time + timeout) > millis()) {
//    while (Serial1.available()) {
//      char c = Serial1.read();
//      response += c;
//    }
//  }
//  
//  Serial.println(response);
//  return response;
//}

//void setup() {
////  Serial1.begin(9600);
////  Serial.begin(9600);
//  pinMode(8, OUTPUT);
//}
//
//String response = "";
//void loop() {
//  digitalWrite(8, 1 - digitalRead(8));
//  delay(1000);
////  response = "";
////  if(Serial.available()) {
////    response = Serial.readString();
////    Serial.println(response);
////    sendData(response, 1000);
////  }
////  response = "";
////  if(Serial1.available()) {
////    while (Serial1.available()) {
////      char c = Serial1.read();
////      response += c;
////    }
////    Serial.println(response);
////  }
//}

void setup() {
  pinMode(A2, INPUT);
  pinMode(8, OUTPUT);
  Serial.begin(9600);
  Serial1.begin(9600);
}

void loop() {
  digitalWrite(8, 1 - digitalRead(8));
  Serial.println(analogRead(A2));
  Serial1.println(analogRead(A2));
  delay(1000);
}
