class Voto:
    def __init__(self, voto, materia):
        self.voto = voto
        self.materia = materia
    
    @staticmethod
    def caricaVoti(nomeFile):
        voti = []

        file = open(nomeFile, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            voto = line.split(",")
            voti.append(Voto(int(voto[0]), voto[1]))

        return voti

class Studente:
    
    def __init__(self,nome,classe,voti):
        self.nome = nome
        self.classe = classe
        self.voti = voti
        
    def media(self):
        somma = 0
        
        for voto in self.voti: somma += voto.voto
            
        return somma / len(self.voti)
        
    @staticmethod
    def checkVoti(voti):
        return len(voti) == 9

    
        
   
voti = Voto.caricaVoti("voti.txt")

print(Studente.checkVoti(voti))

studente = Studente("mario", "5 F", voti)

print(studente.media())
