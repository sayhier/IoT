/*
  Calibration

 Demonstrates one technique for calibrating sensor input.  The
 sensor readings during the first five seconds of the sketch
 execution define the minimum and maximum of expected values
 attached to the sensor pin.

 The sensor minimum and maximum initial values may seem backwards.
 Initially, you set the minimum high and listen for anything
 lower, saving it as the new minimum. Likewise, you set the
 maximum low and listen for anything higher as the new maximum.

 The circuit:
 * Analog sensor (potentiometer will do) attached to analog input 0
 * LED attached from digital pin 9 to ground

 By David A Mellis
 modified 30 Aug 2011
 By Tom Igoe
 created 29 Oct 2008

 http://www.arduino.cc/en/Tutorial/Calibration

 This example code is in the public domain.

 */

// These constants won't change:
const int tempSensorPin = A0;       // pin that temperature sensor is attached to
const int lightSensorPin = A1;      // pin that lightness sensor is attached to
const int humiditySensorPin = A2;   // pin that humidity sensor is attached to

// variables:
int sensorMin = 1023;        // minimum sensor value
int sensorMax = 0;           // maximum sensor value



float temp;
float lightness;
float humidity;

float tempRangeLow = -40.0;     // range low of temperature sensor
float tempRangeHi = 110.0;      // range hi of temperature sensor
float lightRangeLow = 0.0;
float lightRangeHi = 1.0;
float humidityRangeLow = 0.0;
float humidityRangeHi = 1.0;


int tempSensorValue = 0;      // the sensor value of temperature sensor, 0~255
int lightSensorValue = 0;     // the sensor value of lightness sensor, 0~255
int humiditySensorValue = 0;  // the sensor value of humidity sensor, 0~255

char str[] = "temperature";


void sendMeg(String sensorID_1,float sensorValue_1, String sensorID_2,float sensorValue_2, String sensorID_3,float sensorValue_3, String sensorID_4,float sensorValue_4, String sensorID_5,float sensorValue_5)
{
Serial.println("AT");
delay(2000);

Serial.println("AT+CREG?"); //check registration
delay(2000);

Serial.println("AT+CGATT?"); //check attach to GSM
delay(2000);

Serial.println("AT+CSTT"); //set APN
delay(2000);

Serial.println("AT+CIICR"); //激活移动场景
delay(20000);

Serial.println("AT+CIFSR"); //check IP
delay(2000);

Serial.println("AT+CIPSTART=\"TCP\",\"sayhier.gicp.net\",39654"); //connect remote server
delay(5000);

Serial.println("AT+CIPSEND"); //
delay(2000);

Serial.print(sensorID_1); Serial.print(","); Serial.print(sensorValue_1, 2); Serial.print(",");
Serial.print(sensorID_2); Serial.print(","); Serial.print(sensorValue_2, 2); Serial.print(",");
Serial.print(sensorID_3); Serial.print(","); Serial.print(sensorValue_3, 2); Serial.print(",");
Serial.print(sensorID_4); Serial.print(","); Serial.print(sensorValue_4, 2); Serial.print(",");
Serial.print(sensorID_5); Serial.print(","); Serial.print(sensorValue_5, 2); 
delay(2000);
Serial.write(0x1A); //
delay(2000);

Serial.println("AT+CIPCLOSE"); //
delay(2000);

}

void sendClose(){
  
}

void setup() {
  // turn on LED to signal the start of the calibration period:
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
  Serial.begin(9600);
}

void loop() {
  // read the sensor:
  tempSensorValue = analogRead(tempSensorPin);
  lightSensorValue = analogRead(lightSensorPin);
  humiditySensorValue = analogRead(humiditySensorPin);

  // apply the calibration to the sensor reading
  //sensorValue = map(sensorValue, sensorMin, sensorMax, 0, 255);

  // in case the sensor value is outside the range seen during calibration
  //sensorValue = constrain(sensorValue, 0, 255);

  // fade the LED using the calibrated value:
  //analogWrite(ledPin, sensorValue);

  char sensor[] = "temperature";
  
  Serial.print("Temperature:");Serial.println(tempSensorValue);
  Serial.print("Lightness:");Serial.println(lightSensorValue);
  Serial.print("Humidity:");Serial.println(humiditySensorValue);
  Serial.print(sensor);
  Serial.println();
  delay(2000);
  
  float spare_1, spare_2;
  sendMeg("Temperature",float(tempSensorValue),"Lightness",float(lightSensorValue),"Humidity",float(humiditySensorValue),"Spare",spare_1,"Spare",spare_2);
  delay(30*1000);
}
