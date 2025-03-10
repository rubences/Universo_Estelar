import math

class Estrella:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def galaxia(self):
        # Aquí puedes implementar la lógica para determinar la galaxia basada en las coordenadas
        if self.x > 1000 and self.y > 1000 and self.z > 1000:
            return "Galaxia Andrómeda"
        elif self.x > 500 and self.y > 500 and self.z > 500:
            return "Galaxia Vía Láctea"
        else:
            return "Galaxia Desconocida"
        return "Galaxia Desconocida"

    def distancia(self, otra_estrella):
        return math.sqrt((self.x - otra_estrella.x)**2 + (self.y - otra_estrella.y)**2 + (self.z - otra_estrella.z)**2)