# This is an example for the abstract class. Abstract Classes are blueprints for classes. They are used to define the structure of a class.
# Look at below example. In this example, we are defining the structure of a class. Using this structure I have create a single inheritance class to be used in a project.
'''
class file:
    pass
class fileoperations(file):
    pass
'''

import os

class file:    
    def __init__(self, filepath):
        self.path = filepath
    
    def file_exists(self):
        if os.path.isfile(self.path):
            return True
        else:
            raise Exception('File does not exist! Provide a correct file path')
    
    def read(self):
        if self.file_exists():
            rd = open(self.path,"r")
        return rd.read()
    
    def write(self):
        if self.file_exists():
            wr = open(self.path,"r+")
            writetxt = input()
            wr.write(writetxt)
            wr.close()
    
class fileoperations(file):
    pass

fl = fileoperations('/Users/sameershekhar/Documents/GitHub/Data Science Masters/FSDS/1. Python/Object Oriented Programming/file.txt')
content = fl.read()
print(content)