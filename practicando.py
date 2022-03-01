
import numpy as np 


def  suma (a,b):

    sumas= a + b


    print( 'soy suma', sumas)

suma(5,3)

def bucle ():
    valor = int (input())

    for i in range (1,valor+1):

        print(i, 'me repito el numero que digas')


bucle ()


def arrays ():

    a = [1,2,3,4,5,6,7,8,9,10, ' soy un string']

    for i in range (0,len(a) ):
        print ('estoy en la posicion ',i,' y el valor es ',a[i] )

arrays()        