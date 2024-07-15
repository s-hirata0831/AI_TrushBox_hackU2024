/**
  @Generated Pin Manager Header File

  @Company:
    Microchip Technology Inc.

  @File Name:
    pin_manager.h

  @Summary:
    This is the Pin Manager file generated using PIC10 / PIC12 / PIC16 / PIC18 MCUs

  @Description
    This header file provides APIs for driver for .
    Generation Information :
        Product Revision  :  PIC10 / PIC12 / PIC16 / PIC18 MCUs - 1.81.8
        Device            :  PIC16F1769
        Driver Version    :  2.11
    The generated drivers are tested against the following:
        Compiler          :  XC8 2.36 and above
        MPLAB 	          :  MPLAB X 6.00	
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

#ifndef PIN_MANAGER_H
#define PIN_MANAGER_H

/**
  Section: Included Files
*/

#include <xc.h>

#define INPUT   1
#define OUTPUT  0

#define HIGH    1
#define LOW     0

#define ANALOG      1
#define DIGITAL     0

#define PULL_UP_ENABLED      1
#define PULL_UP_DISABLED     0

// get/set B aliases
#define B_TRIS                 TRISAbits.TRISA4
#define B_LAT                  LATAbits.LATA4
#define B_PORT                 PORTAbits.RA4
#define B_WPU                  WPUAbits.WPUA4
#define B_OD                   ODCONAbits.ODA4
#define B_ANS                  ANSELAbits.ANSA4
#define B_SetHigh()            do { LATAbits.LATA4 = 1; } while(0)
#define B_SetLow()             do { LATAbits.LATA4 = 0; } while(0)
#define B_Toggle()             do { LATAbits.LATA4 = ~LATAbits.LATA4; } while(0)
#define B_GetValue()           PORTAbits.RA4
#define B_SetDigitalInput()    do { TRISAbits.TRISA4 = 1; } while(0)
#define B_SetDigitalOutput()   do { TRISAbits.TRISA4 = 0; } while(0)
#define B_SetPullup()          do { WPUAbits.WPUA4 = 1; } while(0)
#define B_ResetPullup()        do { WPUAbits.WPUA4 = 0; } while(0)
#define B_SetPushPull()        do { ODCONAbits.ODA4 = 0; } while(0)
#define B_SetOpenDrain()       do { ODCONAbits.ODA4 = 1; } while(0)
#define B_SetAnalogMode()      do { ANSELAbits.ANSA4 = 1; } while(0)
#define B_SetDigitalMode()     do { ANSELAbits.ANSA4 = 0; } while(0)

// get/set A aliases
#define A_TRIS                 TRISAbits.TRISA5
#define A_LAT                  LATAbits.LATA5
#define A_PORT                 PORTAbits.RA5
#define A_WPU                  WPUAbits.WPUA5
#define A_OD                   ODCONAbits.ODA5
#define A_SetHigh()            do { LATAbits.LATA5 = 1; } while(0)
#define A_SetLow()             do { LATAbits.LATA5 = 0; } while(0)
#define A_Toggle()             do { LATAbits.LATA5 = ~LATAbits.LATA5; } while(0)
#define A_GetValue()           PORTAbits.RA5
#define A_SetDigitalInput()    do { TRISAbits.TRISA5 = 1; } while(0)
#define A_SetDigitalOutput()   do { TRISAbits.TRISA5 = 0; } while(0)
#define A_SetPullup()          do { WPUAbits.WPUA5 = 1; } while(0)
#define A_ResetPullup()        do { WPUAbits.WPUA5 = 0; } while(0)
#define A_SetPushPull()        do { ODCONAbits.ODA5 = 0; } while(0)
#define A_SetOpenDrain()       do { ODCONAbits.ODA5 = 1; } while(0)

