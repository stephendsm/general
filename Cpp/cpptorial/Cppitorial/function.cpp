#include <iostream>

using namespace std;

//Creating a function

int addingNumbers(int x, int y){
    int ans = x + y;
    return ans;
}

int main() {
    cout << "Hello, Shalom, this is your adding number!" << addingNumbers(23, 2) << endl;
    return 0;
}
