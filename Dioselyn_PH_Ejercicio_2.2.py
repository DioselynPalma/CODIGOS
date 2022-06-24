

class Recepcion :
    
    def __init__(self):
        self.patient=["Ana","Diego","Ivan"]
        self.medic=["Dr.Rojas","Dr.Medina","Dr.Luis"]
        
    def nuevos_pacientes(self,pacientes,especialista):
         self.patient.append(pacientes)
         self.medic.append(especialista)
    #Devuelve elemento de la cola 
    def proximo_paciente (self,pacientes):
        if pacientes==self.patient[0]:
              print("El paciente liberad@ es",self.patient.pop(0))
              self.medic.pop(0)
              return print("El proximo paciente es",self.patient[0])
              self.medic.pop(0)
        if len(self.patient) < 1:
              print("")
    def muestra_cola(self):
         print(list(zip(self.patient,self.medic)))
         
Recepcion=Recepcion()
while True:
 print("1-Agregar nuevo paciente") 
 print("2-Ingresar persona liberada y Llamar proximo paciente")
 print("3-Mostrar lista de pacientes y doctor@s")
 print("4-Salir")
 op=int(input("opcion:"))
 if op==1:
     paciente=str(input("Nombre del paciente:"))
     especialista=str(input("Nombre del Especialista:"))
     Recepcion.nuevos_pacientes(paciente,especialista)
 elif op==2:
     pacientefree=str(input("Nombre del paciente liberado:"))
     Recepcion.proximo_paciente(pacientefree)
 elif op==3:
     print(Recepcion.muestra_cola())
 elif op==4:
     break
 else :
     print("Instruccion invalida")
