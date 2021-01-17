#include <iostream>
#include <string>

using namespace std;

// Using variable in Classes (i.e using 'private')
// Not using 'private' is the wrong way like this

class ShalomClass{
public:
    string name;

};

int main() {
    ShalomClass myName;
    myName.name = "Stephen Hangluah";
    cout << myName.name << endl;

    return 0;
}

