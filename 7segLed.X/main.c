/**
  Generated Main Source File

  Company:
    Microchip Technology Inc.

  File Name:
    main.c

  Summary:
    This is the main file generated using PIC10 / PIC12 / PIC16 / PIC18 MCUs

  Description:
    This header file provides implementations for driver APIs for all modules selected in the GUI.
    Generation Information :
        Product Revision  :  PIC10 / PIC12 / PIC16 / PIC18 MCUs - 1.81.8
        Device            :  PIC16F1769
        Driver Version    :  2.00
*/

/*
    (c) 2018 Microchip Technology Inc. and its subsidiaries. 
    
    Subject to your compliance with these terms, you may use Microchip software and any 
    derivatives exclusively with Microchip products. It is your responsibility to comply with third party 
    license terms applicable to your use of third party software (including open source software) that 
    may accompany Microchip software.
    
    THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER 
    EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY 
    IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS 
    FOR A PARTICULAR PURPOSE.
    
    IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE, 
    INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND 
    WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP 
    HAS BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO 
    THE FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL 
    CLAIMS IN ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT 
    OF FEES, IF ANY, THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS 
    SOFTWARE.
*/

#include "mcc_generated_files/mcc.h"

#define OFF 10
#define ATARI 20
#define HAZURE 30

void displayClear(){
  A_SetHigh();
  B_SetHigh();
  C_SetHigh();
  D_SetHigh();
  E_SetHigh();
  F_SetHigh();
  G_SetHigh();
}
void displayZero(){
  displayClear();
  A_SetLow();
  B_SetLow();
  C_SetLow();
  D_SetLow();
  E_SetLow();
  F_SetLow();
}
void displayOne(){
  displayClear();
  B_SetLow();
  C_SetLow();
}
void displayTwo(){
  displayClear();
  A_SetLow();
  B_SetLow();
  G_SetLow();
  E_SetLow();
  D_SetLow();
}
void displayThree(){
  displayClear();
  A_SetLow();
  B_SetLow();
  G_SetLow();
  C_SetLow();
  D_SetLow();
}
void displayFour(){
  displayClear();
  F_SetLow();
  G_SetLow();
  B_SetLow();
  C_SetLow();
}
void displayFive(){
  displayClear();
  A_SetLow();
  F_SetLow();
  G_SetLow();
  C_SetLow();
  D_SetLow();
}
void displaySix(){
  displayClear();
  A_SetLow();
  F_SetLow();
  G_SetLow();
  C_SetLow();
  D_SetLow();
  E_SetLow();
}
void displaySeven(){
  displayClear();
  F_SetLow();
  A_SetLow();
  B_SetLow();
  C_SetLow();
}
void displayEight(){
  displayClear();
  A_SetLow();
  B_SetLow();
  C_SetLow();
  D_SetLow();
  E_SetLow();
  F_SetLow();
  G_SetLow();
}
void displayNine(){
  displayClear();
  A_SetLow();
  B_SetLow();
  G_SetLow();
  F_SetLow();
  C_SetLow();
}

void displaySegments(int num){
  displayClear();
  switch (num)
  {
  case 0:
    displayZero();
    break;
  case 1:
    displayOne();
    break;
  case 2:
    displayTwo();
    break;
  case 3:
    displayThree();
    break;
  case 4:
    displayFour();
    break;
  case 5:
    displayFive();
    break;
  case 6:
    displaySix();
    break;
  case 7:
    displaySeven();
    break;
  case 8:
    displayEight();
    break;
  case 9:
    displayNine();
    break;

  default:
    return;
  }
  DELAY_milliseconds(1);
}

void selectDIG(int dig){
  displayClear();
  DIG_1_SetHigh();
  DIG_2_SetHigh();
  DIG_3_SetHigh();
  DIG_4_SetHigh();

  switch (dig)
  {
    case 1:
      DIG_1_SetLow();
      break;
    case 2:
      DIG_2_SetLow();
      break;
    case 3:
      DIG_3_SetLow();
      break;
    case 4:
      DIG_4_SetLow();
      break;

    default:
      break;
  }
}

