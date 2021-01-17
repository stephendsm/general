#include <iostream>

using namespace std;

// Creating Class and Object
// Class is a bunch of similar task function gather together
// Access specifier: You want to make function that you can only use in your class.
// Sometimes you want to make functions that anybody can use outside your class(i.e in main)
// If you want the main to be able to use your function inside your class, u need make ur function 'public'
// If u dont want main to be able to use the function inside ur class, u need to make ur function 'private'
// Objects is how you access the stuff inside of your class
// The object basically tells it what class you're working with
// In order to create an object it's basically the same as creating a variable
// You type the name of your class('ShalomClass' in this case), then you give the object name ('shalomObject' in this case)
// You use this(i.e 'shalomObject') kind of as the key whenever you want to access the crap/body inside your class
class ShalomClass{
public:
    void coolSaying(){
        cout << "prechin to the choir" << endl;
    }
};

int main() {
    ShalomClass shalomObject;
    shalomObject.coolSaying();
    return 0;
}
