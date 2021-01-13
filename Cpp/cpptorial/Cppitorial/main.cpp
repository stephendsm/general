#include <iostream> // a file that we gonna use later on

using namespace std;

void printCrap(int x); //function prototyping

int main()
{
    // Creating Functions That Use Parameters
    //Parameters: additional information that the function needs in order to work
    printCrap(20);
    return 0;
}

void printCrap(int x){ // we need something to print out but we dont specifically know what it is, we use a (parameter)
    cout << "Bucky favourite number is " << x << endl;
}
