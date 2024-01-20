/*------Programa prueba para banda------
 este programa pretende ayudar al usuario
 a monitorear los procesos de la misma
 las siguientes son las teclas de acceso
 (d) para girar la banda a la derecha
 (i) para girar la banda a la izquierda
 (p) para detener la banda
 (e) para conocer el estado de los pines de las entradas S1 a S4 y las entradas conectadas a los pines 37, 36, 35 y 34
  
 ----conversión ASCII----
 Simbolo    ASCCI
 p          112
 e          101
 i          105
 d          100
 */

char AsciiCod= 0; // Dato  que es enviado por monitor serial
int ValPin=0; // Estado del pin 0/1

// pines DERECHA, IZQUIERDA 

int der = 22;
int izq = 23;

int digitalPin[]= {30,31,32,33}; // Pines de entrada
  
  int num[]= {1,2,3,4}; // Pines de entrada


void setup (){
    Serial.begin(9600);
    
    pinMode(der, OUTPUT); 
    pinMode(izq, OUTPUT); 
    pinMode(30, INPUT); 
    pinMode(31, INPUT); 
    pinMode(32, INPUT); 
    pinMode(33, INPUT); 
    
    Serial.println("d ---> Hacia Derecha, S1");
    Serial.println("i ---> Hacia,Izquierda S4");
    Serial.println("p ---> Parar proceso");
    Serial.println("e ---> estado actual de las entradas");

}
void loop(){
  
  if (Serial.available()>0)
  {
      AsciiCod = Serial.read();
  }
  if((AsciiCod == 'd') || (AsciiCod == 'i' ))
  {
      MovimientoBanda();
  }
  if(AsciiCod == 'p' )
  {
      PararProceso();      
  }
  if(AsciiCod == 'e')
  {
      for(int thisPin=0; thisPin<=3; thisPin++){
          ValPin= digitalRead(digitalPin[thisPin]);
          Serial.print("Entrada S");
          Serial.print(num[thisPin]);
          Serial.print(" = ");
          Serial.println(ValPin);
      }
      
   AsciiCod=0;
   ValPin=0;
  }
}


void MovimientoBanda()
{
  if(AsciiCod=='d' )
  {
      digitalWrite(der, HIGH);
      Serial.println("Banda girando hacia Derecha, S1");
      digitalWrite(izq, LOW);
      AsciiCod=0;
  }else if (AsciiCod=='i' )
  {
        digitalWrite(izq, HIGH);
        Serial.println("Banda girando hacia Izquierda, S4");
        digitalWrite(der, LOW);
        AsciiCod=0;

  }else{}
 
}
void PararProceso()
{ 

    digitalWrite(der, LOW);
    digitalWrite(izq, LOW);
    Serial.println("Proceso detenido");
    AsciiCod=0;

}






