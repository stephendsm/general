// In order to use objects from different classes in our 'main.cpp' we need to include the headers

#include <iostream>
#include "burrito.h"

// Now we can use object from that class( class from 'burrito.h')


using namespace std;

int main() {
    burrito bu;

    return 0;
}

// Recap:
// In order to make a new class you go to file, new class
// u name ur class and make sure u check to have the header 'name.h' and implementation file 'name.cpp' in the same directory
// 'name.h' did basically is include the whole class and then we were able to use all the functions, variables and all the stuff from that class
// include the 'name.h' file in 'main.cpp' file
