class Auto:
    def __init__(self, modelo, ano, score):
        self._modelo = modelo
        self._ano = ano 
        self._score = score

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        self._score = value

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        self._modelo = value

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, value):
        self._ano = value