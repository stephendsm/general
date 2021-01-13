#include <stdio.h>
#include <stdlib.h>

#include <ctype.h>
#include <string.h>
#include <math.h>

int main()
{
    /*
    int tuna = 20;
    printf("%d\n", tuna);
    tuna++; // ++tuna = tuna++
    printf("%d\n", tuna);
    */

    /*
    //++tuna = tuna++ is not the case here now.
    int a = 5, b = 10, answer = 0;
    //add one to a here before run.(i.e wanna get a = 6 now)
    answer = ++a * b;
    printf("The answer is %d \n", answer);

    a = 5, b = 10, answer = 0;
    answer = a++ * b;
    printf("The answer is %d \n", answer);
    */

    //while loops
    /*
    while(test){
        code;
    }
    */

    /*
    int tuna = 1;
    while(tuna < 5){
        printf("I have %d tuna. \n", tuna);
        tuna++;
    }
    */


    /*
    //Do you want a million now or 1 penny but double it amonth?
    int day = 1;
    float amount = .01;

    while(day <= 31){
        printf("Day: %d \t Amount:$ %.2f \n", day, amount);
        amount *= 2;
        day++;
    }
    */

    //do while loops
    //Why we use this, coz this runs at least once
    /*
    do{
        this code;
    }while(this test is true);
    */

    /*
    float grade = 0, scoreEntered = 0, numberOfTests = 0, average = 0;

    printf("Press 0 when completes. \n\n");

    do{
        printf("Tests: %.0f  Average: %.2f  \n", numberOfTests, average);
        printf("\nEnter test score: ");
        scanf("%f", &scoreEntered);
        grade += scoreEntered;
        numberOfTests++;
        average = grade/numberOfTests;
    }while(scoreEntered != 0);
    */

    /*
    //For loop ( is good when you know exactly how many times you want to loop)

    int bacon;

    for (bacon = 0; bacon <= 100; bacon++){
        printf("Bacon is %d \n", bacon);
    }
    */

    /*
    //Making a table
    int column;
    int row;

    for(row = 1; row <= 6; row++){
        for(column = 1; column <= 4; column++){
            printf("%d ", column);
        }
        printf("\n");
    }
    */

    /*
    //Break (Guess a number between 1~100, Once you guess a number 14(the actual number), break it(i.e no needs to loop anymore)

    int counter;
    int howManyTimes;
    int maximum = 10;

    printf("How many times do you want to loop?");
    scanf(" %d", &howManyTimes);

    for(counter = 1; counter<=maximum; counter++){
        printf("%d \n", counter);
        if(counter == howManyTimes){
            break;
        }
    }
    */

    //Continue

    int number = 1;

    do{
        if(number==3 || number==4){
            number++;//whenever number =3 and number=4, number will be add 1(i.e 3+1 and 4+1
            continue;//whatever after continue will ignore it.
            //i.e go right back to the top (after 'number' meets 3(and4) and add 1 respectively)
        }
        printf("%d is available \n", number);
        number++;
    }while(number<=10);

    return 0;

}
