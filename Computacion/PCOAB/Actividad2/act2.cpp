#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

using namespace std;

void printRandoms(int lower, int upper, int count, int x)
{
    int i;
    for (i=0; i < count; i++) {
        int num = (rand() %
            (upper - lower +1)) + lower;
        x = num;
    }
}

int main()
{
    int x, y;
    while (x != y);
    cout<<"\nIngresa un numero: "<<endl;
    cin>>y;
    if (y == x){
        cout<<"\nEl numero "<<y<<" que elegiste fue el correcto."<<endl;
    }
    else if (y < x){
        cout<<"El numero que elegiste es menor al correcto, elige otra vez: "<<endl;
        cin>>y;
    }
    else if (y > x){
        cout<<"El numero que elegiste es mayor al correcto, elige otra vez: "<<endl;
        cin>>y;
    }
}
