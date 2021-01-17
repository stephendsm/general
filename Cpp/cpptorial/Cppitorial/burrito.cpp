//
// Created by shalom on 16.01.2021.
//

// This cpp file is where we're going to be actually building the functions themselves
// This cpp file is pretty much where all the bodies go

#include "burrito.h"
//why do you have to separate '.h file' in '.cpp' file?
//whenever u gonna give these functions to ur friends to use or maybe u r working on it with a team of programmers or distributing this for sale on the internet
//well u r gonna want to compile this right here and change this all in ones and zeros and where u r going to be giving the other programmers is '.h file'
//the reason u only give them basically the prototypes or the titles of the function is saying alright I already built all these function(.cpp file) and they work perfectly, u dont need to change it
//all u need to do is to use the functions themselves(the constructor 'burrito' in this case)themselves
//so whenever u r distributing this(.cpp file), it is going to get compiled and the programmers are going to have access to ur function ((the constructor 'burrito' in this case)
//but they aren't going to be able to change (.cpp file) the function bodies themselves

//the last thing u need to do is to go to 'main.cpp'

#include <iostream>
#include <string>

using namespace std;

burrito::burrito() // class::constructor (:: is 'binary code resolution operator')
{
    cout << "i am a banana" << endl;
}


