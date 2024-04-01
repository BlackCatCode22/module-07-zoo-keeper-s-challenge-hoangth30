# Import the Animal class from the Animal module
from Animal import Animal

class Hyena(Animal):
    # create a static class variable to keep track of the number of hyenas created
    numOfHyenas = 0

    # Create the hyena sound
    hyena_sound = " laugh...laugh "

    # Create a list of hyena names.
    list_of_hyena_names = []

    file_path = r'C:\2023spring\2023fall\python\dataFiles\animalNames.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Iterate through the lines in the file
        line_num = 1
        for line in lines:
            if line_num == 3:
                list_of_hyena_names.extend(line.strip().split(', '))
                break
            else:
                line_num += 1

    def __init__(self, name="a_name", animal_id="an_id", birth_date="2099-01-01", color="a_color", gender="a_gender",
                 weight="a_weight", originating_zoo="a_zoo", date_arrival="2099-01-01"):
        # Increment the static variable numOfHyenas when a new Hyena object is created
        Hyena.numOfHyenas += 1

        # Call the constructor of the parent class (Animal) with 'Hyena' as the species
        super().__init__("hyena", name, animal_id, birth_date, color, gender, weight, originating_zoo, date_arrival)

    def make_sound(self):
        return self.hyena_sound

    # the hyena object will call this method to get an unused hyena name. pop() will remove the first element from
    #   the list_of_hyena_names[]
    def get_hyena_name(self):
        return self.list_of_hyena_names.pop(0)


