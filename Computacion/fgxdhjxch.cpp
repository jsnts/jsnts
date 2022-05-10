#include <iostream>
using namespace std;

class Animal
{
  public: 
  string nombre,especie;
  int edad;

  Animal()
  {

  }

  Animal(string nombre_, string especie_, int edad_)
  {
    setdatos(nombre_,especie_,edad_);
  }

  void setdatos(string nombre_, string especie_, int edad_)

  {

  nombre="";
  especie="";
  edad=0;

  }

  string getnombre()
  {
    return nombre;
  }

  string getespecie()
  {
    return especie;
  }

  int getedad()
  {
    return edad;
  }

  virtual void hablar()
  {
    cout<<"Sonido Animal"<<endl;
  }

};

//___________________

class Perro: public Animal
{
  public:
    string raza, ladrido;

  Perro()
  {

  }
  Perro(string nombre_, string especie_, int edad_,string raza_,string ladrido_)
  {
    setdatos(nombre_,especie_,edad_);
    raza="";
    ladrido="";
  }
  void setdatos(string nombre_, string especie_, int edad_)
  {
    nombre="";
    especie="";
    edad=0;
  }
  void setraza()
  {
    raza="";
  }
  void setladrido()
  {
    ladrido="";
  }
  string getraza()
  {
    return raza;
  }

  string getladrido()
  {
    return ladrido;
  }
  
  void hablar()

  {
    Animal hablar;
    cout<< ladrido <<endl;
  }

  };

//______________

  class Gato: public Animal
{
  public:
    string pelaje, maullido;

  Gato()
  {

  }
  Gato(string nombre_, string especie_, int edad_,string raza_,string ladrido_)
  {
    setdatos(nombre_,especie_,edad_);
    pelaje="";
    maullido="";
  }
  void setdatos(string nombre_, string especie_, int edad_)
  {
    nombre="";
    especie="";
    edad=0;
  }
  void setpelaje()
  {
    pelaje="";
  }
  void setmaullido()
  {
    maullido="";
  }
  string getpelaje()
  {
    return pelaje;
  }

  string getmaullido()
  {
    return maullido;
  }
  
  void hablar()
  
  {
    Animal hablar;
    cout<< maullido <<endl;
  }

  };




  int main(void)
  {
    Perro x("Samuel","pajaro",19,"Yorkie","Woof");
    x.hablar();
    Gato y("Gato","Gato", 13,"Largo", "Miau");
    y.hablar(); 
  }