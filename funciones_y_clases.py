
global1 = 34

def cambiar_global(g):
    '''Cambiar una variable global

    Esta función debe asignarle a la variable global `global1` el valor que se
    le pasa como único argumento posicional.
    '''
    global global1
    global1=g
    return g
cambiar_global(99)
#print (global1)

def anio_bisiesto(yy):
    '''Responder si el entero pasado como argumento es un año bisiesto
    
    Para determinar si un año es bisiesto, se deben tener en cuenta las 
    siguientes condiciones:

    - Si el año es divisible por 4 es bisiesto, a menos que:
        - Si el año es divisible por 100 no es bisiesto a menos que:
            - Si el año es divisible por 400 es bisiesto.

    Retorna True o False
    '''

    
     
     
    if yy%4==0 and yy%100 !=0 :
        return True
        print('anio si es biciesto')

    elif yy%400==0: 
        return True
        print('anio si es biciesto:', yy)

    else:
        return False
        print('el anio no es biciesto') 
       
aa= anio_bisiesto(2000)
#print (aa)









def contar_valles():
    r'''Contar el número de valles

    Esta función debe recibir como argumento una lista de -1's, 0's y 1's, y lo 
    que representan son las subidas y las bajadas en una ruta de caminata. -1
    representa un paso hacia abajo, el 0 representa un paso hacia adelante y el 
    1 representa un paso hacia arriba, entonces por ejemplo, para la lista
    [-1,1,0,1,1,-1,0,0,1,-1,1,1,-1,-1] representa la siguiente ruta:

                /\
         /\__/\/  \
       _/  
     \/

    El objetivo de esta función es devolver el número de valles que estén 
    representados en la lista, que para el ejemplo que se acaba de mostrar es
    de 3 valles.
    '''

listac=[1,-1,0,1,0,1,1,1]

def contar_valles(listaR):
   #print('lista dentro', listaR)
   cuentaAbajo=0#-1s
   cuentaAdelante=0 #0s
   cuentaArriba=0 #1
   for x in range(len(listaR)):
        #print(listaR[x])
        if listaR[x]==-1   :
          cuentaAbajo=cuentaAbajo+1
        #return cuentaLomas
         #print(cuentaLomas)
        elif listaR[x]==0:
          cuentaAdelante=cuentaAdelante+1
        #return cuentaA
        # print(cuentaA)
        elif listaR[x]==1:  
          cuentaArriba=cuentaArriba+1 
   return cuentaAdelante
   #print('prueba cuenta valles', cuentaValles)

    #pass
cuentaV=contar_valles(listac)
print('cantidad de valles:', cuentaV )


listaRocas=[0,1,1,0,1,0,1,1,0,1,0,0]

def saltando_rocas(listaRoca):

    '''Mínimo número de saltos en las rocas

    Esta función hace parte de un juego en el que el jugador debe cruzar un río
    saltando de roca en roca hasta llegar al otro lado. Hay dos tipo de rocas, 
    secas y húmedas, y el jugador debe evitar saltar encima de las húmedas para 
    no resbalarse y caer. Además el jugador puede saltar 1 o 2 rocas, siempre y 
    cuando no caiga en una húmeda.

    Esta función debe recibir como argumento una lista de ceros y unos. Los ceros 
    representan las rocas secas y los unos las húmedas.
    El objetivo es devolver el número mínimo de saltos que debe realizar el 
    jugador para ganar la partida
    '''


 #saltos=0
 #   print('lista rocas', listaRoca)
    for x in range(len(listaRoca)):
        if listaRoca[x]==0:#seca
           saltos =saltos+1
           if listaRoca[x+1]==1:#humeda
              saltos=saltos=saltos+2
           #return saltos
           print(saltos)
        elif listaRoca[x]==1:#humeda
            saltos=saltos=saltos+2
          #  if listaRoca[x+2]==1
            #return saltos
           # print(saltos)
    return saltos
    print('prueba cuenta saltos:', saltos)

#minSaltos=saltando_rocas(listaRocas)    
#print('prueba cuenta saltos:', minSaltos)

listaMedias=[3,1,1,9,1,4,8,1,8,88,10,10]

def pares_medias(listaMedia):
    '''Contar pares de medias

    Esta función debe recibir como argumento una lista de enteros. Cada elemento
    de esta lista representa el color de una media, y por lo tanto si hay dos 
    elementos que tienen el mismo entero, esas dos medias tienen el mismo color.
    El objetivo de esta función es devolver un diccionario cuyas keys son cada 
    uno de los colores que se encuentren en la lista, y los valores son la 
    cantidad de pares que se han encontrado para cada color.
    '''
    #dic={}
    #pares=0
    #i=1
    #listaMedia=sorted(listaMedia)
    #print (listaMedia)

    #for x in range(len(listaMedia)):
      #mediantes=listaMedia[x+1]
     # if listaMedia[x]==dic[x]:
    #    pares=pares+1
   #   i=i+1
  #    dic[x]=listaMedia[x]

 #   return dic 

#CantidadPares= pares_medias(listaMedias)
#print('cantidad de pares:', CantidadPares)


class Person:
    name = ''
    school = ''
     
    def print_name(self):
        print (self.name)
         
    def print_school(self):
        print (self.school)
     
jorge = Person()
jorge.name = 'Jorge'
jorge.school = 'Universidad de la vida'
jorge.print_name()
jorge.print_school()

