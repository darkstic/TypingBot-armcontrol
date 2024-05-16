void setup() {
    Serial.begin(9600);
    pinMode(13, OUTPUT);
}

void loop() {
    if (Serial.available()) {
        char receivedChar = Serial.read();
        Serial.print("Received: ");  // Print a label
        Serial.println(receivedChar);  // Print the received character
    }
}
