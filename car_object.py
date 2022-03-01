class Car :

    def __init__(self,model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        """Privated vars """
        self._state = 'Hold'
        self._engine = Engine(cilindros=4)
        self._breakes = True

    def acceleration (self, tipo='slowly'):

        if tipo == 'rapido':
            self._Engine.gasoline_inyection(10)

        else:
            self.Engine.gasoline_inyection(3)

        self._state = 'Moving'

 """    def frenado (self, state, breakes, engine.gasoline_inyection ):

        if engine.gasoline_inyection != 0 :
            self._breakes= False
            self._state= "Moving" """
        

        


class Engine:

    def __init__(self, cilindros, tipo='gasoline'):
        self.cilindros = cilindros
        self.tipo= tipo
        self._temperature = 0

    def gasoline_iyection(self, cantidad):
        pass

        


