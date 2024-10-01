
from faker import Faker
import pyfiglet
import pyperclip

datos_completo=[]
datos_completo_csv=["Nombre","Apellido","Segundo Apellido"]

vari = Faker('es_ES')

def datos_falsos(): 
    nombre = vari.name()
    apellido = vari.last_name()
    apellido2 = vari.last_name()
    direccion = vari.address()
    edad=vari.random_int(min=18,max=80)

    return nombre, apellido, apellido2, direccion,edad

#x=pandas.Dataframe.from_dict(libros,orient="index")        =    Pandas diccionario

def lenguage():
    texto = input("Tipo de formato de texto : ").lower()
    return texto

#n (next) ejecuta la siguiente lienas de codigo( list and next sirven mucho para experimentar qur bucles esten bien)
#c(continue) ejecuta hasta el proximo punto de interrupcion
#clear limpia todo
#step entra a l la funcion en la linea actual
#quit salir 
#evallua una expresion y muestra su valor
#list entra a la linea de ejecucion, ppr asi decirlo.
#r return termina la ejecucion hasta que termine la funcion.

texto="prueba correct return"
def cantidad_registros():
    count = int(input("Cantidad de registros que quiere : "))
    return count

def tipo(table, count):
    print("Sentencias INSERT generadas:")
    for _ in range(count):
        nombre, apellido, apellido2, direccion,edad = datos_falsos()
        sql_insert = f"INSERT INTO {table} (nombre, apellido, apellido2,edad,direccion) VALUES ('{nombre}','{apellido}','{apellido2}',{edad},'{direccion}');"
        #Tambien es importante añadir el "sql_insert" a lista que tenemos al principio del codigo
        datos_completo.append(sql_insert)
        print(sql_insert)
        # Este es el codigo principal que hace que nuestra terminal se copie toda, o al menos dentro del bucle for. si stopeamos con un "import pdb"  comando:breakpoint()
        # Podremos darnos cuenta se copia en el porta papel uno por uno
        # "datos_completos_limpios = "\n".join(datos_completo)"    Hara mantener los datos, lo puse casi con el mismo nombre, incluso es confuso para mi, pero funciono.
        datos_completos_limpios = "\n".join(datos_completo)
        # "pyperclip.copy(datos_completos_limpios)" Mantendra los datos copiados, exactamente de la lista que tenemos encima, esto hara que se copie uno por uno
        pyperclip.copy(datos_completos_limpios)
        
        
        
def generador_csv(count):
    print(f"Datos CSV Realizados : {count}")
    for _ in range(count+1):
        nombre,apellido,apellido2,direccion,edad = datos_falsos()
        csv= f"{nombre},{apellido},{apellido2},{edad}"
        datos_completo_csv.append(csv)
        print(csv)
        datos_completo_csv_limpios = "\n".join(datos_completo_csv)
        pyperclip.copy(datos_completo_csv_limpios)

if __name__ == "__main__":


    while True:
        ascii_art = pyfiglet.figlet_format("Datos Faker 💻")

        ascii_art2= pyfiglet.figlet_format("Beta",width=100)
        
        print(ascii_art)
        print(ascii_art2)
        
        table = input("Nombre de la tabla : ")
        
        final=lenguage()

        if final in ["posgret", "posgrets", "plp", "plpgsql","post","mysql","sql"]:
            count = cantidad_registros()
            tipo(table, count)
            print("Todo Copiado en el portapapeles exitosomamente")
            continuar = input("¿Desea generar más registros? (s/n): ").lower()
            if continuar != 's':
                break
        elif final in ["csv","cvs"]:
            count=cantidad_registros()
            generador_csv(count)
            print("Todo copia en portapapeles exitosamente")
        else:
            print("No disponible Aun :(")   



#PUEDES VER TU PORTAPAPELES, ALLI SE ENCUENTRAN LOS REGISTROS QUE HICISTES
