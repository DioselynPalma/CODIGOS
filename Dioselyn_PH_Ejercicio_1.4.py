
class TorreDeControl:
    
    def __init__(self):
        self.Por_volar=["AV-03","AV-04","AV-02","AV-07"]
        self.En_vuelo=["AV-01","AV-05","AV-08","AV-010"]
        self.Por_Aterrrizar=[]
        
    def Accion(self,n1):
        if n1==1:
            print("El avion que aterrizara es:")
            self.Por_Aterrrizar.append(self.En_vuelo[0])
            print(self.En_vuelo[0])
            self.En_vuelo.remove(self.En_vuelo[0])
                                 
        if n1==2:
            print("El avion por despegar es")
            print(self.Por_volar[0])
            self.En_vuelo.append(self.Por_volar[0])
        
    def __str__(self):
       if len(self.Por_Aterrrizar)==0:
           print("No hay aviones en la cola para aterrizar")
       if len(self.Por_Aterrrizar)>0:
        print("Los Aviones que aterrizaron son:")
        print(self.Por_Aterrrizar,sep=" ")
       if len(self.En_vuelo)==0:
          print("No hay aviones en la cola para despegar")
       if len(self.En_vuelo)>0:
        print("Los Aviones que despegaron son:")
        print(self.Por_volar,sep=" ")
         
Torre=TorreDeControl()
while True:
 print("1-Accion de despegar o aterrizar")
 print("2-Mostrar estado actual colas de aterrizajes y despegues")
 print("3-Salir")
 op=int(input("opcion:"))
 if op==1:
     p=int(input("Teclee 1(aterrizar) o 2(despegar) segun la accion a elegir:"))
     print(Torre.Accion(p))
 if op==2:
         print("Las colas de aterrizaje y despegue son las siguientes:")
         print(Torre.__str__())
 if op==3:
     break