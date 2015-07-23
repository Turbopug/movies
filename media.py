class Movie():
    """Provides a way to store movie related information.

    Args:
        title: A string representing the title of the movie.
        summary: A string representing a summary of the movie.
        poster_image: A string that points to an image of the movie poster.
        trailer_youtube: A string of the youtube URL for the movie's trailer.
        cast: A string of the actors starring in the movie.
        released: A string of the date the movie was released.
    """

    def __init__(self, title, summary, poster_image, trailer_youtube, cast, released):
        """Inits Movie and assigns parameters to instance variables."""
        self.title = title
        self.summary = summary
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.cast = cast
        self.release_date = released
