class Persona ():

    def __init__(self, nombre, edad, profesion):

        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
      

    def saluda (self, otraPersona):

        

        print( 'Hola', otraPersona.nombre, 'me llamo', self.nombre, 'Tengo', self.edad, 'años', 'soy', self.profesion)
        
         


David = Persona ( 'David',  35, 'ingeniero')
Erika = Persona ('Erika', 32, 'diseñadora')

David.saluda(Erika)
Erika.saluda(David)

