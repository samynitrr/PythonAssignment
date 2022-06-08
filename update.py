import pandas as pd
from validate import Validate
from read_write import Read_Write
from log import *

validate = Validate()
read_write = Read_Write()

class Update():
    
    def read_and_replace_pandas(self, file:str, old_string:str, new_string:str):
        '''
        Reads a file and replaces all occurrences of a string with another string.

        file: give the entire path of the file along with file name and extension

        old_string: the string to be replaced
        
        new_string: the string to replace the old string

        example:    
        filecontent = 'This is a test file'

        file = 'C:/Users/User/Desktop/file.txt'
        read_and_replace(file, 'test', 'what')
        result --> 'The text file was successfully read and replaced.'

        filecontent = 'This is a what file'
        
        
        '''  
        try:
            if validate.file_exists(file) & validate.file_is_txt(file) & validate.file_not_empty(file):
                df = pd.read_csv(file, header = None)
                df.columns=['text']
                if validate.file_has_old_string(file, old_string):
                    df['text'] = df['text'].str.replace(old_string,new_string)
                    df.to_csv(file, index=False, header=None)
                    return 'The text file was successfully read and replaced.'
        except Exception as e:
            return (e)

    def read_and_replace(self,file:str, old_string:str, new_string:str):
        '''
        Reads a file and replaces all occurrences of a string with another string.

        file: give the entire path of the file along with file name and extension

        old_string: the string to be replaced
        
        new_string: the string to replace the old string

        example:    
        filecontent = 'This is a test file'

        file = 'C:/Users/User/Desktop/file.txt'
        read_and_replace(file, 'test', 'what')
        result --> 'The text file was successfully read and replaced.'

        filecontent = 'This is a what file'
        
        
        '''
        try:            
            filecontent = read_write.read_file(file)
            if validate.file_has_old_string(file, old_string):
                filecontent = filecontent.replace(old_string, new_string)
                read_write.write_file(file, filecontent)
                return 'The text file was successfully read and replaced.'            
        except Exception as e:
            return (e)