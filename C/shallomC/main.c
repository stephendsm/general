#include <stdio.h>
#include <stdlib.h>
#include "shalomInfo.h"
//#define MYNAME "shalom"

int main()
{
    //printf("Bucky is awesome!\n"); // \n prints next line
    //printf("Bucky is awesome!\a"); // \a will print a beep
    //printf("%s is the best %s ever\n", "Shalom", "programmer"); // %s is a place holder for string
    //printf("I ate %d corndogs last night", 2); // %d is a place holder for integer
    //printf("Pi is %f\n", 3.1415926535); // %f is a place holder for float. Normally 6 decimal
    //printf("Pi is %.2f\n", 3.1415926535); // btw % and f , you can define the decimal place as you like
    /*
    //Variable (int)

    int age;
    int currentYear;
    int birthYear;

    currentYear = 2020;
    birthYear = 1984;
    age = currentYear-birthYear;

    printf("I am %d years old!", age);
    */

    /*
    //Variable (string)
    char name[17] = "Stephen Hangluah"; // You need I space more to count at the end.
    printf("My name is %s\n", name);

    name[6] = 'z';
    printf("My name is now %s\n", name);

    char pro[] = "Programming C";
    printf("%s the best programming language ever!\n", pro);

    strcpy(pro, "Programming C++");//strcpy(which variable?,your string)
    printf("%s the best programming language ever!\n", pro);
    */

    //printf("My  name is %s\n", MYNAME);

    int girlAge = (AGE / 2) + 7;
    printf("%s can date girls %d or older\n", MYNAME, girlAge);

    return 0;
}
