#include <stdio.h>
#include <stdlib.h>


//prototyping our function
void printSomething();
void convertToDollars(float euro);
int calculateBonus(int yearsWorked);

void passByValue(int i);
void passByAddress(int *i);

int main(){
/*
    printSomething();

    float euroPrice1;
    scanf("%f", &euroPrice1);
    convertToDollars(euroPrice1);

    */

    /*
    int workedYear;
    printf("Enter workedYear!\n");
    scanf("%d", &workedYear);;
    printf("Your bonus is %d", calculateBonus(workedYear));
    */

    int tuna = 20;
    passByValue(tuna);
    printf("Passing by value, tuna is now %d\n", tuna);

    passByAddress(&tuna);
    printf("Passing by address, tuna is now %d\n", tuna);

    return 0;
}

//Basically int main{} is a function which returns 0(i.e OK)
//Besides this, we can creat another function.
//void: we are making a function it's going to do something, we dont want anything or return back
void printSomething(){
    printf("Enter the amount in Euro!\n");

    return;  //every function needs return. Here says we're done with this function, return to the rest of your pprogram
}

//Passing Arguments to Functions
void convertToDollars(float euro){
    float usd = euro * 1.37;
    printf("%.2f Euro = %.2f USD\n", euro, usd);

    return;
}

//Return Values
//Make a function that's going to run some equation and return an integer
//Bonus or extra money that its employees get at the end of year
 int calculateBonus(int yearsWorked){ //Note: we had 'void' function above, but here we wanna have 'int' bcoz we want to get integer as a return
    int bonus = yearsWorked * 250;

    if(yearsWorked > 10){
        bonus += 1000;
    }

    return bonus;//Whenever you return anything other than 'void', you actually can't just write 'return;'
           //You need to write what are you returning
           //We are returning 'bonus' in this case, bcoz that's the main goal of this function
 }

 //Pass by Reference vs Pass by Value
 void passByValue(int i){
    i = 99;

    return;
 }

 void passByAddress(int *i){
    *i = 64;

    return;
 }

