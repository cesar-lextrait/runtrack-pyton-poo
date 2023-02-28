class Students:

    def __init__(self, nom, prenom, id, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__id = id
        self.__credits = credits
        self.__level = self.__studentEval()

    def studentInfo(self):
        self.__level = self.__studentEval()

        print(f"Nom = {self.__prenom} ")
        print(f"Prénom = {self.__nom}")
        print(f"Student ID = {self.__id}")
        print(f"Student Level = {self.__level}")

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits

    def get_credits(self):
        return self.__credits

    def __studentEval(self):
        if self.__credits >= 90:
            return("Excellent")
        elif self.__credits >= 80:
            return("Tres bien")
        elif self.__credits >= 70:
            return("Bien")
        elif self.__credits >= 60:
            return("Passable")
        elif self.__credits < 60:
            return("Insuffisant")
                
john_doe = Students("Doe", "John", 145, 78)
john_doe.studentInfo()