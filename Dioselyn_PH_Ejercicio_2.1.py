# -*- coding: utf-8 -*-


class ColaDePacientes :
    
    def __init__(self):
        self.ColaPacientes=[] 
        
    #Anade elementos a la cola
    def nuevo_paciente(self,pacientes):
         self.ColaPacientes.append(pacientes)
        
    #Devuelve elemento de la cola 
    def proximo_paciente (self):
            print("El primer paciente en la cola es",self.ColaPacientes.pop(0))
            
    def muestra_cola(self):
         print(self.ColaPacientes)
      
       
Cola=ColaDePacientes()    
while True:
 print("1-Agregar nuevo paciente") 
 print("2-Llamar proximo paciente")
 print("3-Mostrar lista de pacientes")
 print("4-Salir")
 op=int(input("opcion:"))
 if op==1:
     p=str(input("Ingrese el nombre del nuevo paciente:")) 
     Cola.nuevo_paciente(p)
 elif op==2:
     print(Cola.proximo_paciente())
 elif op==3:
     print(Cola.muestra_cola())
 elif op==4:
     break
 else :
     print("Instruccion invalida")