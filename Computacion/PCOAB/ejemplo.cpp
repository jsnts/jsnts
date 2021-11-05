#include <iostream>

using namespace std;

int calculaSuma(int a, int b)
{
    int suma=a+b;
    return suma;
}
int main()
{
    int x, y;
    cout<<"Entrar con x ="<<endl;
    cin>>x;
    cout<<"Entrar con y ="<<endl;
    cin>>y;
    cout<<"El resultado es = "<<x<<" + "<<y<<calculaSuma(x, y)<<endl;
}