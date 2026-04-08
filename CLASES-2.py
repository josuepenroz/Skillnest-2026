class Poleron:
    """"
    Metodo constructor 
    funciones que inicializa el objeto que se va a crear 
    Acá se agregan los atributos

    """
    def __init__(self,color,material,modelo):
        self.color = color
        self.material = material
        self.modelo = modelo
        self.uso = False
        print(f"se ha creado un poleron {self.color} de {self.material} de tipo {self.modelo}")
    def usar(self):
        self.uso = True
        print(f"el poleron {self.color} esta siendo usado" )
    def teñir(self, nuevoColor):
        self.color = nuevoColor
        print(f"El poleron {self.color} se tiño el poleron de color {nuevoColor}")

poleron1 = Poleron("azul","algodon","Con cierre")
poleron2 = Poleron("azul","algodon","Con cierre")
print(poleron1.material)

poleron2.teñir("rojo")

 def __init