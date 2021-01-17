#include <iostream>
using namespace std;

int main() {
    int num = 1;
    int user_num;
    int total = 0;

    while(num <= 5){
        cout << "Enter the number" << endl;
        cin >> user_num;
        total += user_num;
        num++;
    }

    cout << "Total number is:" << total << endl;

    return 0;
}

