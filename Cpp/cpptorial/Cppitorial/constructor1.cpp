#include <iostream>
#include <string>

using namespace std;

// Constructor
// is a function that gets called automatically as soon as you create an object
// never have a return type(i.e no need int, void or string..)
// just type the constructor 'name' where the 'name' is always the same as the class name
// But peopele didn't print things out in their constructors 
// This is the wrong way, for example ..

class ShalomClass{
public:
    // Creating a constructor
    ShalomClass(){
        cout << "this will get printed automagically" << endl;
    }
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

    ShalomClass shalomObj;
    return 0;
}
