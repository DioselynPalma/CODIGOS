

posicion=0
Paciente=["Roger","Tylor","Isbael"]
Consultorio=[1,2,3]
Union=list(zip(Paciente,Consultorio))
while True:
 print("1-Agregar nuevo paciente") 
 print("2-Ingresar consultorio libre y indicar proximo paciente")
 print("3-Mostrar lista de pacientes")
 print("4-Salir")
 op=int(input("opcion:"))
 if op==1:
     paciente=str(input("Nombre del paciente :"))
     Paciente.append(paciente)
     print(sep="/n")
 elif op==2:
       Consu=int(input("Numero del consultorio liberado:"))
       Consultorio.remove(Consu)
       print("Consultorio ocupados:",Consultorio,"consultorio disponible:",Consu)
       print("El proximo pasiente en espera es:",Paciente.pop(0))
       print(sep="/n")
 elif op==3:
     print(Paciente)
     print(sep="/n")
 elif op==4:
     break
 else :
     print("Instruccion invalida")