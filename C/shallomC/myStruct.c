#include <stdio.h>
#include <stdlib.h>

#include "shalomStructInfo.h"

int main(){

    struct user shalom;
    struct user cing;

    shalom.userID = 1;
    cing.userID = 2;

    puts("Enter the first name of user 1\n");
    gets(shalom.firstName);

    puts("Enter the first name of user 2\n");
    gets(cing.firstName);

    printf("User1 ID is %d\n", shalom.userID );
    printf("User2 firstName is %s\n", cing.firstName);

    return 0;


}
