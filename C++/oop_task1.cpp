#include <iostream>
#include <ctime>

/* Create an array of size 6, then fill it with random natural numbers
from 1 to 49 without repetitions (just like in the classic
Lotto numbers game). Find two elements (the smallest and the largest) and
print the following information about them:
1. Value
2. Position in the array
3. Prime number? */


using namespace std;

bool isPrime(int number) {
    if (number < 2) return false;
    for (int i = 2; i * i <= number; i++) {
        if (number % i == 0) return false;
    }
    return true;
}

int main() {
    const int SIZE = 6;
    int lotto[SIZE];
    bool drawn[50] = {false}; 

    srand(time(0)); 

    for (int i = 0; i < SIZE; ) {
        int number = rand() % 49 + 1;
        if (!drawn[number]) {
            lotto[i] = number;
            drawn[number] = true;
            i++;
        }
    }

  
    cout << "Lotto: ";
  
    for (int i = 0; i < SIZE; i++) {
        cout << lotto[i] << " ";
    }
    cout << endl;
  
    int minIndex = 0, maxIndex = 0;
    for (int i = 1; i < SIZE; i++) {
        if (lotto[i] < lotto[minIndex]) minIndex = i;
        if (lotto[i] > lotto[maxIndex]) maxIndex = i;
    }

  
    cout << "\nMinimum:\n";
    cout << "Value: " << lotto[minIndex] << endl;
    cout << "Position: " << minIndex << endl;
    cout << "Is it a prime number?: " << (isPrime(lotto[minIndex]) ? "Yes" : "No") << endl;

    cout << "\nMaximum:\n";
    cout << "Value: " << lotto[maxIndex] << endl;
    cout << "Position: " << maxIndex << endl;
    cout << "Is it a prime number?: " << (isPrime(lotto[maxIndex]) ? "Yes" : "No") << endl;

    return 0;
}

