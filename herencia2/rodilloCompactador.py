from herencia1.maquinaria import MaquinariaVial

class RodilloCompactador(MaquinariaVial):
    def __init__(self, nombre, identificador, peso, estado,tipoRodillo):
        super().__init__(nombre, identificador, peso, estado)
        self.tipoRodillo = tipoRodillo
        
    def __str__(self):
         return super().__str__()+" "+ self.tipoRodillo
     
    def compactar(self):
        print("La máquina esta compactando") 
