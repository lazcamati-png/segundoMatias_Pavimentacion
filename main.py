from herencia2.pavimentadora import Pavimentadora
from herencia2.rodilloCompactador import RodilloCompactador

def main():
    pv = Pavimentadora("Maquinaria:Pavimentadora","ID:MV001","1500 kg","Activa","3.5 m ")
    print(pv)
    pv.pavimentar()
    
    rc = RodilloCompactador("Maquinaria:Rodillo Compactador", "ID:MV002","Peso:1367 kg", "Estado: Activa","Tipo de rodillo: Vibratorio")
    print(rc)
    rc.compactar()
    
if __name__ == "__main__":
    main()
    