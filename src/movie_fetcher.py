# Principio de Inversión de Dependencias: No existen dependencias entre los módulos ya que ellos están separados
from solid.DataFetcher import DataFetcher
from solid.get_movie_dict import get_movie_dict
from solid.file_writer import CSVWriter

def main():

    # Principio de responsabilidad única: fetch_data solo se encarga de usar requests para obtener la información del sitio web
    url = 'http://www.imdb.com/chart/top'
    fetcher = DataFetcher(url)
    fetcher.fetch_data()
    
    # Principio de responsabilidad única: get_movies solo se encarga de usar BeautifulSoup para leer el contenido del sitio web y generar una lista de películas
    movies = fetcher.get_movies()
    
    # Principio de responsabilidad única: get_movie_dict solo se encarga de encontrar los datos relevantes en el contenido del sitio web por película
    list = [get_movie_dict(i, movie) for i, movie in enumerate(movies)]
    
    # Principio de responsabilidad única: CSVWriter solo se encarga de generar un archivo csv con la información de las películas
    writer = CSVWriter(list)
    writer.write()


if __name__ == '__main__':
    main()