void displayRoll(int cnt){
  displayClear();
  switch(cnt){
    case 1:
      A_SetLow();
      B_SetLow();
      break;
    case 2:
      B_SetLow();
      C_SetLow();
      break;
    case 3:
      C_SetLow();
      D_SetLow();
      break;
    case 4:
      D_SetLow();
      E_SetLow();
      break;
    case 5:
      E_SetLow();
      F_SetLow();
      break;
    case 6:
      F_SetLow();
      A_SetLow();
      break;

    default:
      return;
  }
  DELAY_milliseconds(1);
}

void displayLotteryResult(int val){
  int dig_1 = val / 1000;
  int dig_2 = (val / 100) % 10;
  int dig_3 = (val / 10) % 10;
  int dig_4 = val % 10;
  //全桁回転
  for(int x=0; x<3; x++){ //回転回数
    for(int i=1; i<7; i++){ //回転表示1周分
      for(int wait_cnt=0; wait_cnt<10; wait_cnt++){
        for(int j=1; j<5; j++){
          selectDIG(j);
          displayRoll(i);
        }
      }
    }
  }

  //1桁目表示
  for(int x=0; x<1; x++){ //回転回数
    for(int i=1; i<7; i++){ //回転表示1周分
      for(int wait_cnt=0; wait_cnt<10; wait_cnt++){
        for(int j=1; j<5; j++){
          selectDIG(j);
          if(j == 1){
            displaySegments(dig_1);
          }else{
            displayRoll(i);
          }
        }
      }
    }
  }

  //2桁目表示
  for(int x=0; x<1; x++){ //回転回数
    for(int i=1; i<7; i++){ //回転表示1周分
      for(int wait_cnt=0; wait_cnt<10; wait_cnt++){
        for(int j=1; j<5; j++){
          selectDIG(j);
          if(j == 1){
            displaySegments(dig_1);
          }else if(j == 2){
            displaySegments(dig_2);
          }else{
            displayRoll(i);
          }
        }
      }
    }
  }

  //3桁目表示
  for(int x=0; x<1; x++){ //回転回数
    for(int i=1; i<7; i++){ //回転表示1周分
      for(int wait_cnt=0; wait_cnt<10; wait_cnt++){
        for(int j=1; j<5; j++){
          selectDIG(j);
          if(j == 1){
            displaySegments(dig_1);
          }else if(j == 2){
            displaySegments(dig_2);
          }else if(j == 3){
            displaySegments(dig_3);
          }else{
            displayRoll(i);
          }
        }
      }
    }
  }

  //4桁目表示
  for(int wait_cnt=0; wait_cnt<1000; wait_cnt++){
    for(int j=1; j<5; j++){
      selectDIG(j);
      if(j == 1){
        displaySegments(dig_1);
      }else if(j == 2){
        displaySegments(dig_2);
      }else if(j == 3){
        displaySegments(dig_3);
      }else{
        displaySegments(dig_4);
      }
    }
  }
}

void main(void)
{
    // initialize the device
    SYSTEM_Initialize();

    // When using interrupts, you need to set the Global and Peripheral Interrupt Enable bits
    // Use the following macros to:

    // Enable the Global Interrupts
    //INTERRUPT_GlobalInterruptEnable();

    // Enable the Peripheral Interrupts
    //INTERRUPT_PeripheralInterruptEnable();

    // Disable the Global Interrupts
    //INTERRUPT_GlobalInterruptDisable();

    // Disable the Peripheral Interrupts
    //INTERRUPT_PeripheralInterruptDisable();

    while (1)
    {
      if(EUSART_is_rx_ready()){
        uint8_t data = EUSART_Read();
        if(data == OFF){
          displayClear();
        }else if(data == ATARI){
          displayLotteryResult(7777);
          EUSART_Write(50);
        }else if(data == HAZURE){
          displayLotteryResult(7776);
          EUSART_Write(50);
        }else{
          displayClear();
        }
      }
      //displayLotteryResult(7777);
    }
}

/**
 End of File
*/