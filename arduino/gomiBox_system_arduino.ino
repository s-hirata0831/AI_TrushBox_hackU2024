#include <Adafruit_NeoPixel.h>

#define PIN_CAN 6
#define PIN_PET 7
#define LED_NUM 14  //LEDの数
#define RESULT_CAN_PIN 5
#define OPEN_SIGNAL_PIN 4
#define RESET_NUM_SW 3

float Vcc = 5.0;
int cnt_pet=0;
int cnt_can=0;
double distance;
bool coverIsOpened = false;
bool objectIsPassed = false;

double getDistance();
void setLed(bool isCan, int num);
void inLed(bool isCan);
void offLed(bool isCan);
void fallingLed(bool isCan, int num);
void allOffLed();
void warningRedLed(bool isCan);

Adafruit_NeoPixel ledtape_can = Adafruit_NeoPixel(LED_NUM, PIN_CAN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel ledtape_pet = Adafruit_NeoPixel(LED_NUM, PIN_PET, NEO_GRB + NEO_KHZ800);  

void setup()  
{
  Serial.begin(9600);
  ledtape_can.begin();
  ledtape_pet.begin();
  pinMode(4, OUTPUT);
  pinMode(RESULT_CAN_PIN, INPUT); // 外部PULL_DOWN
  pinMode(OPEN_SIGNAL_PIN, INPUT); // 外部PULL_DOWN
  pinMode(RESET_NUM_SW, INPUT_PULLUP);
  digitalWrite(2, LOW);  
}

void loop()  
{
  if(digitalRead(RESET_NUM_SW) == LOW){ // pushed reset_num sw
    cnt_pet=0;
    cnt_can=0;
    allOffLed();
  }else{
    if(digitalRead(OPEN_SIGNAL_PIN) == HIGH){
      if(coverIsOpened == false){
        delay(10000);
        coverIsOpened = true;
      }
      distance = getDistance();
      if(distance < 35 && objectIsPassed == false){
        objectIsPassed = true;
        if(digitalRead(RESULT_CAN_PIN) == HIGH){
          fallingLed(true, cnt_can);
          cnt_can++;
        }else{
          fallingLed(false, cnt_pet);
          cnt_pet++;
        }
        digitalWrite(2, HIGH);
      }
      digitalWrite(2, LOW);
    }else{
      coverIsOpened = false;
      objectIsPassed = false;
      if(cnt_can == 14) warningRedLed(true);
      if(cnt_pet == 14) warningRedLed(false);
    }
  } 
}

double getDistance(){
  double dist1=0.0;
  for(int i=0;i<1000;i++){
    dist1 += Vcc*analogRead(A0)/1023;
    }
    dist1 /= 1000;
    return 26.549*pow(dist1,-1.2091);
}

void setLed(bool isCan, int num){
  uint8_t can_color = 100;
  uint8_t pet_color = 100;
  if(isCan){
    offLed(true);
    for(int i = 13; i >= 14-num; i--)
    {
      ledtape_can.setPixelColor(i, ledtape_can.Color(can_color, 0, can_color));
    }
  }else{
    offLed(false);
    for(int i = 13; i >= 14-num; i--) 
    {
      ledtape_pet.setPixelColor(i , ledtape_pet.Color(0, pet_color, pet_color));
    }
  }
}

void inLed(bool isCan){
  uint8_t can_color = 100;
  uint8_t pet_color = 100;
  if(isCan){
    for(int i = 0; i < LED_NUM; i++)
    {
      offLed(true);
      ledtape_can.setPixelColor(i, ledtape_can.Color(150, 0, 150));
      ledtape_can.show();
      delay(50);
    }
  }else{
    for(int i = 0; i < LED_NUM; i++)
    {
      offLed(false);
      ledtape_pet.setPixelColor(i, ledtape_pet.Color(0, 150, 150));
      ledtape_pet.show();
      delay(50);
    }
  }
}

void fallingLed(bool isCan, int num){
  uint8_t can_color = 100;
  uint8_t pet_color = 100;
  if(isCan){
    setLed(isCan, num);
    for(int i=0; i <= 13-num;i++){
      if(i>0) ledtape_can.setPixelColor(i-1, ledtape_can.Color(0, 0, 0));
      ledtape_can.setPixelColor(i, ledtape_can.Color(can_color, 0, can_color));
      ledtape_can.show();
      delay(100);
    }
  }else{
    setLed(isCan, num);
    for(int i=0; i <= 13-num;i++){
      if(i>0) ledtape_pet.setPixelColor(i-1, ledtape_pet.Color(0, 0, 0));
      ledtape_pet.setPixelColor(i, ledtape_pet.Color(0, pet_color, pet_color));
      ledtape_pet.show();
      delay(100);
    }
  }
  
}

void offLed(bool isCan){
  if(isCan){
    for(int i=0; i<14; i++){
      ledtape_can.setPixelColor(i, ledtape_can.Color(0, 0, 0));
    }
  }else{
    for(int i=0; i<14; i++){
      ledtape_pet.setPixelColor(i, ledtape_pet.Color(0, 0, 0));
    }
  }
}

void allOffLed(){
  for(int i=0; i < 14; i++){
    ledtape_can.setPixelColor(i, ledtape_can.Color(0, 0, 0));
    ledtape_pet.setPixelColor(i, ledtape_pet.Color(0, 0, 0));
  }
  ledtape_can.show();
  ledtape_pet.show();
}

void warningRedLed(bool isCan){
  if(isCan){
    for(int i=0; i < 14; i++){
      ledtape_can.setPixelColor(i, ledtape_can.Color(150, 0, 0));
    }
    ledtape_can.show();
  }else{
    for(int i=0; i < 14; i++){
      ledtape_pet.setPixelColor(i, ledtape_pet.Color(150, 0, 0));
    }
    ledtape_pet.show();
  }
}