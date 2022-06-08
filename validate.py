import os.path
class Validate():
    def file_exists(self,file:str):
        '''
        Checks if a file exists.

        file: give the entire path of the file along with file name and extension

        example:    
        //File Exists
        file = 'C:/Users/User/Desktop/file.txt'
        file_exists(file)
        result --> True

        //File Does Not Exist
        file = 'C:/Users/User/Desktop/filertr.txt'
        file_exists(file)
        result --> False 
        '''
        try:
            if os.path.exists(file):
                return True
        except Exception as e:
            return ('File does not exist.')
    
    def file_is_txt(self,file:str):
        '''
        Checks if a file is a txt file.

        file: give the entire path of the file along with file name and extension

        example:    
        //File is txt
        file = 'C:/Users/User/Desktop/file.csv'
        file_is_csv(file)
        result --> True

        //File is not txt
        file = 'C:/Users/User/Desktop/file.txt'
        file_is_csv(file)
        result --> False 
        '''
        try:
            if file.endswith('.txt'):
                return True
        except Exception as e:
            return ('File is not a txt file.')

    def file_not_empty(self,file:str):
        '''
        Checks if a file is empty.

        file: give the entire path of the file along with file name and extension

        example:    
        //File is Empty
        file = 'C:/Users/User/Desktop/file.txt'
        file_not_empty(file)
        result --> False

        //File is Not Empty
        file = 'C:/Users/User/Desktop/file.txt'
        file_not_empty(file)
        result --> True 
        '''
        try:
            if os.path.getsize(file) > 0:
                return True
        except Exception as e:
            return ('File is empty.')         

               

    def file_has_old_string(self,file:str, old_string:str):
        '''
        Checks if a file contains a string.

        file: give the entire path of the file along with file name and extension

        old_string: the string to be replaced

        example:    
        //File has old string
        file = 'C:/Users/User/Desktop/file.txt'
        file_has_old_string(file, 'old')
        result --> True

        //File does not have old string
        file = 'C:/Users/User/Desktop/file.txt'
        file_has_old_string(file, 'new')
        result --> False 
        '''
        try:
            if old_string in open(file).read():
                return True
        except Exception as e:
            return ('File does not contain the {old_string}.')