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

class RegularPresentIR(RegleConjugaison):
    def conjuguer(self, verbe, pronom):
        stem = self.getStem(verbe.infinitif, 2)
        if pronom in [Pronom.JE, pronom.TU]:
            return stem + "is"
        if pronom in [Pronom.IL, Pronom.ELLE, Pronom.ON]:
            return stem + "it"
        if pronom == Pronom.NOUS:
            return stem + "issons"
        if pronom == Pronom.VOUS:
            return stem + "issez"
        if pronom in [Pronom.ILS, Pronom.ELLES]:
            return stem + "issent"
        return "PRONOM INCONNU"

class RegularPresentRE(RegleConjugaison):
    def conjuguer(self, verbe, pronom):
        stem = self.getStem(verbe.infinitif, 2)
        if pronom in [Pronom.JE, pronom.TU]:
            return stem + "s"
        if pronom in [Pronom.IL, Pronom.ELLE, Pronom.ON]:
            return stem
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
    
class AllerPresent(RegleConjugaison):
    def conjuguer(self, verbe, pronom):
        if pronom == Pronom.JE:
            return "vais"
        if pronom == Pronom.TU:
            return "vas"
        if pronom in [Pronom.IL, Pronom.ELLE, Pronom.ON]:
            return "va"
        if pronom == Pronom.NOUS:
            return "allons"
        if pronom == Pronom.VOUS:
            return "allez"
        if pronom in [Pronom.ILS, Pronom.ELLES]:
            return "vont"
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

verbes_irregular = [
    Verbe("aller", "to go", AllerPresent()),
    Verbe("avoir", "to have", AvoirPresent()),
    Verbe("être", "to be", EtrePresent()),
]

