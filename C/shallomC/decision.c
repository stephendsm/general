#include <stdio.h>
#include <stdlib.h>

int main()
{
    /*
    int age;
    char gender;

    printf("How old are you? \n");
    scanf("%d", &age);

    if (age >= 18){
        printf(("What is your gender? (m/f) \n"));
        scanf(" %c", &gender); //remember to have space before %c (i.e " %c")

        if (gender == 'm'){
            printf("Hello dude!");
            }
        else
            printf("Hello madam");

        }

    else
        printf("Sorry");
    */

    /*
    float grade1, grade2, grade3, avg;

    printf("Enter your 3 test grades: \n");
    scanf(" %f", &grade1); // remember to have space (i.e " %f")
    scanf(" %f", &grade2);
    scanf(" %f", &grade3);

    avg = (grade1 + grade2 + grade3) / 3;
    printf("Average: %.2f \n", avg);

    if(avg >= 90){
        printf("Grade: A");
        }
    else if(avg >= 80){
        printf("Grade: B");
        }
    else if(avg >= 70){
        printf("Grade: C");
        }
    else if(avg >= 60){
        printf("Grade: D");
        }
    else{
        printf("Grade: E");
        }
    */

    //Test more than one condition
    /*
    int hoursStudied = 60; // per weeks
    int kidsBeatUp = 0 ;

    if ((hoursStudied>=60) && (kidsBeatUp==0)){
        printf("You are a good student! \n");
        }
    */

    /*
    char answer;
    printf("Do you like bacons? (y/n) \n");
    scanf(" %c", &answer); //needs '&' coz 'answer' is one char

    if ((answer == 'y') | (answer == 'n')){
        printf("Good job! \n");
        }
    else{
        printf("You should check typing! \n");
        }
    */

    /*
    //short handed if statement
    char lastName[20];
    printf("Enter your last name: \n");
    scanf(" %s", lastName); // don't need '&' coz 'lastName' is string(i.e not char)

    (lastName[0] < 'M') ? (printf("Blue team \n")) : (printf("Red team \n"));//(statement) ? (trueCode) : (falseCode);
    */

    /*
    //the useful of short handed if statement
    int friends = 7; //I have 0 friends, I have 1 friend, I have 2 friends.

    printf("I have %d friend%s \n", friends, (friends =! 1) ? ("s") : (""));
    */

    return 0;
}
