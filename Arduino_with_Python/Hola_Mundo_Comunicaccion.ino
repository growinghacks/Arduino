int valor_limete=800; 
// Este valor es AJUSTABLE depentiendo 
//la humedad que queremos mantener
float humedad=0;

void setup(){
  Serial.begin(9600);
  pinMode(13,OUTPUT); // Diferentes pines que van a enviar las señales electricas para activar las bombas
 }
 
void loop() {
  Serial.println(analogRead(A0)); // Diferentes lectores de valores de humedad
  humedad = analogRead(A0);
  if(analogRead(A0) > valor_limete){ // Programamos para que si los valores no son los deceados activen el pin 
    digitalWrite(13,HIGH);
  }
  else{
    digitalWrite(13, LOW);
  }
  delay (1000);

Serial.println(humedad);
delay(1000);
}
