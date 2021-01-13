#include <stdio.h>
#include <stdlib.h>

int main(){
    /*
    //Writing Files in C
    FILE * fPointer;
    fPointer = fopen("bacon.txt", "w");

    fprintf(fPointer, "Bacon is good\n"); //If we write eg,"Bacon is good", then the old one "I love cheese" would be delete
                                          //and replace it with "Bacon is good"

    fclose(fPointer);
    */

    /*
    //Read Files in C
    FILE * fPointer;
    fPointer = fopen("bacon.txt", "r");

    //To could read file, we need to store it first (i.e create a variable )
    char singleLine[150];

    //To could read character, line by line
    while(!feof(fPointer)){ // feof=file end of file; which is not equal ends('!') wrt 'fPointer', loop it
        fgets(singleLine, 150, fPointer); //fgets function gets line by line
        puts(singleLine); //the information will store in single line, so just print it out now
                          //sideNote: puts function automatically adds content to a new line every time
    }

    fclose(fPointer);
    */

    /*
    //Append to File
    FILE *fPointer;
    fPointer = fopen("bacon.txt", "a");


    fprintf(fPointer, "\n- a hikewl by Bucky Roberts");

    fclose(fPointer);
    */

    //Random File Access
    //What if we want to change onle little word in the middle of existing file/text
    FILE * fPointer;
    fPointer = fopen("bacon.txt", "w+"); //w=write in a file;+ = after that(w) we can read it afterwards

    fputs("I ate 3 pumpkins today", fPointer);

    fseek(fPointer, 7, SEEK_SET); //fPointer=file; 7=want to start a writting from 7th; SEEK_SET=start from at the beginning
    fputs(" munchkins on Friday", fPointer);

    fseek(fPointer, -6, SEEK_END); //fPointer=file; -6=backward counting 6places SEEK_END=start from at the end
    fputs(" top of a mountain", fPointer);

    fclose(fPointer);

    return 0;
}
