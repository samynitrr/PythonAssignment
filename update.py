import pandas as pd
from validate import Validate
from read_write import Read_Write

class Update(Read_Write):
    
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
        if self.file_exists(file):
            if self.file_is_txt(file):
                if self.file_not_empty(file):
                    df = pd.read_csv(file, header = None)
                    df.columns=['text']
                    if self.file_has_old_string(file, old_string):
                        df['text'] = df['text'].str.replace(old_string,new_string)
                        df.to_csv(file, index=False, header=None)
                        return 'The text file was successfully read and replaced.'
                    else:
                        raise Exception ('The text file was successfully read but not replaced.')
        
        

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
        filecontent = self.read_file(file)
        if self.file_has_old_string(file, old_string):
            filecontent = filecontent.replace(old_string, new_string)
            self.write_file(file, filecontent)
            return 'The text file was successfully read and replaced.'            
        else:
            raise Exception ('The text file was successfully read but not replaced.')