#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

using namespace std;

int magic(){
    int count = 0;
    int rando = rand() % 100+1;
    while (true){
        count += 1;
        int guess;
        cout << "Ingresa un numero entre 1 y 100: ";
        cin >> guess;
        if (guess > rando){
            cout << "MENOS" << endl;
        }else if (guess < rando){
            cout << "MAS" <<endl;
        }else if (guess == rando){
            cout << "Lo Lograste!! Le atinaste al numero en "<< count << " intentos" << endl;
            return 0;
        }
        
    }

}

int main(){
    srand((unsigned) time(0));
    int resp = magic();

}