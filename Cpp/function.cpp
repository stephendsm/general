#include <iostream> // a file that we gonna use later on

using namespace std;

void printSomething(); //function prototyping

int main()
{
    //Function
    printSomething();
    return 0;
}

//creating a function
//a calculation function gonna give back integer number, in that case use 'int function()'
//a function just printing somethin out of the screen, and dont return any answer to you, use 'void function()'

void printSomething(){
    cout << "000 i am text on the screen" << endl;
}
