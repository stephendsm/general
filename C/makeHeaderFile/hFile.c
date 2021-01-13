#include <stdio.h>
#include <stdlib.h>

#include "shalomHeader.h"
//#define MYNAME "shalom"

int main()
{
    //printf("My name is %s\n", MYNAME);// This is for #define ..
    int girlAge = (AGE / 2) + 7;
    printf("%s can date girls %d or older\n", MYNAME, girlAge);
    return 0;
}