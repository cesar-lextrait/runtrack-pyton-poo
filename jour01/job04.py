class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("Je suis", self.nom, self.prenom) 

A = Personne('John', 'Doe')
B = Personne('Ma', 'Ma')
C = Personne('Za', 'Za')

A.SePresenter()
B.SePresenter()
C.SePresenter()