#include <Wire.h>
int y[2]={A0,A3};
int x[2]={A1,A4};
int sw_pin1=A2;
int sw_pin2=A5;
struct Toggle{
  int toggle_x;
  int toggle_y;
};
void setup() {
  // put your setup code here, to run once:
  pinMode(sw_pin1,INPUT);
  pinMode(sw_pin2,INPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  Toggle toggle[2];
  for(int i=0;i<2;i++){
    toggle[i].toggle_x=analogRead(x[i]);
    toggle[i].toggle_y=analogRead(y[i]);
  }
  for(int i=0;i<2;i++){
    Serial.print(toggle[i].toggle_x);
    Serial.print(" ");
    Serial.print(toggle[i].toggle_y);
    Serial.print("  ");
  }
  Serial.println("");
  delay(10);
}