// get/set RB4 procedures
#define RB4_SetHigh()            do { LATBbits.LATB4 = 1; } while(0)
#define RB4_SetLow()             do { LATBbits.LATB4 = 0; } while(0)
#define RB4_Toggle()             do { LATBbits.LATB4 = ~LATBbits.LATB4; } while(0)
#define RB4_GetValue()              PORTBbits.RB4
#define RB4_SetDigitalInput()    do { TRISBbits.TRISB4 = 1; } while(0)
#define RB4_SetDigitalOutput()   do { TRISBbits.TRISB4 = 0; } while(0)
#define RB4_SetPullup()             do { WPUBbits.WPUB4 = 1; } while(0)
#define RB4_ResetPullup()           do { WPUBbits.WPUB4 = 0; } while(0)
#define RB4_SetAnalogMode()         do { ANSELBbits.ANSB4 = 1; } while(0)
#define RB4_SetDigitalMode()        do { ANSELBbits.ANSB4 = 0; } while(0)

// get/set RB5 procedures
#define RB5_SetHigh()            do { LATBbits.LATB5 = 1; } while(0)
#define RB5_SetLow()             do { LATBbits.LATB5 = 0; } while(0)
#define RB5_Toggle()             do { LATBbits.LATB5 = ~LATBbits.LATB5; } while(0)
#define RB5_GetValue()              PORTBbits.RB5
#define RB5_SetDigitalInput()    do { TRISBbits.TRISB5 = 1; } while(0)
#define RB5_SetDigitalOutput()   do { TRISBbits.TRISB5 = 0; } while(0)
#define RB5_SetPullup()             do { WPUBbits.WPUB5 = 1; } while(0)
#define RB5_ResetPullup()           do { WPUBbits.WPUB5 = 0; } while(0)
#define RB5_SetAnalogMode()         do { ANSELBbits.ANSB5 = 1; } while(0)
#define RB5_SetDigitalMode()        do { ANSELBbits.ANSB5 = 0; } while(0)

// get/set DIG_2 aliases
#define DIG_2_TRIS                 TRISBbits.TRISB6
#define DIG_2_LAT                  LATBbits.LATB6
#define DIG_2_PORT                 PORTBbits.RB6
#define DIG_2_WPU                  WPUBbits.WPUB6
#define DIG_2_OD                   ODCONBbits.ODB6
#define DIG_2_ANS                  ANSELBbits.ANSB6
#define DIG_2_SetHigh()            do { LATBbits.LATB6 = 1; } while(0)
#define DIG_2_SetLow()             do { LATBbits.LATB6 = 0; } while(0)
#define DIG_2_Toggle()             do { LATBbits.LATB6 = ~LATBbits.LATB6; } while(0)
#define DIG_2_GetValue()           PORTBbits.RB6
#define DIG_2_SetDigitalInput()    do { TRISBbits.TRISB6 = 1; } while(0)
#define DIG_2_SetDigitalOutput()   do { TRISBbits.TRISB6 = 0; } while(0)
#define DIG_2_SetPullup()          do { WPUBbits.WPUB6 = 1; } while(0)
#define DIG_2_ResetPullup()        do { WPUBbits.WPUB6 = 0; } while(0)
#define DIG_2_SetPushPull()        do { ODCONBbits.ODB6 = 0; } while(0)
#define DIG_2_SetOpenDrain()       do { ODCONBbits.ODB6 = 1; } while(0)
#define DIG_2_SetAnalogMode()      do { ANSELBbits.ANSB6 = 1; } while(0)
#define DIG_2_SetDigitalMode()     do { ANSELBbits.ANSB6 = 0; } while(0)

