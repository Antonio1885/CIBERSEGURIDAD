# codigo de el juego piedra papel y tijeras 

#aqui impotamos una carpeta random para que todo sea de froma aleatoria 
import random

#definimos una jugada 
def jugar():
  #abrimos un bucle para que se ejecute forma infinita hata que el jugador decida salir y tambien definomos un break 
  #para que atravez de un comando solicitat dejar de jugar 
  while True:
    jugador = input("ingrese (papel, piedra,  tijeras) o ¨salir¨ para dejar de jugar: ").strip().lower()
    if jugador =="salir":
        print("gracias por jugar ")
        break
 #aqui le indicamos a la computadora que elija una opcion aleatoria de las indicadas para haci comenzar la jugada
    elegir= ("papel", "piedra",  "tijeras")
    computadora = random.choice(elegir)
    print(f"tu eliges {jugador}, computador elige,{computadora}")
   #aqui definimos las diferentes jugadas y definimos cuando gana el jugador y cuando gana la computadora 
    if jugador == computadora:
     print("empate")

    elif jugador == "piedra":
       if computadora == "tijeras":
          print("ganaste")
        
       else:
            print ("perdiste ") 

    elif jugador == "papel":
        if computadora == " piedra ":          
            print("ganaste")
       
        else:
            print("perdiste ")    

    elif jugador == "tijeras":
         if computadora == "papel":
            print("ganaste")
       
         else:
           print("perdiste")
#en esta ultima linea definimos que si el jugador no ingresa ninguna de las opciones asignadas le pida ingresar 
#una opcion correcta 
    else:
      print("Entrada no válida. Por favor, elige papel, piedra o tijeras")             
                      
     
             
jugar()
