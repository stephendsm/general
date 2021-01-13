#include <iostream> 

using namespace std;

int main()
{
    int a;  // declearing a variable
    int b;
    int sum;
    //a = 45; // assigning some values to this variable
    //But we want the user to asign a value as he wants
    
    cout << "Enter a number hoss! \n"; // cout takes the information from the computer
    cin >> a; // 'cin' = input stream object; which is giving the information (from the user) to the computer; '>>' = stream exaction extraction operator
    
    cout << "Enter another number hoss! \n";
    cin >> b;

    sum = a + b;
    cout << "The sum of those numbers is " << sum << endl;
    return 0;          
}