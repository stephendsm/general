#include <iostream>
#include <string>

using namespace std;

// Constructor
// is a function that gets called automatically as soon as you create an object
// never have a return type(i.e no need int, void or string..)
// just type the constructor 'name' where the 'name' is always the same as the class name
// But peopele didn't print things out in their constructors
// constructor1.cpp was the wrong way, but see this ..
// The main reason that people make constructors are to give variables an initial value
// this class has a variable 'name', but it might have another variable called 'age', 'height' ..
// So as soon as you create an object from that class, you might want to assign a bunch of values to these variables
// In order to do that, here is what we do ..

class ShalomClass{
public:
    // Creating a constructor
    // Whenever you want ot take a value and assign it to a variable you need to add  parameter in your constructor
    // So lets go ahead and assign a value to this 'name' in constructor(here)
    ShalomClass(string z){
        //passing it in a string to be setting it equal to 'name'
        //we already have a function that does that called 'setName()'
        setName(z);
        //so now later on whenever we want to use our constructor, our constructor can take a parameter as well
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
    //so now later on whenever we want to use our constructor, our constructor can take a parameter as well
    ShalomClass shalomObj("Hey mung, congrats for your first constructor");
    cout << shalomObj.getName() << endl;

    ShalomClass shalomObj2("Hey mung, congrats for your second constructor");
    cout << shalomObj2.getName() << endl;
    return 0;
}