// get/set DIG_1 aliases
#define DIG_1_TRIS                 TRISBbits.TRISB7
#define DIG_1_LAT                  LATBbits.LATB7
#define DIG_1_PORT                 PORTBbits.RB7
#define DIG_1_WPU                  WPUBbits.WPUB7
#define DIG_1_OD                   ODCONBbits.ODB7
#define DIG_1_ANS                  ANSELBbits.ANSB7
#define DIG_1_SetHigh()            do { LATBbits.LATB7 = 1; } while(0)
#define DIG_1_SetLow()             do { LATBbits.LATB7 = 0; } while(0)
#define DIG_1_Toggle()             do { LATBbits.LATB7 = ~LATBbits.LATB7; } while(0)
#define DIG_1_GetValue()           PORTBbits.RB7
#define DIG_1_SetDigitalInput()    do { TRISBbits.TRISB7 = 1; } while(0)
#define DIG_1_SetDigitalOutput()   do { TRISBbits.TRISB7 = 0; } while(0)
#define DIG_1_SetPullup()          do { WPUBbits.WPUB7 = 1; } while(0)
#define DIG_1_ResetPullup()        do { WPUBbits.WPUB7 = 0; } while(0)
#define DIG_1_SetPushPull()        do { ODCONBbits.ODB7 = 0; } while(0)
#define DIG_1_SetOpenDrain()       do { ODCONBbits.ODB7 = 1; } while(0)
#define DIG_1_SetAnalogMode()      do { ANSELBbits.ANSB7 = 1; } while(0)
#define DIG_1_SetDigitalMode()     do { ANSELBbits.ANSB7 = 0; } while(0)

// get/set DIG_4 aliases
#define DIG_4_TRIS                 TRISCbits.TRISC1
#define DIG_4_LAT                  LATCbits.LATC1
#define DIG_4_PORT                 PORTCbits.RC1
#define DIG_4_WPU                  WPUCbits.WPUC1
#define DIG_4_OD                   ODCONCbits.ODC1
#define DIG_4_ANS                  ANSELCbits.ANSC1
#define DIG_4_SetHigh()            do { LATCbits.LATC1 = 1; } while(0)
#define DIG_4_SetLow()             do { LATCbits.LATC1 = 0; } while(0)
#define DIG_4_Toggle()             do { LATCbits.LATC1 = ~LATCbits.LATC1; } while(0)
#define DIG_4_GetValue()           PORTCbits.RC1
#define DIG_4_SetDigitalInput()    do { TRISCbits.TRISC1 = 1; } while(0)
#define DIG_4_SetDigitalOutput()   do { TRISCbits.TRISC1 = 0; } while(0)
#define DIG_4_SetPullup()          do { WPUCbits.WPUC1 = 1; } while(0)
#define DIG_4_ResetPullup()        do { WPUCbits.WPUC1 = 0; } while(0)
#define DIG_4_SetPushPull()        do { ODCONCbits.ODC1 = 0; } while(0)
#define DIG_4_SetOpenDrain()       do { ODCONCbits.ODC1 = 1; } while(0)
#define DIG_4_SetAnalogMode()      do { ANSELCbits.ANSC1 = 1; } while(0)
#define DIG_4_SetDigitalMode()     do { ANSELCbits.ANSC1 = 0; } while(0)

// get/set DIG_3 aliases
#define DIG_3_TRIS                 TRISCbits.TRISC2
#define DIG_3_LAT                  LATCbits.LATC2
#define DIG_3_PORT                 PORTCbits.RC2
#define DIG_3_WPU                  WPUCbits.WPUC2
#define DIG_3_OD                   ODCONCbits.ODC2
#define DIG_3_ANS                  ANSELCbits.ANSC2
#define DIG_3_SetHigh()            do { LATCbits.LATC2 = 1; } while(0)
#define DIG_3_SetLow()             do { LATCbits.LATC2 = 0; } while(0)
#define DIG_3_Toggle()             do { LATCbits.LATC2 = ~LATCbits.LATC2; } while(0)
#define DIG_3_GetValue()           PORTCbits.RC2
#define DIG_3_SetDigitalInput()    do { TRISCbits.TRISC2 = 1; } while(0)
#define DIG_3_SetDigitalOutput()   do { TRISCbits.TRISC2 = 0; } while(0)
#define DIG_3_SetPullup()          do { WPUCbits.WPUC2 = 1; } while(0)
#define DIG_3_ResetPullup()        do { WPUCbits.WPUC2 = 0; } while(0)
#define DIG_3_SetPushPull()        do { ODCONCbits.ODC2 = 0; } while(0)
#define DIG_3_SetOpenDrain()       do { ODCONCbits.ODC2 = 1; } while(0)
#define DIG_3_SetAnalogMode()      do { ANSELCbits.ANSC2 = 1; } while(0)
#define DIG_3_SetDigitalMode()     do { ANSELCbits.ANSC2 = 0; } while(0)

