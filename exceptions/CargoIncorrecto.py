class CargoIncorrecto(Exception):
        def __init__(self, descripcion):
                
                self.descripcion = descripcion

        #luego cuando usamos el raise, pones raise CargoIncorrect(404,"el cargo del empleado es incorrecto")
        #lo otro seria cambiar todos los try y exception en uno solo
        #try:
        #exception CargoIncorrecto or CInoExiste or...... as e:
