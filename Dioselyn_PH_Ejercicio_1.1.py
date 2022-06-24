
class TorreDeControl:
    
    def __init__(self):
        self.Despegues=["AV-03","AV-04","AV-06","AV-08","AV-010"]
        self.Aterrizajes=["AV-01","AV-05","AV-09","AV-02","AV-07"]
        self.Estacionamiento1=["ES1","ES2","ES3","ES4","ES5","ES6","ES7","ES8"]
        
    def Accion(self,A1):
        self.Despegues.remove(A1)
        self.Aterrizajes.append(A1)
    def Aterrizajes(self,A3):
        self.Aterrizajes.pop(0)
        self.Despegues.append(A3)
    def Reconocimiento(self,R1):
        self.Aterrizajes.append(R1)
    
    def Estacionamiento(self):
        print(self.Estacionamiento1) 
        
    def mostrar(self):            
        print("Aviones por aterrizar")
        print(self.Aterrizajes,sep=" ")
        print("Aviones que despegan")
        print(self.Despegues,sep=" ")
         
Torre=TorreDeControl()     
while True:
 print("1-Asignar estacionamiento para aviones recien llegados") 
 print("2-Ingresar aviones que despegan")
 print("3-Reconocimiento de aviones que despegaron y aterrizaron")
 print("4-Salir")
 op=int(input("opcion:"))
 if op==1:
     print("Estacionamiento disponibles")
     print(Torre.Estacionamiento())
     p=int(input("si quiere ocupar un lugar presione 2, si no presione 1:"))
     if p==2:
         T=str(input("Ingrese el avion que aterrizo:"))
         Torre.Aterrizajes.append(T)
         Torre.Despegues.append(T)
         Lugar=str(input("Ingrese el estacionamiento a asignar:"))
         Torre.Estacionamiento1.remove(Lugar)
     if p==1:
      Des=str(input("Ingrese el estacionamiento a desocupar:"))
      Torre.Estacionamiento1.append(Des)
 elif op==2:
     Des=str(input("Ingrese el avion que despego:"))
     Torre.Accion(Des)
 elif op==3:
     print(Torre.mostrar())
 elif op==4:
     break
 else :
     print("Instruccion invalida")
