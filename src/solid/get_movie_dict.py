import re

def get_movie_dict(i, chunk):
    
    # movie title, year and place
    movie_string = chunk[1].get_text()
    movie_title = re.search('(?<=\.\\n      )(.*)(?=\\n\()', movie_string).group(1)
    year = re.search('\((\d*?)\)', movie_string).group(1)
    place = re.search('\d{1,3}', movie_string).group(0)

    # crew
    crew = chunk[1].a.attrs.get("title")

    # rating
    rating = chunk[0].findChild('span', {'name':'ir'}).attrs.get('data-value')

    # vote
    vote = chunk[2].findChild('strong').attrs.get('data-value')

    # link
    link = chunk[1].a.attrs.get('href')

    movie_dict = {"movie_title": movie_title,
        "year": year,
        "place": place,
        "star_cast": crew,
        "rating": rating,
        "vote": vote,
        "link": link,
        "preference_key": i % 4 + 1}
    
    
    return movie_dict