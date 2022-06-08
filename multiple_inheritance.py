# This is an example for the multiple inheritance. Multiple inheritance is when a child class inherits from more than one class.

# Parent class1
class Movie_id:
    id = "1"
    def __init__(self,a,b,c):
        self.a = a 
        self.b= b 
        self.c = c  
    def id(self):
        print(self.id)
 
# Parent class2
class Movie_name:
    movie_name = "Top Gun Maverick"
    def movie(self):
        print(self.movie_name)
 
# Child class
class Customer(Movie_id, Movie_name):
    def watch_movie(self):
        print("Movie Id :", self.id)
        print("Movie Name :", self.movie_name)
 
# Child class code
c1 = Customer(4,5,6)
c1.id = "2"
c1.movie_name = "Doctor Strange: Multiverse of Madness"
c1.watch_movie()