// get/set E aliases
#define E_TRIS                 TRISCbits.TRISC3
#define E_LAT                  LATCbits.LATC3
#define E_PORT                 PORTCbits.RC3
#define E_WPU                  WPUCbits.WPUC3
#define E_OD                   ODCONCbits.ODC3
#define E_ANS                  ANSELCbits.ANSC3
#define E_SetHigh()            do { LATCbits.LATC3 = 1; } while(0)
#define E_SetLow()             do { LATCbits.LATC3 = 0; } while(0)
#define E_Toggle()             do { LATCbits.LATC3 = ~LATCbits.LATC3; } while(0)
#define E_GetValue()           PORTCbits.RC3
#define E_SetDigitalInput()    do { TRISCbits.TRISC3 = 1; } while(0)
#define E_SetDigitalOutput()   do { TRISCbits.TRISC3 = 0; } while(0)
#define E_SetPullup()          do { WPUCbits.WPUC3 = 1; } while(0)
#define E_ResetPullup()        do { WPUCbits.WPUC3 = 0; } while(0)
#define E_SetPushPull()        do { ODCONCbits.ODC3 = 0; } while(0)
#define E_SetOpenDrain()       do { ODCONCbits.ODC3 = 1; } while(0)
#define E_SetAnalogMode()      do { ANSELCbits.ANSC3 = 1; } while(0)
#define E_SetDigitalMode()     do { ANSELCbits.ANSC3 = 0; } while(0)

// get/set D aliases
#define D_TRIS                 TRISCbits.TRISC4
#define D_LAT                  LATCbits.LATC4
#define D_PORT                 PORTCbits.RC4
#define D_WPU                  WPUCbits.WPUC4
#define D_OD                   ODCONCbits.ODC4
#define D_SetHigh()            do { LATCbits.LATC4 = 1; } while(0)
#define D_SetLow()             do { LATCbits.LATC4 = 0; } while(0)
#define D_Toggle()             do { LATCbits.LATC4 = ~LATCbits.LATC4; } while(0)
#define D_GetValue()           PORTCbits.RC4
#define D_SetDigitalInput()    do { TRISCbits.TRISC4 = 1; } while(0)
#define D_SetDigitalOutput()   do { TRISCbits.TRISC4 = 0; } while(0)
#define D_SetPullup()          do { WPUCbits.WPUC4 = 1; } while(0)
#define D_ResetPullup()        do { WPUCbits.WPUC4 = 0; } while(0)
#define D_SetPushPull()        do { ODCONCbits.ODC4 = 0; } while(0)
#define D_SetOpenDrain()       do { ODCONCbits.ODC4 = 1; } while(0)

// get/set C aliases
#define C_TRIS                 TRISCbits.TRISC5
#define C_LAT                  LATCbits.LATC5
#define C_PORT                 PORTCbits.RC5
#define C_WPU                  WPUCbits.WPUC5
#define C_OD                   ODCONCbits.ODC5
#define C_SetHigh()            do { LATCbits.LATC5 = 1; } while(0)
#define C_SetLow()             do { LATCbits.LATC5 = 0; } while(0)
#define C_Toggle()             do { LATCbits.LATC5 = ~LATCbits.LATC5; } while(0)
#define C_GetValue()           PORTCbits.RC5
#define C_SetDigitalInput()    do { TRISCbits.TRISC5 = 1; } while(0)
#define C_SetDigitalOutput()   do { TRISCbits.TRISC5 = 0; } while(0)
#define C_SetPullup()          do { WPUCbits.WPUC5 = 1; } while(0)
#define C_ResetPullup()        do { WPUCbits.WPUC5 = 0; } while(0)
#define C_SetPushPull()        do { ODCONCbits.ODC5 = 0; } while(0)
#define C_SetOpenDrain()       do { ODCONCbits.ODC5 = 1; } while(0)

