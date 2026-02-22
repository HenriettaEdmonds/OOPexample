class Console:
    def __init__(self, name, release_year, manufacturer, generation):
        self.name = name
        self.release_year = release_year
        self.manufacturer = manufacturer
        self.generation = generation
    
    def is_vintage(self):
        self.release_year >= 2000
    
    def __str__(self):
       return (f"Name: {self.name}, Release Year: {self.release_year}, Manufacturer: {self.manufacturer},Generation: {self.generation}")
        

def read_consoles(csv_filepath):

    try:
        data = open(csv_filepath, 'r')
    except FileNotFoundError:
        print("file was not found")
        return {}
    else:
        data.readline() 
        consoles = {}
        for line in data:
            line.strip().split(',')
            name = line[0]
            try:
                release_year = int(line[1])
            except:
                return f"Invalid release year format in CSV file. Skipping {name}... "

            manufacturer = line[2]
            generation = line[3]

            new_console = Console(name, release_year, manufacturer, generation)

            consoles[name]= new_console
    return consoles

def main():
    console_dictionary = read_consoles("consoles.csv")
    for console in console_dictionary.items():
         print(console)
         print()
         if Console.is_vintage() == True:
             print(f"This console is vintage")
    
main()
      


    





