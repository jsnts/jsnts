#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int y = 6;

int chooseRandoms(int lower, int upper, int count)
{
    int num = (rand() % (upper - lower +1)) + lower;
    return num;
}

int main()
{
    
    
    int y;
    int num = chooseRandoms(1, 100, 1);
    while (num != y);
        cout<<"\nIngresa un numero: "<<endl;
        cin>>y;
        if (y == num){
            cout<<"\nEl numero "<<y<<" que elegiste fue el correcto."<<endl;
        }
        if (y < num){
            cout<<"El numero que elegiste es menor al correcto, elige otra vez: "<<endl;
            cin>>y;
        }
        if (y > num){
            cout<<"El numero que elegiste es mayor al correcto, elige otra vez: "<<endl;
            cin>>y;
        }
}

