import random

class Dado:
    @staticmethod
    def tirar():
        return random.randint(1,6)