#include <iostream> // a file that we gonna use later on

using namespace std;

int main()
{
    // If Statement
    /*if(test){
        code to run;
    }
    */
    int a;
    int b;
    cout << "Enter a number! \n";
    cin >> a;

    cout << "Enter another number! \n";
    cin >> b;

    if(a>b){
        cout << "Your first given number: " << a << " is greater than second number " << b << endl;

    }
    else{
        cout << "Your second given number: " << b << " is greater than first number " << a << endl;
    }


    return 0;
}