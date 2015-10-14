/* Mobin Anandwala.
BME 595 Implantable Systems
Final Project
Force differential using Force sensing resistors
This code is a modification of the code obtained from the following
learn.adafruit.com/force-sensitive-resistor-fsr/using-an-fsr */

int fsrPin0 = 0; // FSR1 and R1 = 10K is connected to input pin a0
int fsrReading0; // Reading from FSR0 voltage divider
int fsrVoltage0; // analog reading from pin0 converted to voltage
unsigned long fsrResistance0; // Voltage from pin0 converted to resistance
unsigned long fsrConductance0; // Conductance measured in micromhos
long fsrForce0; // Force from resistance on pin0
int fsrPin1 = 1; // analog reading from pin1 connected to voltage
int fsrReading1; // Reading from FSR1 voltage divider
int fsrVoltage1; // reading from pin1 converted to voltage3
unsigned long fsrResistance1; // voltage from pint converted to resitance
unsigned long fsrConductance1; // Conductance measured in micromhos
long fsrForce1; // Force from resistance on pin1
const float Area = 0.000127; // Area of 0.5 in diameter FSR
long pressure0; // Pressure from FSR0
long pressure1; // Pressure from FSR1
const float maxpressure = 31233677.2; // maximum hoop stress using pressure = atmospheric

void setup(void) {
  Serial.begin(9600);  // Debugging information sent via serial
}

void loop(void) {
  // From Pin0
  fsrReading0 = analogRead(fsrPin0);
  fsrReading1 = analogRead(fsrPin1);
  
  // analog voltage reading is from 0 to 1023 where 0 is 0V and 1023 is 5V = 5000mV
  fsrVoltage0 = map(fsrReading0, 0, 1023, 0, 5000);
  Serial.println("Voltage reading in mV on pin0 = ");
  Serial.println(fsrVoltage0);
  fsrVoltage1 = map(fsrReading1, 0, 1023, 0, 5000);
  Serial.println("Voltage reading in mV on pin1 = ");
  Serial.println(fsrVoltage1);
  
  if (fsrVoltage0 == 0) {
    Serial.println("No Pressure from FSR0");
  } else {
    // The voltage = Vin * R1/(R1 + FSR) where R1 = 10K and Vin = 5V
    // FSR = ((Vin - V)* R)/V voltage divider
    fsrResistance0 = 5000 - fsrVoltage0; // Voltage in mV
    fsrResistance0 *= 10000; // 10K  Resistor
    fsrResistance0 /= fsrVoltage0;
   
   fsrConductance0 = 1000000;  // Conductance measured in micromhos
   fsrConductance0 /= fsrResistance0;
  
   // Using the FSR graphs to obtain the force
   if (fsrConductance0 <= 1000) {
     fsrForce0 = fsrConductance0 / 80;
     Serial.println("Force in Newtons on FSR0 = ");
     Serial.println(fsrForce0);
   } else {
     fsrForce0 = fsrConductance0 - 1000;
     fsrForce0 /= 30;
     Serial.println("Force in Newtons on FSR0 =  ");
     Serial.println(fsrForce0);
   }
  }
  if (fsrVoltage1 == 0) {
    Serial.println("No Pressure from FSR1");
  } else {
    // The voltage = Vin * R1/(R1 + FSR) where R1 = 10K and Vin = 5V
    // FSR = ((Vin - V)* R)/V voltage divider
    fsrResistance1 = 5000 - fsrVoltage1; // Voltage in mV
    fsrResistance1 *= 10000; // 10K  Resistor
    fsrResistance1 /= fsrVoltage1;
   
   fsrConductance1 = 1000000;  // Conductance measured in micromhos
   fsrConductance1 /= fsrResistance1;
   
   
   // Using the FSR graphs to obtain the force
   if (fsrConductance1 <= 1000) {
     fsrForce1 = fsrConductance1 / 80;
     Serial.println("Force in Newtons on FSR1 = ");
     Serial.println(fsrForce1);
   } else {
     fsrForce1 = fsrConductance1 - 1000;
     fsrForce1 /= 30;
     Serial.println("Force in Newtons on FSR1 = ");
     Serial.println(fsrForce1);
   }
  }
  pressure0 = fsrForce0/Area;
  Serial.println("Pressure in Pa on FSR0 = ");
  Serial.println(pressure0);
  pressure1 = fsrForce1/Area;
  Serial.println("Pressure in Pa on FSR1 = ");
  Serial.println(pressure1);
 
  if (pressure0 > maxpressure) {
     Serial.println("Failure has occured from FSR0");
  } else {
     Serial.println("Failure has not occured");
  
  if (pressure1 > maxpressure) {
  Serial.println("Failure has occured from FSR1");
  } else {
  Serial.println("Failure has not occured");
   }
  }
}
