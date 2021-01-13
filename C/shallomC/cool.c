#include <stdio.h>
#include <stdlib.h>

#include <ctype.h>
#include <string.h>
#include <math.h>

int main(){
/*
    char grade = 'C';
    printf("Enter your grade! (A/B/C/D/F ?) \n");
    scanf(" %c", &grade);

    switch(grade){
        case 'A' : printf("Sweet! \n");
                   break;

        case 'B' : printf("Could have tried harder! \n");
                   break;

        case 'C' : printf("I C you didn't study enough! \n");
                   break;

        case 'D' : printf("You love the D \n");
                   break;

        case 'F' : printf("That is embrassing! \n");
                   break;

        default  : printf("That doesn't make sense! \n");

    }
*/

    /*
    int tuna = '&';

    if( isalpha(tuna) ){ //isalpha() got from ctype.h file
        printf("%c is a letter \n", tuna);
    }
    else{
        if( isdigit(tuna) ){ //isdigit() got from ctype.h file
            printf("%c is a number \n", tuna);
        }else{
            printf("%c is a OMG WTF is that! ? \n", tuna);
        }
    }
    */

    /*
    //Testing UPPERCASE or lowercase
    int tuna;
    printf("Enter password? \n");
    scanf(" %c", &tuna);

    if( isalpha(tuna) ){ //isalpha() got from ctype.h file
        if( isupper(tuna)){
            printf("%c is an upper case letter \n", tuna);
        }else{
            printf("%c is an lower case letter \n", tuna);
        }
    }
    else{
        if( isdigit(tuna) ){ //isdigit() got from ctype.h file
            printf("%c is a number \n", tuna);
        }else{
            printf("%c is a OMG WTF is that! ? \n", tuna);
        }
    }
    */

    /*
    //convert a lowercase letter to uppercase letter or vice versa
    char a = 'a';
    char b = 'F';
    char c = '8';

    printf("%c \n", toupper(a));
    printf("%c \n", toupper(b));
    printf("%c \n", toupper(c));
    */

    /*
    //strcat and strcpy (by using string.h)
    char ham[100] = "Hey ";

    strcat(ham, "Bucky ");
    strcat(ham, "! ");

    printf("%s \n", ham);

    strcpy(ham, "Bucky is cool! ");

    printf("%s \n", ham);
    */


    /*
    //puts and gets
    char myName[50];
    char favouriteFood[50];
    char extra[100] = "";

    puts("What is your name? ");
    gets(myName);

    puts("What is your favourite food");
    gets(favouriteFood);

    strcat(extra, myName);
    strcat(extra, " loves to eat ");
    strcat(extra, favouriteFood);

    puts(extra);
    */

    /*
    //Rounding Numbers(build-in function is math.h)
    float decNum1 = 9.873;
    float decNum2 = 3.45;

    printf("Decimal number 1 round(floor) to %.2f \n", floor(decNum1));
    printf("Decimal number 2 round(floor) to %.2f \n", floor(decNum2));

    printf("Decimal number 1 round(floor) to %.2f \n", ceil(decNum1));
    printf("Decimal number 2 round(floor) to %.2f \n", ceil(decNum2));
    */


    /*
    //Absolute value wtih abs
    int year1;
    int year2;
    int age;

    printf("Enter your birth year! \n");
    scanf(" %d", &year1);

    printf("Enter current year! \n");
    scanf(" %d", &year2);

    age = year1 - year2;
    printf("Your age is %d \n", age);
    printf("Your age is %d \n", abs(age));//absolute gives back positive value

    printf("5 power 3 is %f \n", pow(5,3));

    printf("square roots of 16 is %f \n", sqrt(16));
    */

    /*
    //Random Number Generator with rand
    int diceRoll;
    for(int i = 0; i < 8; i++){
        diceRoll = (rand() % 6) + 1; //rand()%6 gives modulus 0~5, by adding 1 gives 1~6
        printf("%d \n", diceRoll);
    }
    */

    //int and float arrays
    /*
    int i;
    int meatBalls[4] = {7, 9, 43, 21};

    for(i=0;i<4;i++){
        printf("Elements: %d  %d \n", i, meatBalls[i]);
    }
    */

    /*
    int i;
    int meatBalls[5];
    int totalBalls = 0;

    for(i=1; i<=5; i++){
        printf("How many meatBalls did you eat on day %d \n", i);
        scanf(" %d", &meatBalls[i]);
    }

    for(i=1; i<=5; i++){
        totalBalls += meatBalls[i];
    }

    int avg;
    avg = totalBalls/5;

    printf("\n You ate %d meatballs in total, i.e average of %d per day! \n", totalBalls, avg);
    */

    //Why you are banned from fantasy hockey!
    //parallel arrays

    int i;
    int player[5] = {58, 66, 68, 71, 87};
    int goals[5] = {26, 39, 25, 29, 31};
    int gamesPlayed[5] = {30, 30, 28, 30, 26};
    float ppg[5]; //point per game
    float bestPPG = 0.0;
    int bestPlayer;

    for(i=0; i<=5; i++){
        ppg[i] = (float)goals[i] / (float)gamesPlayed[i];
        printf("%d \t %d \t %d \t %.2f \n", player[i], goals[i], gamesPlayed[i], ppg[i]);

        if(ppg[i] > bestPPG){
            bestPPG = ppg[i];
            bestPlayer = player[i];
        }
    }
    printf("\nThe best player is: %d \n", bestPlayer);

    return 0;
}
