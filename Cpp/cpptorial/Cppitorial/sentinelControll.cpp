#include <iostream>
using namespace std;

// Sentinel Controlled Program
// If we dont know how many times we gonna loop, we use this technique

int main() {

    int age;
    int totalAge = 0;
    int avgAge;
    int num = 0;

    cout << "Enter persons ages or -1 to quite" << endl;
    cin >> age;

    while( age != -1){
        totalAge += age;
        num++;

        cout << "Enter next persons ages or -1 to quite" << endl;
        cin >> age;

    }
    cout << "Number of people entered is: " << num << endl;
    cout << "Total age is: " << totalAge << endl;
    avgAge = totalAge/num;
    cout << "Average age is: " << avgAge << endl;

    return 0;
}
