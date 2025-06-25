# codigo de el juego piedra papel y tijeras 


import random
def jugar():
   while True
    jugador = input("ingrese (papel, piedra,  tijeras) o ¨salir¨ para dejar de jugar: ").strip().lower()
    if jugador =="salir":
        print("gracias por jugar ")
        break

    elegir= ("papel", "piedra",  "tijeras")
    computadora = random.choice(elegir)
    print(f"tu eliges {jugador}, computador elige,{computadora}")
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

    else:
      print("Entrada no válida. Por favor, elige papel, piedra o tijeras")             
                      
     
             
jugar()
