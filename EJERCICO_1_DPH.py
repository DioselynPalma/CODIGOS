

import pandas as pd
datos =        [["Raul",23],
                ["Cristian",24],
                ["Alejandro",29],
                ["Heber",27],
                ["Manuel", 25],
                ["Gerardo", 24],
                ["Jose", 25],
                ["David", 28],
                ["Eliel", 23],
                ["Jacinto",22]]
columnas =['Alumno','Edad']
df = pd.DataFrame(datos,columns=columnas,)
porprom = df.sort_values('Edad',ascending=False)                                                                       
porprom.head()
arx = porprom.iloc[0,:]
print ("La lista ingresada es la siguiente:")
print (df)
print()
print("El alumno con mayor edad es:")
print(arx) 