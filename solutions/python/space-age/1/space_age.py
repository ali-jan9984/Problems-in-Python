class SpaceAge:
    def __init__(self, seconds):
        self.age_in_seconds = seconds
        self.earth_one_year = (1 * (365.25/1) * (24/1) * (60/1) * (60/1))
    def on_earth(self):
        return round(self.age_in_seconds / self.earth_one_year,2)
    def on_mercury(self):
        return round(SpaceAge.on_earth(self) / 0.2408467,2)
    def on_venus(self):
        value = SpaceAge.on_earth(self) / 0.61519726
        return int(value * 100) / 100
    def on_mars(self):
        return round(SpaceAge.on_earth(self)/ 1.880858,2)
    def on_jupiter(self):
        return round(SpaceAge.on_earth(self)/ 11.862615,2)
    def on_saturn(self):
        return round(SpaceAge.on_earth(self)/ 29.447498,2)
    def on_uranus(self):
        return round(SpaceAge.on_earth(self)/ 84.016846,2)
    def on_neptune(self):
        return round(SpaceAge.on_earth(self)/ 164.79132,2)