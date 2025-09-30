class SensorManager:
    # Attribut de classe
    sensor_count = 0

    def __init__(self, name, value):
        self.name = name
        self._value = value
        SensorManager.sensor_count += 1

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, (int, float)):
            raise ValueError("La valeur doit être numérique")
        self._value = new_value

    @classmethod  # décorateur @classmethod
    def get_sensor_count(cls):
        return cls.sensor_count

    @staticmethod   # décorateur @staticmethod
    def is_valid_value(v):
        return isinstance(v, (int, float))

    def __str__(self):
        return f"{self.name} -> {self._value}"

# Démonstration
s1 = SensorManager("Capteur A", 12)
s2 = SensorManager("Capteur B", 18.5)
print(s1)                          # Utilise __str__
print(SensorManager.get_sensor_count())  # Méthode de classe
print(SensorManager.is_valid_value(10))  # Méthode statique