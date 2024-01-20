// Reto #1 Cotrol Inalambrico Xbee ---> Programa del Receptor
// Realizado por:
// Jacobo Chica Quintero
// Juan Diego Agudelo Balvin
// Sara Alvarez Bello
// Fecha:
// Agosto 2023


// Librerias:
//#include <TimerOne.h> 

// Declaraciones:

  // Variables
  char fun1 = 0;
  int pos1 = 0;
  int aux1 = 0;
  char ss = 0;
  int fin = 0;
  int segundos = 0;
  
  
  // Sensores
  int s1 = 30;
  int s2 = 31;
  int s3 = 32;
  int s4 = 33;

  // Giro
  int der = 22;
  int izq = 23;

////////////


void setup() {
  
  // Comunicación
  Serial.begin(9600);   // Comunicación Serial con el usuario
  Serial3.begin(9600);  // Comunicación de receptor a emisor

  // Entradas
  pinMode(s1, INPUT);
  pinMode(s2, INPUT);
  pinMode(s3, INPUT);
  pinMode(s4, INPUT);

  // Salidas
  pinMode(der, OUTPUT);
  pinMode(izq, OUTPUT);

  // Interrupcion temporal
  //Timer1.initialize(10000);
  //Timer1.attachInterrupt(reloj);
}




void loop() {

  if (Serial3.available()>0){

    fun1 = Serial3.read();

    if(fun1 == 'z'){
      aux1 = 0;

      while(aux1 == 0){

        Serial.println("Sensando");

        if(digitalRead(s1) == 1){ // Si el sensor 1 esta activo
          aux1 = 1;
        }

        if(digitalRead(s2) == 1){ // Si el sensor 2 esta activo
          aux1 = 2;
        }

        if(digitalRead(s3) == 1){ // Si el sensor 3 esta activo
          aux1 = 3;
        }

        if(digitalRead(s4) == 1){ // Si el sensor 4 esta activo
          aux1 = 4;
        }
      }

      definicion(aux1);
    }

    if(fun1 == '1'){
      fin = 1;

      if(aux1 == 2){

        derecha(aux1, fin, segundos);
      }

      if(aux1 == 3){

        derecha(aux1, fin, segundos);
      }

      if(aux1 == 4){
        
        derecha(aux1, fin, segundos);
      }
    }

    if(fun1 == '2'){
      fin = 2;

      if(aux1 == 1){
      
        izquierda(aux1, fin, segundos);
      }

      if(aux1 == 3){
        
        derecha(aux1, fin, segundos);
      }

      if(aux1 == 4){
       
        derecha(aux1, fin, segundos);
      }
    }

    if(fun1 == '3'){
      fin = 3;

      if(aux1 == 1){
        
        izquierda(aux1, fin, segundos);
      }

      if(aux1 == 2){
        
        izquierda(aux1, fin, segundos);
      }

      if(aux1 == 4){
       
        derecha(aux1, fin, segundos);
      }
    }

    if(fun1 == '4'){
      fin = 4;

      if(aux1 == 1){
        
        izquierda(aux1, fin, segundos);
      }

      if(aux1 == 2){
       
        izquierda(aux1, fin, segundos);
      }

      if(aux1 == 3){
        
        izquierda(aux1, fin, segundos);
      }
    }

    if(fun1 == 'u'){
      segundos = 1000;
    }

    if(fun1 == 'v'){
      segundos = 2000;
    }

    if(fun1 == 'w'){
      segundos = 3000;
    }

    if(fun1 == 'x'){
      segundos = 4000;
    }

    if(fun1 == '5'){
      segundos = 5000;
    }

    if(fun1 == '6'){
      segundos = 6000;
    }

    if(fun1 == '7'){
      segundos = 7000;
    }

    if(fun1 == '8'){
      segundos = 8000;
    }

    if(fun1 == '9'){
      segundos = 9000;
    }

  }

}

////////////

// Funciones;

void definicion(int defi){

    if(defi == 1){
      Serial3.print('j');
  }

    if(defi == 2){
      Serial3.print('q');
  }

    if(defi == 3){
      Serial3.print('k');
  }

    if(defi == 4){
      Serial3.print('m');
  }

}

void izquierda(int si, int sf, int segseg){
  int auxil1 = 0;
  int auxil2 = 0;

  if (sf == 1){
    auxil1 = s1;
  }
  if (sf == 2){
    auxil1 = s2;
  }
  if (sf == 3){
    auxil1 = s3;
  }
  if (sf == 4){
    auxil1 = s4;
  }

    if (si == 1){
    auxil2 = s1;
  }
  if (si == 2){
    auxil2 = s2;
  }
  if (si == 3){
    auxil2 = s3;
  }
  if (si == 4){
    auxil2 = s4;
  }

  digitalWrite(der, LOW);
  digitalWrite(izq, HIGH);
  Serial3.print('l');

  while(digitalRead(auxil1) == 0){
  }
  Serial3.print('o');
  digitalWrite(izq, LOW);
  digitalWrite(der, LOW);
  

  delay(segseg);

 
  digitalWrite(der, HIGH);
  digitalWrite(izq, LOW);
  Serial3.print('d');
  while(digitalRead(auxil2) == LOW){ 
  }
  Serial3.print('o');
  digitalWrite(izq, LOW);
  digitalWrite(der, LOW);

}


void derecha(int si, int sf, int segseg){

  int auxil1 = 0;
  int auxil2 = 0;

  if (sf == 1){
    auxil1 = s1;
  }
  if (sf == 2){
    auxil1 = s2;
  }
  if (sf == 3){
    auxil1 = s3;
  }
  if (sf == 4){
    auxil1 = s4;
  }

    if (si == 1){
    auxil2 = s1;
  }
  if (si == 2){
    auxil2 = s2;
  }
  if (si == 3){
    auxil2 = s3;
  }
  if (si == 4){
    auxil2 = s4;
  }

  digitalWrite(izq, LOW);
  digitalWrite(der, HIGH);
  Serial3.print('d');

  while(digitalRead(auxil1) == 0){
  }
  Serial3.print('o');
  digitalWrite(izq, LOW);
  digitalWrite(der, LOW);


  delay(segseg);


  digitalWrite(izq, HIGH);
  digitalWrite(der, LOW);
  Serial3.print('l');
  while(digitalRead(auxil2) == LOW){ 
  }
  Serial3.print('o');
  digitalWrite(izq, LOW);
  digitalWrite(der, LOW);
}

/*void reloj(){

Serial.println("reloj");  

  if (Serial3.available()>0){
    Serial.println("Se detecto el serial para p");
    int auxil3 = Serial3.read();
    int auxil4 = 0;

    if(auxil3 == 'p'){

      digitalWrite(izq, LOW);
      digitalWrite(der, LOW);

      while(auxil4 == 0){

        if (Serial3.available()>0){

          int auxil5 = Serial3.read();

          if (auxil5 == 'r'){
            auxil4 = 1;
          }
        }

      }

    }
  }

}*/