// get/set F aliases
#define F_TRIS                 TRISCbits.TRISC6
#define F_LAT                  LATCbits.LATC6
#define F_PORT                 PORTCbits.RC6
#define F_WPU                  WPUCbits.WPUC6
#define F_OD                   ODCONCbits.ODC6
#define F_ANS                  ANSELCbits.ANSC6
#define F_SetHigh()            do { LATCbits.LATC6 = 1; } while(0)
#define F_SetLow()             do { LATCbits.LATC6 = 0; } while(0)
#define F_Toggle()             do { LATCbits.LATC6 = ~LATCbits.LATC6; } while(0)
#define F_GetValue()           PORTCbits.RC6
#define F_SetDigitalInput()    do { TRISCbits.TRISC6 = 1; } while(0)
#define F_SetDigitalOutput()   do { TRISCbits.TRISC6 = 0; } while(0)
#define F_SetPullup()          do { WPUCbits.WPUC6 = 1; } while(0)
#define F_ResetPullup()        do { WPUCbits.WPUC6 = 0; } while(0)
#define F_SetPushPull()        do { ODCONCbits.ODC6 = 0; } while(0)
#define F_SetOpenDrain()       do { ODCONCbits.ODC6 = 1; } while(0)
#define F_SetAnalogMode()      do { ANSELCbits.ANSC6 = 1; } while(0)
#define F_SetDigitalMode()     do { ANSELCbits.ANSC6 = 0; } while(0)

// get/set G aliases
#define G_TRIS                 TRISCbits.TRISC7
#define G_LAT                  LATCbits.LATC7
#define G_PORT                 PORTCbits.RC7
#define G_WPU                  WPUCbits.WPUC7
#define G_OD                   ODCONCbits.ODC7
#define G_ANS                  ANSELCbits.ANSC7
#define G_SetHigh()            do { LATCbits.LATC7 = 1; } while(0)
#define G_SetLow()             do { LATCbits.LATC7 = 0; } while(0)
#define G_Toggle()             do { LATCbits.LATC7 = ~LATCbits.LATC7; } while(0)
#define G_GetValue()           PORTCbits.RC7
#define G_SetDigitalInput()    do { TRISCbits.TRISC7 = 1; } while(0)
#define G_SetDigitalOutput()   do { TRISCbits.TRISC7 = 0; } while(0)
#define G_SetPullup()          do { WPUCbits.WPUC7 = 1; } while(0)
#define G_ResetPullup()        do { WPUCbits.WPUC7 = 0; } while(0)
#define G_SetPushPull()        do { ODCONCbits.ODC7 = 0; } while(0)
#define G_SetOpenDrain()       do { ODCONCbits.ODC7 = 1; } while(0)
#define G_SetAnalogMode()      do { ANSELCbits.ANSC7 = 1; } while(0)
#define G_SetDigitalMode()     do { ANSELCbits.ANSC7 = 0; } while(0)

/**
   @Param
    none
   @Returns
    none
   @Description
    GPIO and peripheral I/O initialization
   @Example
    PIN_MANAGER_Initialize();
 */
void PIN_MANAGER_Initialize (void);

/**
 * @Param
    none
 * @Returns
    none
 * @Description
    Interrupt on Change Handling routine
 * @Example
    PIN_MANAGER_IOC();
 */
void PIN_MANAGER_IOC(void);



#endif // PIN_MANAGER_H
/**
 End of File
*/