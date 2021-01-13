#include <stdio.h>
#include <stdlib.h>

int main()
{
    char firstName[20];
    char crush[20];
    int numberOfBabies;

    printf("What is your name? \n");
    scanf("%s", firstName);

    printf("Who are you going to marry? \n");
    scanf("%s", crush);

    printf("How many kids will you have? \n");
    scanf("%s", &numberOfBabies);// needs to use & except array(i.e char)

    printf("%s and %s are in love and will have %d babies \n", firstName, crush, numberOfBabies);
}
