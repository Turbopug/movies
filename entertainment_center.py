import media
import fresh_tomatoes
import xml.etree.ElementTree as ET

# Parse the movies.xml document 
tree = ET.parse('movies.xml')

root = tree.getroot()
my_movies = []

# Iterates over the child elements and appends a new instance of
# media.Movie class to the my_movies list.
for movie in root.findall('movie'):
    my_movies.append(media.Movie(movie.find('title').text,
                                 movie.find('summary').text,
                                 movie.find('poster').text,
                                 movie.find('trailer').text,
                                 movie.find('cast').text,
                                 movie.find('released').text))

# Create the html page with the list
fresh_tomatoes.open_movies_page(my_movies)