# Crear una clase llamada `ListaComa` que reciba en su constructor un iterable
# con el valor inicial para una lista que se guardará en un atributo llamado 
# `lista`. Implementar el método __str__ para que devuelva un string con todos
# los elementos del atributo `lista` unidos a través de comas. Ejemplo:
# si `lista` es [1,2,3,4], __str__ debe devolver '1,2,3,4'

listaData=[1,2,3,4,5]

class ListaComa:
  #lista=[]
  
    def __init__ (self, lista):
          self.lista=lista
          print ('la lista q le envie:',lista)
      #for x in range(len(lista)):
        #listaU = self.lista
        #listaUnida=lista[x]+listaUnida[x]
           #print(lista[x])
      #return listaUnida
    def __str__(self):
        listaUnida = ''
        for x in range(len(self.lista)):
            print('haber que pasa', self.lista)
            listaUnida=  listaUnida +str(self.lista[x])
        listaUnida=','.join(listaUnida)
        print(listaUnida)
        return listaUnida

lista1 = ListaComa(listaData)
#lista1.lista=listaData
#listaObjeto=lista1(listaData)
print('esta es mi lista despues de pasar por la clase:', lista1)


        #nombresCadena = self.nombres+self.apellidos
        #nombresCadena=' '.join(nombresCadena)



    

# Crear una clase llamada `Persona` que reciba en su constructor como 1er 
# argumento un iterable con el valor inicial para una lista que se guardará en
# un atributo llamado `nombres` y como 2do argumento un iterable con el valor 
# inicial para una lista que se guardará en un atributo llamado `apellidos`.
# Antes de guardar estos atributos se debe verificar que todos los elementos 
# de estas dos listas deben ser de tipo str y procesar todos los elementos de
# cada una de las dos listas para que su primera letra sea mayúscula y las demás
# minúsculas.
#
# Implementar el método `nombre_completo` para que devuelva un string con todos 
# los elementos de `nombres` concatenados con espacio, y esto a su vez 
# concatenado con todos los elementos de `appelidos` concatenados con espacio.
# Ejemplo:
# si `nombres` es ['Juan', 'David'] y `apellidos` es ['Torres', 'Salazar'],
# el método `nombre completo` debe devolver  'Juan David Torres Salazar'



ListaApellidos=['quintero', 'maldonado']
ListaNombres=['danilo', 'helver']

class Persona:
    lista=[]
  
   # print(isinstance(self.apellidos,str))
      #if self.nombres[x]=str
    def __init__ (self, nombres, apellidos):
        self.nombres=[]
        for x in range(len(nombres)):
                     if isinstance(nombres[x],str)==True :
                        
                         #self.nombres.capitalize()
                        self.nombres.append(nombres[x].capitalize())
                        #nombres=nombres[x].capitalize()+str(nombres)
                        #print('nombre en el for',nombres)
        #print('despues del for',nombres)
        #print('apellidos antes del for',apellidos) 
        
        for x in range(len(apellidos)):
                     if isinstance(apellidos[x],str)==True :
                        self.apellidos=apellidos
                        apellidos[x]=apellidos[x].capitalize()
                        #apellidosS=apellidos[x].capitalize()+' , '+str(apellidosS)
                        #print('apellido en el for',apellidos)

    def nombre_completo (self):
        nombresCadena=[]
        nombresCadena = self.nombres+self.apellidos
        nombresCadena=' '.join(nombresCadena)

        print('nomsbres completos', nombresCadena)
        return str(nombresCadena)







apellidosAntes = Persona(ListaNombres, ListaApellidos )
print('prueba objeto metodo2', apellidosAntes.nombre_completo())




# Crear una clase llamada `Persona1` que herede de la clase `Persona`, y que en su
# constructor reciba además de los atributos del padre, una variable tipo 
# `datetime` como 3er argumento para guardar en atributo `fecha_nacimiento`.
#



import datetime
from datetime import date
#from datetime import datetime

mifecha=datetime.datetime(1984, 9, 23)
class Persona1(Persona):
    def __init__ (self, nombres, apellidos, fecha_nacimiento):
        
        
        self.fecha_nacimiento = fecha_nacimiento
        super().__init__(nombres, apellidos)

        print('fecha nacimeinto antes de metodo edad', fecha_nacimiento)

    def edad (self):
        
#Día actual
        print('dentro de la clase', self.fecha_nacimiento)
        yy=self.fecha_nacimiento
        yearM=yy.year
        print('yearMMMM', yearM)
        #self.fecha_nacimiento=fecha_nacimiento
        today = date.today()
        print('hoy',today)
        year = today.year
        print('year', year)
        print(self.fecha_nacimiento)
        
#Fecha actual
        #now = datetime.now()
        #print('now', now)
        CalculoEdad = year-yearM
        print('calse calculando edad', CalculoEdad)
        
        return CalculoEdad

print('mifecha antes de nada', mifecha)
cumple=Persona1(ListaNombres, ListaApellidos, mifecha)
#cumple=Persona1.__init__(ListaNombres, ListaApellidos, mifecha)
print('mi cumple:', cumple.edad())


# Implementar el método `edad` para que devuelva un `int` que represente la edad
# de la persona y que se calcule restando los años entre la fecha actual y 
# el atributo `fecha_nacimiento`.
# Ejemplo:
# si `fecha_nacimiento` es 1985-10-21 y la fecha actual es 2020-10-20, el método
# `edad` debe devover 35.

