import re
from Animal import Animal
import datetime

# Dictionary to store available names
available_names = {}

# Function to read names from file
def read_animal_names():
    with open("animalNames.txt", "r") as file:
        current_species = None
        for line in file:
            line = line.strip()
            if line.endswith("Names:"):
                current_species = line.split()[0].lower()
                available_names[current_species] = []
            elif line:
                names = [name.strip() for name in line.split(",")]
                available_names[current_species].extend(names)

# Function to process arriving animals and generate the zoo population report
def process_arriving_animals():
    with open("arrivingAnimals.txt", "r") as file:
        animals = file.readlines()

    with open("zooPopulation.txt", "w") as report:
        habitats = {"hyena": [], "lion": [], "tiger": [], "bear": []}

        for animal in animals:
            animal = animal.strip()
            match = re.match(r"(\d+) year old (female|male) (\w+), (?:born in )?([^,]+), (.+) color, (\d+) pounds, from (.*)", animal)
            if match:
                age = int(match.group(1))
                sex = match.group(2)
                species = match.group(3).lower()
                birth_season = match.group(4).lower() if match.group(4).lower() != "unknown" else None
                color = match.group(5)
                weight = int(match.group(6))
                origin = match.group(7)

                animal_obj = Animal(species, age, sex, birth_season, color, weight, origin, available_names)
                habitats[species].append(animal_obj.get_animal_info())

        for species, animals in habitats.items():
            report.write(f"{species.capitalize()} Habitat:\n")
            if not animals:
                report.write("No animals in this habitat\n")
            for animal_info in animals:
                report.write(f"{animal_info}\n")
            report.write("\n")

# Main function to execute the script
def main():
    read_animal_names()
    process_arriving_animals()

if __name__ == "__main__":
    main()