// Reto #1 Cotrol Inalambrico Xbee ---> Programa del emisor
// Realizado por:
// Jacobo Chica Quintero
// Juan Diego Agudelo Balvin
// Sara Alvarez Bello
// Fecha:
// Agosto 2023


// Librerias:

// Declaraciones:

  // Variables
  char fun = 0; // Orden del usuario 
  int pos = 0; // Posicion inicial de la pieza
  char fun_pos = 0; // // Funcion de la funcion posicion
  int aux_pos = 0; // Auxiliar de la funcion posicion
  
  
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

/*
  // Entradas
  pinMode(s1, INPUT);
  pinMode(s2, INPUT);
  pinMode(s3, INPUT);
  pinMode(s4, INPUT);

  // Salidas
  pinMode(der, OUTPUT);
  pinMode(izq, OUTPUT);

  */

  Serial.println("Control de la banda");
  Serial.println("Para comenzar con el programa ubique la pieza en uno de los sensores");
  Serial.println("Despues envie el caracter (c) en el monitor para comenzar");
  Serial.println(" ");
  Serial.println("Estas son las funciones que usted puede utilizar para controlar la planta: ");
  Serial.println(" ");
  Serial.println("c ---> Comenzar el programa");
  Serial.println("1 ---> Llevar la pieza al sensor 1");
  Serial.println("2 ---> Llevar la pieza al sensor 2");
  Serial.println("3 ---> Llevar la pieza al sensor 3");
  Serial.println("4 ---> Llevar la pieza al sensor 4");
  Serial.println("p ---> Pausar el proceso");
  Serial.println("r ---> Reanudar el proceso");
  
}


/////////////

void loop() {

  // fun = 0; //No creo que sea necesario

  if (Serial.available()>0){
    
    fun = Serial.read();

    if (fun == 'c'){ // Iniciar
      Serial.println("Iniciando");
      pos = posicion();
    }


    if (fun == '1'){
      if (pos == 1){
      Serial.println("La pieza se encuentra en el sensor 1, seleccione otro sensor");
      }

      if (pos == 2){
        segundos();
        mover(fun);
        
      }

      if (pos == 3){
        segundos();
        mover(fun);
        
      }

      if (pos == 4){
        segundos();
        mover(fun);
        
      }
    }


    if (fun == '2'){
      if (pos == 2){
      Serial.println("La pieza se encuentra en el sensor 2, seleccione otro sensor");
      }

      if (pos == 1){
        segundos();
        mover(fun);
    
      }

      if (pos == 3){
        segundos();
        mover(fun);
      }

      if (pos == 4){
        segundos();
        mover(fun);
        
      }
    }


    if (fun == '3'){
      if (pos == 3){
      Serial.println("La pieza se encuentra en el sensor 3, seleccione otro sensor");
      }

      if (pos == 1){
        segundos();
        mover(fun);
        
      }

      if (pos == 2){
        segundos();
        mover(fun);
        
      }

      if (pos == 4){
        segundos();
        mover(fun);
        
      }
    }
    

    if (fun == '4'){
      if (pos == 4){
      Serial.println("La pieza se encuentra en el sensor 4, seleccione otro sensor");
      }

      if (pos == 1){
        segundos();
        mover(fun);

      }

      if (pos == 2){
        segundos();
        mover(fun);

      }

      if (pos == 3){
        segundos();
        mover(fun);

      }
    }
    
    

    if (fun == 'p'){
      Serial2.print('p');
    }

    if (fun == 'r'){

      Serial2.print('r');
    }
  
  }


  if (Serial3.available()>0){
    char funaux1 = Serial3.read();

    if (funaux1 == 'd'){
      analogWrite(2,0);
      analogWrite(3,0);
      analogWrite(4,255);
    }

    if (funaux1 == 'o'){
      analogWrite(2,0);
      analogWrite(3,0);
      analogWrite(4,0);
    }

    if (funaux1 == 'l'){
      analogWrite(2,255);
      analogWrite(3,0);
      analogWrite(4,0);
    }
  }
  
}

////////////

// Funciones;

int posicion(){ // Funcion posicion

  aux_pos = 0;
  Serial3.print('z');

  while(aux_pos == 0){

    fun_pos = Serial3.read();

    if(fun_pos == 'j'){

      Serial.println("Pieza en el sensor 1");
      aux_pos = 1;
      Serial.println("¿A cual sensor se dirige?");
    }

    if(fun_pos == 'q'){

      Serial.println("Pieza en el sensor 2");
      aux_pos = 2;
      Serial.println("¿A cual sensor se dirige?");
    }

    if(fun_pos == 'k'){

      Serial.println("Pieza en el sensor 3");
      aux_pos = 3;
      Serial.println("¿A cual sensor se dirige?");
    }

    if(fun_pos == 'm'){

      Serial.println("Pieza en el sensor 4");
      aux_pos = 4;
      Serial.println("¿A cual sensor se dirige?");
    }

  }

  return(aux_pos);
}

void mover(char sd){ // Mover a la izquierda hasta el sensor destino (sd)

  if(sd == '1'){
    Serial3.print(sd);
  }

  if(sd == '2'){
    Serial3.print(sd);
  }

  if(sd == '3'){
    Serial3.print(sd);
  }

  if(sd == '4'){
    Serial3.print(sd);
  }

}

void segundos(){
  Serial.println("¿Cuantos segundos se va a quedar la pieza en este sensor?");
  Serial.println("Escriba un numero del 1 al 9");
  int segu = 0;
  char aux4 = 0;
  while(segu == 0){

    
    if (Serial.available()>0){
      aux4 = Serial.read();

      if(aux4 == '1'){
        Serial3.print('u');
        segu = 1;
      }

      if(aux4 == '2'){
        Serial3.print('v');
        segu = 2;
      }

      if(aux4 == '3'){
        Serial3.print('w');
        segu = 3;
      }

      if(aux4 == '4'){
        Serial3.print('x');
        segu = 4;
      }

      if(aux4 == '5'){
        Serial3.print(aux4);
        segu = 5;
        Serial.println("Se envio 5 seg");
      }

      if(aux4 == '6'){
        Serial3.print(aux4);
        segu = 6;
      }

      if(aux4 == '7'){
        Serial3.print(aux4);
        segu = 7;
      }

      if(aux4 == '8'){
        Serial3.print(aux4);
        segu = 8;
      }

      if(aux4 == '9'){
        Serial3.print(aux4);
        segu = 9;
      }
    }
  }
}
