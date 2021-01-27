// C++ assingment 
// 
// Instruction: Print your name 50 times using while and do-while loop.
// Lecturer: Mr. Emma
// Course: CMS 114
// Date: Jan-26-2021
#include <iostream>
using namespace std;

int main() {
    // Printing my name 50 times using while loop.
    string myName = "Wisdom Matthew";
    int count = 1;
    int loop = 50;
    cout << "Using while loop :" << endl << "--------------------------------------------" << endl << endl;
    while (count <= loop)
    {
        cout << myName << endl;
        count++;
    }

    // Printing my name 50 times using do-while loop.
    // setting count to 1 again;
    count = 1;
    cout << endl << "Using do-while loop :" << endl << "--------------------------------------------" << endl << endl;
    do {
        cout << myName << endl;
        count++;
    } while(count <= loop);
    return 0;
}