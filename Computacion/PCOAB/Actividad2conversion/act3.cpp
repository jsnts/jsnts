#include <iostream>

using namespace std;

int conversion(int cel){   
    int far = (cel * (9/5)) + 32;
    printf("%d", far, "%d", cel);
    return far;
}

int main()
{
    int veces, cel;
    cout<<"Cuantos valores quieres convertir: "<<endl;
    cin>>veces;
    int i;
    for (i = 1; i <= veces; i++)
        {
            cout<<"Cual es el numero en celsius: "<<endl;
            cin>>cel;
            conversion(cel);
        }
}