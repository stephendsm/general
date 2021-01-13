#include <stdio.h>
#include <stdlib.h>

#include <ctype.h>
#include <string.h>
#include <math.h>

int main(){
/*
    int i, temp, swapped;
    int howMany = 10; //10 player
    int goals[howMany];

    for(i=0; i<howMany; i++){
        goals[i] = (rand()%25) + 1;
    }
    //sort it the original
    printf("Original list: \n");
    for(i=0; i<howMany; i++){
        printf("%d \n", goals[i]);
    }

    while(1){
        swapped = 0;
        for(i=0; i<howMany-1; i++){
            if(goals[i] > goals[i+1]){
                int temp = goals[i];
                goals[i] = goals[i+1];
                goals[i+1] = temp;
                swapped = 1;
            }
        }
        if (swapped==0){
            break;
        }
    }
    //sort it in order list
    printf("Sorted list: \n");
    for(i=0; i<howMany; i++){
        printf("%d \n", goals[i]);
    }
    */

    /*
    int tuna = 19;
    //printf("%p \n", &tuna);
    printf("Address \t Name \t Value \n");
    printf("%p \t %s \t %d \n", &tuna, "tuna", tuna);

    //Pointer is a special type of variable that can hold the address(can hold the address of tuna in this case)
    int * pTuna = &tuna;
    printf("%p \t %s \t %d \n", pTuna, "tuna", tuna);

    printf("%p \t %s \t %p \n", &pTuna, "pTuna", pTuna);
    */

    /*
    //dereferance a pointer
    int tuna = 19;
    int * pTuna = &tuna;

    printf("Address \t Name \t Value \n");
    printf("%p \t %s \t %d \n", pTuna,"tuna", tuna);
    printf("%p \t %s \t %p \n", &pTuna,"pTuna", pTuna);

    //So what would be *pTuna?
    printf("\n *pTuna = %d \n", *pTuna); //*pTuna is what we called 'dereferancing' a pointer
                                         //i.e whenever you dereferance a variable(*pTuna-->tuna), (it goes to the variable(tuna) that appoints to)
                                         //and it gets the value of it!
    //now *pTuna = tuna = 19
    //but how about this?
    *pTuna = 79;
    printf("\n *pTuna = %d \n", *pTuna);
    printf("\n tuna = %d \n", tuna);
    //To conclude this: Hey pTuna(i.e (dereferancing) *pTuna, go to the variable 'tuna' and get the value of his)
    //In above case, we go and get the value of 'tuna' (by dereferancing a pointer) to be 79 isf 19.
    */

    /*
    //Arrays and Pointers
    int i;
    int meatBalls[5] = {7, 9, 43, 21, 31};

    printf("Element \t Address \t Value \n");

    for(i=0; i<5; i++){
        printf("meatBalls[%d] \t %p \t %d \n", i, &meatBalls[i], meatBalls[i]);
    }
    //NOTE: If you notice that, just 'meatBalls' is the memory address of the first element(i. meatBall[0] )
    //array names('meatBalls' in this case) are just pointers to the first element
    printf("\nmeatBalls \t\t %p \n", meatBalls);

    //dereference it(automatically at place meatBalls[0]
    printf("\n*meatBalls \t\t %d \n", *meatBalls);

    //dereference it to another place(eg; meatBalls[2] )
    printf("\n*(meatBalls+2) \t\t %d \n", *(meatBalls+2));
    */

    /*
    //Strings and Pointers
    char movie1[] = "The return of Buckyman!"; //movie1 now already acts like a pointer
                                               //where it points to the first elements address, but 'movie1' is a constant(i.e not a variable)
    //We want to change string in 'movie1[]'. Since it is constant and cann't allow to change. So what we gonna do.
    //We needs a pointer of 'movie1[]' (i.e variable til 'movie1[] so that we can change string in movie1[] )
    char * movie2 = "Bucky is awesome I love him!";

    puts(movie2);

    movie2 = "New movie title";

    puts(movie2);

    //Note: Whenever you just make a very simple array of characters(i.e 'char movie1[]' in this case )
    //it's hard to change bcoz that name of the array is a constant (i.e 'char movie1[]' in this case )
    //however whenever you make a pointer to a string (i.e 'char * movie2' in this case), this pointer('movie2') now is a variable (i.e you can change whatever you want).
    //since all this is doing is its storing the address of something, so then we can treat it like a string saying start this address(i.e
    */

    /*
    //Problems with String Lengths
    //We need no longer character (from user) than that has given (eg; 'char movie[20]' i.e movie[given] )
    char movie[20];
    char *pMovie = movie; //we dont need to do like this '&movie' since movie is arry (i.e it already is a pointer of the first elements)

    printf("Give me a movie title! \n");
    fgets(pMovie, 20, stdin); //fgets is basically the same as 'scanf' or 'get' function
    puts(pMovie);
    */

    /*
    //The heap: is the leftover memory that we can borrow whenever we need it and give it back whenever our program ends.
    //So how do we borrow the memory from the heap?
    //malloc: function which gets memory from the heap or allocate memory
    //malloc: function takes the memory (from heap) like how much memory do you need?

    int * points;

    //gets memory from the heap(heap=computer's main memory)
    points = (int *) malloc(5 * sizeof(int)); // 'malloc(5 * sizeof(int))' acts lik a pointer bcoz of '(int *)' standing before it
                                              // sizeof(int) means the size of int(if your computer has 4 bytes, the the size will be 4) multiply with 5
    //give it back to the computer
    free(points); //whenever the program ends, free the memory used back to the computer
    */


    /*
    //Creating an Expandable(utvidbar) Program using the Heap //Expandable=be able to made large or more extensive
    int i, howMany, average;
    int total = 0;
    int * pointsArray;

    pointsArray = (int *) malloc(howMany * sizeof(int));

    printf("How many number do you want in average?\n");
    scanf("%d", &howMany);

    printf("Enter them hoss?");

    for(i=0; i<howMany; i++){
        scanf("%d", &pointsArray[i]);
        total += pointsArray[i];
    }

    average = (float)total/(float)howMany;

    printf("The average is: %d \n", average);
    */

    //Structures
    //Suppose you want to get information of your 500 employee's age,weight. first and last name, ID and so on and so forth.
    //copy and paste each and every 500 .. it would be a suck
    //thinking to use array, but array just can only store the same data type
    //welcom to 'Strucetures': is a way that you can group a bunch of variable types together and the dont need to be the same type
    //Remember: do a 'blueprint' in a seperate 'headerfile'. It would be nicer.

    return 0;
}
