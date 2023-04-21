import csv
import abc

# Principio abierto/cerrado : Este módulo podría extenderse con clases que generen otro tipo de archivos diferentes a csv (xlsx por ejemplo), sin afectar que aún pueda generar archivos csv.
class FileWriter(abc.ABC):
    
    def __init__(self, list) -> None:
        self.list = list
        
    @abc.abstractmethod
    def write(self):
        raise Exception("I am an interface")

# Principio de segregación de la interfaz: La clase CSVWriter implementa el método abstracto write() de la interfaz FileWriter
class CSVWriter(FileWriter):
    
    def write(self) -> None:
        fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
        with open("movie_results.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for movie in self.list:
                writer.writerow({**movie})