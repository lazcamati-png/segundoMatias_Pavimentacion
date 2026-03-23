class MaquinariaVial(object):
    def __init__(self,nombre,identificador,peso,estado):
        self.nombre = nombre
        self.identificador = identificador
        self.peso = peso
        self.estado = estado
        
    def __str__(self):
        return self.nombre+" "+str(self.identificador)+" "+str(self.peso)+" "+self.estado
    
    def iniciar():
        print("Iniciando")
        
    def detener():
        print("Deteniendo")
        
    def mostrarInformacion():
        print("Mostrando información")