verbes_regular = [
    Verbe("abolir", "to abolish", RegularPresentIR()),
    Verbe("accepter", "to accept", RegularPresentER()),
    Verbe("accomplir", "to accomplish", RegularPresentIR()),
    Verbe("adorer", "to love", RegularPresentER()),
    Verbe("agir", "to act", RegularPresentIR()),
    Verbe("agrandir", "to enlarge/to increase", RegularPresentIR()),
    Verbe("aimer", "to like", RegularPresentER()),
    Verbe("annuler", "to cancel", RegularPresentER()),
    Verbe("appuyer", "to press", PresentUYER()),
    Verbe("arranger", "to arrange", PresentGER()),
    Verbe("attendre", "to wait for", RegularPresentRE()),
    Verbe("attraper", "to catch", RegularPresentER()),
    Verbe("avertir", "to warn", RegularPresentIR()),
    Verbe("bâtir", "to build", RegularPresentIR()),
    Verbe("bavarder", "to chat", RegularPresentER()),
    Verbe("belayer", "to sweep", PresentAYER()),
    Verbe("bénir", "to bless", RegularPresentIR()),
    Verbe("blanchir", "to whiten/to lighten", RegularPresentIR()),
    Verbe("casser", "to break", RegularPresentER()),
    Verbe("chanter", "to sing", RegularPresentER()),
    Verbe("charger", "to charge", PresentGER()),
    Verbe("chercher", "to look for", RegularPresentER()),
    Verbe("choisir", "to choose", RegularPresentIR()),
    Verbe("commander", "to order", RegularPresentER()),
    Verbe("commencer", "to begin", RegularPresentER()),
    Verbe("confondre", "to confuse", RegularPresentRE()),
    Verbe("convertir", "to convert", RegularPresentIR()),
    Verbe("correspondre", "to correspond", RegularPresentRE()),
    Verbe("couper", "to cut", RegularPresentER()),
    Verbe("danser", "to dance", RegularPresentER()),
    Verbe("demander", "to ask", RegularPresentER()),
    Verbe("défendre", "to defend", RegularPresentRE()),
    Verbe("definir", "to define", RegularPresentIR()),
    Verbe("dépendre", "to depend", RegularPresentRE()),
    Verbe("dépenser", "to spend", RegularPresentER()),
    Verbe("descendre", "to descend", RegularPresentRE()),
    Verbe("dessiner", "to draw", RegularPresentER()),
    Verbe("détester", "to hate", RegularPresentER()),
    Verbe("donner", "to give", RegularPresentER()),
    Verbe("ecouter", "to listen", RegularPresentER()),
    Verbe("effacer", "to erase", PresentCER()),
    Verbe("emprunter", "to borrow", RegularPresentER()),
    Verbe("enlever", "to remove", RegularPresentER()),
    Verbe("ennuyer", "to bore", PresentUYER()),
    Verbe("entendre", "to hear/to understand", RegularPresentRE()),
    Verbe("essayer", "to try", PresentAYER()),
    Verbe("essuyer", "to wipe", PresentUYER()),
    Verbe("établir", "to establish", RegularPresentIR()),
    Verbe("étendre", "to stretch", RegularPresentRE()),
    Verbe("étourdir", "to stun/deafen/dizzy", RegularPresentIR()),
    Verbe("étudier", "to study", RegularPresentER()),
    Verbe("exprimer", "to express", RegularPresentER()),
    Verbe("fermer", "to close", RegularPresentER()),
    Verbe("finir", "to finish", RegularPresentIR()),
    Verbe("fondre", "to melt", RegularPresentRE()),
    Verbe("franchir", "to clear an obstacle", RegularPresentIR()),
    Verbe("gagner", "to win/to earn", RegularPresentER()),
    Verbe("garder", "to keep", RegularPresentER()),
    Verbe("goûter", "to taste", RegularPresentER()),
    Verbe("grossir", "to gain weight", RegularPresentIR()),
    Verbe("guérir", "to cure/heal/recover", RegularPresentIR()),
    Verbe("habiter", "to live", RegularPresentER()),
    Verbe("hésiter", "to hesitate", RegularPresentER()),
    Verbe("investir", "to invest", RegularPresentIR()),
    Verbe("jouer", "to play", RegularPresentER()),
    Verbe("lancer", "to launch", PresentCER()),
    Verbe("laver", "to wash", RegularPresentER()),
    Verbe("maigrir", "to lose weight", RegularPresentIR()),
    Verbe("manger", "to eat", PresentGER()),
    Verbe("montrer", "to show", RegularPresentER()),
    Verbe("mordre", "to bite", RegularPresentRE()),
    Verbe("nettoyer", "to clean", PresentOYER()),
    Verbe("nourrir", "to feed/to nourish", RegularPresentIR()),
    Verbe("obéir", "to obey", RegularPresentIR()),
    Verbe("oublier", "to forget", RegularPresentER()),
    Verbe("parler", "to speak/to talk", RegularPresentER()),
    Verbe("partager", "to share", PresentGER()),
    Verbe("payer", "to pay", PresentAYER()),
    Verbe("pendre", "to hang/to suspend", RegularPresentRE()),
    Verbe("penser", "to think", RegularPresentER()),
    Verbe("perdre", "to lose", RegularPresentRE()),
    Verbe("porter", "to wear/to carry", RegularPresentER()),
    Verbe("présenter", "to introduce", RegularPresentER()),
    Verbe("prétendre", "to claim", RegularPresentRE()),
    Verbe("prêter", "to lend", RegularPresentER()),
    Verbe("prononcer", "to pronounce", PresentCER()),
    Verbe("punir", "to punish", RegularPresentIR()),
    Verbe("réfléchir", "to reflect/to think", RegularPresentIR()),
    Verbe("refuser", "to refuse", RegularPresentER()),
    Verbe("regarder", "to watch", RegularPresentER()),
    Verbe("remplir", "to fill", RegularPresentIR()),
    Verbe("rencontrer", "to meet", RegularPresentER()),
    Verbe("rendre", "to give back/to return", RegularPresentRE()),
    Verbe("répandre", "to spread/to scatter", RegularPresentRE()),
    Verbe("répondre", "to answer", RegularPresentRE()),
    Verbe("rester", "to stay/to remain", RegularPresentER()),
    Verbe("réussir", "to succeed", RegularPresentIR()),
    Verbe("rêver", "to dream", RegularPresentER()),
    Verbe("rougir", "to blush/to turn red", RegularPresentIR()),
    Verbe("saisir", "to seize", RegularPresentIR()),
    Verbe("saluer", "to greet", RegularPresentER()),
    Verbe("sauter", "to jump", RegularPresentER()),
    Verbe("sembler", "to seem", RegularPresentER()),
    Verbe("skier", "to ski", RegularPresentER()),
    Verbe("suspendre", "to suspend", RegularPresentRE()),
    Verbe("téléphoner", "to telephone", RegularPresentER()),
    Verbe("tomber", "to fall", RegularPresentER()),
    Verbe("tordre", "to twist", RegularPresentRE()),
    Verbe("tracer", "to draw", PresentCER()),
    Verbe("travailler", "to work", RegularPresentER()),
    Verbe("trouver", "to find", RegularPresentER()),
    Verbe("tutoyer", "to use", PresentOYER()),
    Verbe("utiliser", "to use", RegularPresentER()),
    Verbe("vendre", "to sell", RegularPresentRE()),
    Verbe("viellir", "to age/to grow old", RegularPresentIR()),
    Verbe("visiter", "to visit", RegularPresentER()),
    Verbe("voler", "to fly", RegularPresentER()),
    Verbe("vouvoyer", "to use", PresentOYER()),
]

# Jeu.

class Jeu:

    def __init__(self, groupes_verbes, temps):
        self.score = 0
        self.attempts = 0
        self.groupes_verbes = groupes_verbes
        self.temps = temps

    def tempRandom(self):
        return random.choice(self.temps)
    
    def verbeRandom(self):
        groupe = random.choice(self.groupes_verbes)
        return random.choice(groupe)
    
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
    jeu = Jeu([verbes_regular, verbes_irregular], [Temps.PRESENT])
    jeu.joue()
    return 0

if __name__ == "__main__":
    sys.exit(main())
