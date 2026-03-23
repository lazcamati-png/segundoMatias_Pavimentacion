from herencia1.maquinaria import MaquinariaVial

class Pavimentadora(MaquinariaVial):
    def __init__(self, nombre, identificador, peso, estado,anchoPavimentacion):
        super().__init__(nombre, identificador, peso, estado)
        self.anchoPavimentacion = anchoPavimentacion
        
    def __str__(self):
        return super().__str__()+" "+str(self.anchoPavimentacion)
    
    def pavimentar(self):
        print("La máquina está pavimentando la carretera")
