clc;
clear;
vo = input("Cual es la velocidad inicial del proyectil: ");
angulog = input("Cual es el angulo de salida: ");

angulor = angulog*pi()/180; %Convertimos el Angulo a radianes
vox = vo*cos(angulor); %Conseguimos las velocidades iniciales en el ejex y en el ejey
voy = vo*sin(angulor);
x0 = 0; %Ponemos el valor de las x0 y y0 iniciales
y0 = 2500; %Altura de un volcan
h = 0.065; %Paso de el tiempo de Euler

g = 9.8; %Gravedad
sigma = input("Cual es el coeficiente ß de su proyectil: ");
D = input("Cual es el diametro de su proyectil: ");
m = 0.15; %Masa del proyectil
b = sigma/D;
t = 0:h:60; %Tiempo con a ritmo del paso antes usado
vx = zeros(size(t)); %Esto crea un vector que tenga todos los valores de velocidadx velocidady, al igual que sus posiciónes
vy = zeros(size(t));
x = zeros(size(t));
y = zeros(size(t));
vx(1) = vox; % Esto hace que el primer valor de estos vectores sean las posiciones iniciales
vy(1) = voy;
x(1) = x0;
y(1) = y0;

for i = 1:length(vx) %Esto consige la velocidad en x con el metodo de euler
    vx(i+1)= vx(i)+h*((-b/m)*vx(i));
end

for i = 1:length(vy)
     %Esto consigue la velocidad en y con el metodo de euler
    vy(i+1)= vy(i)+h*((-b/m)*vy(i)-g);
end

for i = 1:length(x) % Esto consigue la posición en x con el metodo de euelr
    
    x(i+1)= x(i)+vx(i)*h;
end

for i = 1:length(y) % Esto consigue la posición en y con el metodo de euler
    
    y(i+1)= y(i)+vy(i)*h;
end



for i=1:size(x,2) %Esto hace la gráfica
    if(i>1 && y(i)<=0)
        break;
    end
    plot(x(i),y(i),'bo','MarkerSize',3);
    xlabel({'Velocidad en x',vx(i),'Posicion en x',x(i)}) % Esto despliega los valores actuales de la velocidad y distancias en ambos ejes
    ylabel({'Velocidad en y',vy(i),'Posicion en y',y(i)})
    hold on; 
    pause(0.02);
    axis([-2500 2500 y0-2500 y0+600]);
    img = imread('volcan2.jpg');%Creamos un objeto de tipo imagen
    image('CData',img,'XData',[-500 500],'YData',[0 y0]);%Definimos la posicion de la imagen

    tx = text(0,y0*2-20,"Posicion x: "); 
    ty = text(0,y0*2-120,"Posicion y: ");
    tvx = text(0,y0*2-220,"Velocidad x: ");
    tvy = text(0,y0*2-320,"Velocidad y: ");

end


disp("Los Parametros que se usaron fueron:")
fprintf("Angulo: %i\nVelocidad Inicial en x e y: (%fm/s, %fm/s)\nPosición inicial en (x,y): (%i, %i)", angulog,vox, voy, x0, y0)
fprintf("\nTamaño del paso usado para Euler: %f\n gravedad: 9.8\n Coeficiente ß: %f\nDiametro: %f",h, sigma, D)
fprintf("\nMasa: %f\nconstant b = %f\n",m, b)
