import datetime

class Animal:
    animal_counters = {
        "hyena": 1,
        "lion": 1,
        "tiger": 1,
        "bear": 1
    }

    def __init__(self, species, age, sex, birth_season, color, weight, origin, available_names):
        self.species = species.lower()
        self.age = age
        self.sex = sex
        self.birth_season = birth_season.lower() if birth_season not in [None, "unknown"] else None
        self.color = color
        self.weight = weight
        self.origin = origin
        self.available_names = available_names
        self.birth_date = self.gen_birth_date()
        self.unique_id = self.gen_unique_id()
        self.name = self.assign_name()

    def gen_birth_date(self):
        current_year = datetime.datetime.now().year
        birth_year = current_year - self.age
        season_dates = {
            "spring": "-03-21",
            "summer": "-06-21",
            "fall": "-09-21",
            "winter": "-12-21"
        }
        if self.birth_season in season_dates:
            birth_date = f"{birth_year}{season_dates[self.birth_season]}"
        else:
            birth_date = f"{birth_year}-01-01"  # Default to January 1st if unknown
        return birth_date

    def gen_unique_id(self):
        species_code = self.species[:2].upper()
        unique_id = f"{species_code}{Animal.animal_counters[self.species]:02d}"
        Animal.animal_counters[self.species] += 1
        return unique_id

    def assign_name(self):
        if self.available_names[self.species]:
            return self.available_names[self.species].pop(0)
        else:
            return f"Unnamed_{self.species}_{Animal.animal_counters[self.species]}"

    def get_animal_info(self):
        return f"{self.unique_id}, {self.name}; birth date: {self.birth_date}; {self.color} color; {self.sex}; {self.weight} pounds; from {self.origin}; arrived: {datetime.datetime.now().date()}"
