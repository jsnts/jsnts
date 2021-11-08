#include <iostream>

using namespace std;

int conversion(int cel){   
    int far = (9.0/5.0) * cel + 32;
    printf("\nFarenheit: %d", far);
    printf("\nCelsius: %d", cel);
    return 0;
}

int main()
{
    int veces, cel;
    cout<<"\nCuantos valores quieres convertir: "<<endl;
    cin>>veces;
    int i;
    for (i = 1; i <= veces; i++)
        {
            cout<<"\nCual es el numero en celsius: "<<endl;
            cin>>cel;
            conversion(cel);
        }
}