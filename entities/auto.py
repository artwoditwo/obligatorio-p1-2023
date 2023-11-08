class Auto:
    def __init__(self, modelo, ano, score):
        self._modelo = modelo
        self._ano = ano 
        self._score = score

    @property
    def score(self):
        return self._score