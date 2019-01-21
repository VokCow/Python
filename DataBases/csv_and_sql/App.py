import pymysql as sq

#  Primero se definen metodos para leer el archivo csv, establecer la conexion con el servidor MySQL y ejecutar comando SQL.

def leerArchivo(rutaArchivo):
    lineas = []
    try:
        file = open(rutaArchivo, "r")
        while True:
            linea = file.readline()
            if not linea:
                break
            lineas.append(linea)
    except:
        lineas = []
    finally:
        if not file.closed:
            file.close()
    return lineas

class Excepcion(Exception):
    # toda excepcion en Python esta compuesta por un metodo constructor __init__ y otro __str__ unicamente
    def __init__(self,message):
        self.message=message
    def __str__(self):
        return str(self.message)

class Conexion(object):
    # constructor
    def __init__(self,host,puerto,usuario,password,database):
        self.cDB,self.host,self.puerto,self.usuario,self.password,self.database=None,host,puerto,usuario,password,database
        if host=="" or puerto==0 or usuario=="" or password=="" or database=="":
            raise Excepcion("Algunos parametros fueron nulos")
    # abrir la conexion
    def open(self):
        self.cDB=sq.connect(host=self.host, port=self.puerto, user=self.usuario, passwd = self.password, db=self.database)

    def comandoSql(self,sql):
        cursor = self.cDB.cursor()
        try:
            cursor.execute(sql)
            self.cDB.commit()
        except Excepcion as e:
            print(str(e))
            self.cDB.rollback()
    def close(self):
        self.cDB.close()

# a continuacion se ejecutan los metodos anteriores

try:
    taxis = Conexion("localhost",3306,"admin","admin","sys")
except Excepcion:
    print("Ha tenido lugar una excepción")

taxis.open()

# por defecto se creara una base de datos nueva cuyo nombre podemos elegir, en la que se guardara la tabla con el contenido del archivo csv

db = input("Type database name: ")
taxis.comandoSql("CREATE DATABASE " + db +";")
taxis.comandoSql("USE " + db +";")

taxis.comandoSql("CREATE TABLE Matriculaciones (Matricula varchar(50), Fecha varchar(20), Marca varchar(50), EuroTaxi varchar(20));")
data = leerArchivo("C:\\Curso2\\TAXI_Flota_Diario.csv")[1:]  # la primera linea es la cabecera que no interesa.
#c=0
for row in data:
    #c+=1
    rrow=row.split(";") #Vamos extrayendo, fila a fila, las columnas, haciendo un split sobre cada fila
    # para construir la query ok hay que poner las comillas antes y despues de cada nombre de columna, ya que debe tener formato string
    sql = "INSERT INTO Matriculaciones VALUES( \"" + rrow[1] + "\" , \"" + rrow[2] + "\" , \"" + rrow[3] + "\" , \"" + \
          rrow[13] + "\" ) " # para ello se usa el caracter de escape \
    taxis.comandoSql(sql)
    #if (c == 10): break

# la variable c permitiria realizar pruebas rapidas ya que detendria el bucle for tras 10 iteraciones

taxis.close()
