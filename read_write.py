from validate import Validate


class Read_Write(Validate):
    def read_file(self,file:str):
            '''
            Reads a file and returns the content.

            file: give the entire path of the file along with file name and extension

            example:    
            filecontent = 'This is a test file'

            file = 'C:/Users/User/Desktop/file.txt'
            read_file(file)
            result --> 'This is a test file'

            
            
            
            '''
            if self.file_exists(file):
                if self.file_is_txt(file):
                    if self.file_not_empty(file):
                        with open(file, 'r') as f:
                            filecontent  = f.read()
                        return filecontent

    def write_file(self, file:str, content:str):
        '''
        Writes a file.

        file: give the entire path of the file along with file name and extension

        content: the content to be written to the file

        example:    
        filecontent = 'This is a test file'

        file = 'C:/Users/User/Desktop/file.txt'
        write_file(file, filecontent)
        result --> 'The text file was successfully written.'

        
        
        
        '''
        try:
            with open(file, 'w') as f:
                f.write(content)
            return 'The text file was successfully written.'
        except Exception as e:
            return (e)
