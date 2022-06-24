
#2.Escribir un método reconocimiento, que verifique si hay algún nuevo avión esperando para aterrizar y/o 
#despegar, y de ser así los encole en la cola correspondiente. Para ello, utilizar random.randrange(2).

class TorreDeControl:
    
    def __init__(self):
        self.Por_volar=["AV-03","AV-04"]
        self.En_vuelo=["AV-01","AV-05"]
        self.Por_Aterrrizar=[]
        self.Despegue=[]
        
    def Reconocimiento(self):
        print("El numero de aviones esperando por aterrizar es:",len(self.En_vuelo))
        if len(self.En_vuelo)==0:
            print("No hay aviones esperando por aterrizar")
        elif len(self.En_vuelo) > 0:
            print("Los aviones que se esperan por aterrizar son ")
            print(self.En_vuelo,sep="\n")
            for i in range(0,len(self.En_vuelo),1):
                self.Por_Aterrrizar.append(self.En_vuelo[i])
        print("El numero de aviones por despegar es:",len(self.Por_volar))
        if len(self.Por_volar)==0:
            print("No hay aviones esperando por despegar")
        elif len(self.Por_volar) > 0:
            print("Los aviones que se esperan por despegar son los siguientes")
            print(self.Por_volar,sep="\n")
            for i in range(0,len(self.Por_volar),1):
                self.Despegue.append(self.Por_volar[i])
    def Ingreso(self):
        print(self.Estacionamiento1) 
        
    def mostrar(self):            
        print("Aviones por aterrizar")
        print(self.Por_Aterrrizar,sep=" ")
        print("Aviones que despegan")
        print(self.Despegue,sep=" ")
         
Torre=TorreDeControl()
while True:
 print("1-Verificacion de aviones esperando por aterrizar y/o despegar")
 print("2-Mostrar colas de aterrizajes y despegues")
 print("3-Salir")
 op=int(input("opcion:"))
 if op==1:
     print(Torre.Reconocimiento())
 if op==2:
         print("Las colas de aterrizaje y despegue son las siguientes:")
         print(Torre.mostrar())
 if op==3:
     break