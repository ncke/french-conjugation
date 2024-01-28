from enum import Enum
import random
import sys

# Pronoms.

class Pronom(Enum):
    JE = "je"
    TU = "tu"
    IL = "il"
    ELLE = "elle"
    ON = "on"
    NOUS = "nous"
    VOUS = "vous"
    ILS = "ils"
    ELLES = "elles"

# Temps.

class Temps(Enum):
    PRESENT = "present"

# Regles de Conjugaison.

class RegleConjugaison:

    def getStem(self, infinitif, n):
        return infinitif[:-n]

    def conjuguer(verbe, pronom):
        return "CONJUGAISON"

class RegularPresentER(RegleConjugaison):

    def conjuguer(self, verbe, pronom):
        stem = self.getStem(verbe.infinitif, 2)

        if pronom in [Pronom.JE, pronom.IL, pronom.ELLE, Pronom.ON]:
            return stem + "e"
        
        if pronom == Pronom.TU:
            return stem + "es"

        if pronom == Pronom.NOUS:
            return stem + "ons"
        
        if pronom == Pronom.VOUS:
            return stem + "ez"
        
        if pronom in [Pronom.ILS, Pronom.ELLES]:
            return stem + "ent"
        
        return "PRONOM INCONNU"
    
class EtrePresent(RegleConjugaison):

    def conjuguer(self, verbe, pronom):
        if pronom == Pronom.JE:
            return "suis"
        
        if pronom == Pronom.TU:
            return "es"
        
        if pronom in [Pronom.IL, Pronom.ELLE, Pronom.ON]:
            return "est"

        if pronom == Pronom.NOUS:
            return "sommes"
        
        if pronom == Pronom.VOUS:
            return "êtes"
        
        if pronom in [Pronom.ILS, Pronom.ELLES]:
            return "sont"
        
        return "PRONOM INCONNU"
    
class AvoirPresent(RegleConjugaison):

    def conjuguer(self, verbe, pronom):
        if pronom == Pronom.JE:
            return "ai"
        
        if pronom == Pronom.TU:
            return "as"
        
        if pronom in [Pronom.IL, Pronom.ELLE, Pronom.ON]:
            return "a"

        if pronom == Pronom.NOUS:
            return "avons"
        
        if pronom == Pronom.VOUS:
            return "avez"
        
        if pronom in [Pronom.ILS, Pronom.ELLES]:
            return "ont"
        
        return "PRONOM INCONNU"
    
class PresentCER(RegularPresentER):

    def conjuguer(self, verbe, pronom):
        if pronom == Pronom.NOUS:
            stem = self.getStem(verbe.infinitif, 3)
            return stem + "çons"
        
        return super().conjuguer(verbe, pronom)
    
class PresentGER(RegularPresentER):

    def conjuguer(self, verbe, pronom):
        if pronom == Pronom.NOUS:
            stem = self.getStem(verbe.infinitif, 2)
            return stem + "eons"
        
        return super().conjuguer(verbe, pronom)

class PresentAYER(RegularPresentER):

    def conjuguer(self, verbe, pronom):
        stem = self.getStem(verbe.infinitif, 3) + "i"

        if pronom in [Pronom.JE, pronom.IL, pronom.ELLE, Pronom.ON]:
            return stem + "e"
        
        if pronom == Pronom.TU:
            return stem + "es"

        if pronom == Pronom.NOUS:
            return self.getStem(verbe.infinitif, 2) + "ons"
        
        if pronom == Pronom.VOUS:
            return self.getStem(verbe.infinitif, 2) + "ez"
        
        if pronom in [Pronom.ILS, Pronom.ELLES]:
            return stem + "ent"
        
        return "PRONOM INCONNU"
    
class PresentOYER(PresentAYER):

    def conjuguer(self, verbe, pronom):
        return super().conjuguer(verbe, pronom)
    
class PresentUYER(PresentAYER):

    def conjuguer(self, verbe, pronom):
        return super().conjuguer(verbe, pronom)

