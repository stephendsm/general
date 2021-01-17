#include <iostream>
#include <string>

using namespace std;

// We wanted to access this 'private name' variable
// Well we couldn't access it directly since it's private
// We need to build 'public function' to get this access
// Using variable in Classes (i.e using 'private')
// Not using 'private' is the wrong way
// Making class variable (i.e string 'name' in this case) is generally not good programming practice, easy to mess up
// Make the variable(i.e string 'name' in this case) 'private'
// Making only private without public cant be access
// We need to build a 'public' function inside ur class to have access to those variable inside ur 'public'
// Make public functions to access, we want o add two functions in 'public'
// first thin is set the name, and secondly is get the name, i.e we want to return 'Stephen' 'Tom' ...
class ShalomClass{
public:
    // setting the value of this variable 'name', we need to creat a function/method
    void setName(string x){
        name = x;
    }
    // getting the value of this variable 'name'
    string getName(){
        return name;
    }
private:
    string name;

};

int main() {
    ShalomClass myName;
    //set a value to this
    myName.setName("Sir Shalom");
    //print it out
    cout << myName.getName() << endl;

    return 0;
}
