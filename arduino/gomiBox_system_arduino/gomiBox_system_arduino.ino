#include <Adafruit_NeoPixel.h>
#include <SoftwareSerial.h>
#include <Servo.h>

#define PIN_CAN 6
#define PIN_PET 7
#define LED_NUM 30  //LEDの数
#define RESULT_CAN_PIN 5
#define OPEN_SIGNAL_PIN 4
//#define RESET 12
#define CAP_SW 12
#define JETSON_SERIAL_RX A1
#define JETSON_SERIAL_TX A2
#define PIC_SERIAL_RX A3
#define PIC_SERIAL_TX A4
#define SERVO_PET 9
#define SERVO_CAN 10
#define SERVO_MINICOLA 11
#define SERVO_CLOSE_ANGLE 0
#define SERVO_OPEN_ANGLE 100
#define SEG_OFF 10
#define SEG_ATARI 20
#define SEG_HAZURE 30
#define SEG_END 50

SoftwareSerial jetsonSerial(JETSON_SERIAL_RX, JETSON_SERIAL_TX);
SoftwareSerial picSerial(PIC_SERIAL_RX, PIC_SERIAL_TX);
Servo petServo;
Servo canServo;
Servo miniColaServo;

float Vcc = 5.0;
int cnt_pet = 0;
int cnt_can = 0;
int rand_num;
double distance;
bool coverIsOpened = false;
bool objectIsPassed = false;
bool petCoverIsOpened;
uint8_t object;

double getDistance();
void setLed(bool isCan, int num);
void inLed(bool isCan);
void offLed(bool isCan);

void fallingLed(bool isCan, int num);
void allOffLed();
void warningRedLed(bool isCan);

void openCover(bool is_pet);
void closeCover(bool is_pet);

Adafruit_NeoPixel ledtape_can = Adafruit_NeoPixel(LED_NUM, PIN_CAN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel ledtape_pet = Adafruit_NeoPixel(LED_NUM, PIN_PET, NEO_GRB + NEO_KHZ800);  

void setup()  
{
  jetsonSerial.begin(9600);
  picSerial.begin(9600);
  Serial.begin(9600);  
  
  ledtape_can.begin();
  ledtape_pet.begin();
  petServo.attach(SERVO_PET);
  canServo.attach(SERVO_CAN);
  miniColaServo.attach(SERVO_MINICOLA);

  pinMode(4, OUTPUT);
  pinMode(RESULT_CAN_PIN, INPUT); // 外部PULL_DOWN
  pinMode(OPEN_SIGNAL_PIN, INPUT); // 外部PULL_DOWN
  pinMode(CAP_SW, INPUT);
  digitalWrite(2, LOW);  
  delay(5000);
  jetsonSerial.println("serial_start");
}

//void(* resetFunc) (void) = 0; //declare reset function

void loop()  
{
  jetsonSerial.println("main-loop");
  delay(1000);
  while(true){
    picSerial.println("wait ai");
    jetsonSerial.println("wait ai");
    if(Serial.available()){ //どちらが検知されたかを取得
      object = Serial.read();
      //object = "can";
      jetsonSerial.println(object);
      if(object == 112){ //pet
        openCover(true);
        break;
      }else if(object == 99){ //can
        openCover(false);
        break;
      }
    }    
  }
  delay(1000);
  while(true){
    distance = getDistance();
    jetsonSerial.println(distance);
    if(distance < 35){
      jetsonSerial.print("pass");
      if(object == 112){ //pet
        closeCover(true);
        fallingLed(false, cnt_pet);
        cnt_pet++;
        while(digitalRead(CAP_SW) == LOW){} //キャップが入るまで待つ
        picSerial.write(SEG_ATARI);
        jetsonSerial.println("seg-atari");
        miniColaServo.write(0);
        delay(1000);
        miniColaServo.write(90);        
        //while(picSerial.read() != SEG_END){}
      }else{
        closeCover(false);
        fallingLed(true, cnt_can);
        cnt_can++;
        picSerial.write(SEG_ATARI);
        jetsonSerial.println("seg-atari");
        miniColaServo.write(0);
        delay(1000);
        miniColaServo.write(90);
        //while(picSerial.read() != SEG_END){}
      }
      break;
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
    for(int i = LED_NUM-num; i <= LED_NUM-1; i++)
    {
      ledtape_can.setPixelColor(i, ledtape_can.Color(can_color, 0, can_color));
    }
  }else{
    offLed(false);
    for(int i = LED_NUM-num; i <= LED_NUM-1; i++) 
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
    for(int i=0; i <= (LED_NUM-1)-num;i++){
      if(i>0) ledtape_can.setPixelColor(i-1, ledtape_can.Color(0, 0, 0));
      ledtape_can.setPixelColor(i, ledtape_can.Color(can_color, 0, can_color));
      ledtape_can.show();
      delay(100);
    }
  }else{
    setLed(isCan, num);
    for(int i=0; i <= (LED_NUM-1)-num;i++){
      if(i>0) ledtape_pet.setPixelColor(i-1, ledtape_pet.Color(0, 0, 0));
      ledtape_pet.setPixelColor(i, ledtape_pet.Color(0, pet_color, pet_color));
      ledtape_pet.show();
      delay(100);
    }
  }
  
}

void offLed(bool isCan){
  if(isCan){
    for(int i=0; i<LED_NUM; i++){
      ledtape_can.setPixelColor(i, ledtape_can.Color(0, 0, 0));
    }
  }else{
    for(int i=0; i<LED_NUM; i++){
      ledtape_pet.setPixelColor(i, ledtape_pet.Color(0, 0, 0));
    }
  }
}

void allOffLed(){
  for(int i=0; i < LED_NUM; i++){
    ledtape_can.setPixelColor(i, ledtape_can.Color(0, 0, 0));
    ledtape_pet.setPixelColor(i, ledtape_pet.Color(0, 0, 0));
  }
  ledtape_can.show();
  ledtape_pet.show();
}

void warningRedLed(bool isCan){
  if(isCan){
    for(int i=0; i < LED_NUM; i++){
      ledtape_can.setPixelColor(i, ledtape_can.Color(150, 0, 0));
    }
    ledtape_can.show();
  }else{
    for(int i=0; i < LED_NUM; i++){
      ledtape_pet.setPixelColor(i, ledtape_pet.Color(150, 0, 0));
    }
    ledtape_pet.show();
  }
}

int checkSerialData(String data){
  
}

void openCover(bool is_pet){
  if(is_pet){
    petServo.write(SERVO_OPEN_ANGLE);
  }else{
    canServo.write(0);
  }
}

void closeCover(bool is_pet){
  if(is_pet){
    petServo.write(SERVO_CLOSE_ANGLE);
  }else{
    canServo.write(180);
  }
}