# Verbe.

class Verbe:

    def __init__(self, infinitif, anglais, reglePresent):
        self.infinitif = infinitif
        self.anglais = anglais
        self.reglePresent = reglePresent

    def commenceVoyelle(self):
        return self.infinitif[0] in ['a', 'e', 'i', 'o', 'u']

    def obtenirPronom(self, pronom):
        if pronom == Pronom.JE and self.commenceVoyelle():
            return "j'"
        return pronom.value

    def conjuguer(self, temps, pronom):
        if temps == Temps.PRESENT:
            return self.reglePresent.conjuguer(self, pronom)
        
        return "TEMPS INCONNU"

# Liste de verbes.

tres_irregular = [
    Verbe("être", "to be", EtrePresent()),
    Verbe("avoir", "to have", AvoirPresent()),
]

verbes = [
    Verbe("accepter", "to accept", RegularPresentER()),
    Verbe("appuyer", "to press", PresentUYER()),
    Verbe("arranger", "to arrange", PresentGER()),
    Verbe("belayer", "to sweep", PresentAYER()),
    Verbe("charger", "to charge", PresentGER()),
    Verbe("dépenser", "to spend", RegularPresentER()),
    Verbe("donner", "to give", RegularPresentER()),
    Verbe("effacer", "to erase", PresentCER()),
    Verbe("ennuyer", "to bore", PresentUYER()),
    Verbe("essayer", "to try", PresentAYER()),
    Verbe("essuyer", "to wipe", PresentUYER()),
    Verbe("hésiter", "to hesitate", RegularPresentER()),
    Verbe("lancer", "to launch", PresentCER()),
    Verbe("manger", "to eat", PresentGER()),
    Verbe("montre", "to show", RegularPresentER()),
    Verbe("nettoyer", "to clean", PresentOYER()),
    Verbe("partager", "to share", PresentGER()),
    Verbe("payer", "to pay", PresentAYER()),
    Verbe("prononcer", "to pronounce", PresentCER()),
    Verbe("rencontrer", "to meet", RegularPresentER()),
    Verbe("rêver", "to dream", RegularPresentER()),
    Verbe("tomber", "to fall", RegularPresentER()),
    Verbe("tracer", "to draw", PresentCER()),
    Verbe("tutoyer", "to use", PresentOYER()),
    Verbe("vouvoyer", "to use", PresentOYER()),
]

# Jeu.

class Jeu:

    def __init__(self, verbes, temps):
        self.score = 0
        self.attempts = 0
        self.verbes = tres_irregular
        self.temps = temps

    def tempRandom(self):
        return random.choice(self.temps)
    
    def verbeRandom(self):
        return random.choice(self.verbes)
    
    def pronomRandom(self):
        return random.choice([
            Pronom.JE,
            Pronom.TU,
            Pronom.IL,
            Pronom.ELLE,
            Pronom.ON,
            Pronom.NOUS,
            Pronom.VOUS,
            Pronom.ILS,
            Pronom.ELLES
        ])

    def traductionRandom(self):
        t = self.tempRandom()
        v = self.verbeRandom()
        p = self.pronomRandom()
        correct = v.conjuguer(t, p)
        anglais = "(" + v.anglais + ")"
        print(v.infinitif, anglais, "temps:", t.value)
        question = v.obtenirPronom(p)
        if question != "j'":
            question = question + " "
        question = question + "X" * len(correct) + ": "

        answer = input(question)
        if answer == correct:
            print("bonne réponse")
            self.score += 1
        else:
            print("mauvaise réponse, c'est", correct)

        self.attempts += 1
        percent = 100 * self.score / self.attempts
        print(self.score, "/", self.attempts, "(", percent, "% )")
        print()
        
    def joue(self):
        while True:
            self.traductionRandom()

def main() -> int:
    jeu = Jeu(verbes, [Temps.PRESENT])
    jeu.joue()
    return 0

if __name__ == "__main__":
    sys.exit(main())
