import webbrowser
#refer google style guide 
#class is a keyword to define a class and classname must b in pascal case
class Movie():
      """This class provides a way to store movie related information"""
    VALID_RATINGS = ["G","PG","PG-13","R"] 
    #internally it calls a __init__ function which is also called as constructor which is used to create an instance of a class
#init has two underscore before and after init keyword, that means it tells the programmer that its a reserved predefined function, which is used to create speace in memory to create a new object
#init takes few pecies of arguments
    #- self - is the object being created ,just like 'this' in java ...current object or current instance
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
    #what will happen if we remove the self keyword in front of the instance variable and then run it.


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
