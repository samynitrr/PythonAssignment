# PythonAssignment

This is a python assignment.

https://drive.google.com/file/d/1vkmqcjYHQr_hKe8qRBmLc-T8tO2Cb7ev/view

1. Create a function in python to read the text file and replace specific content of the file.

```
example:    
        filecontent = 'This is a placement assignment'

        file = 'C:/Users/User/Desktop/example.txt'
        read_and_replace(file, 'placement', 'screening')
        result --> 'The text file was successfully read and replaced.'

        filecontent = 'This is a screening assignment'

```


This code is written with OOPS concept. It is created with multiple classes. 
- validate.py : It has a validate Class which checks for file exists, file format and file content not empty and old_string exists in file.

- read_write.py : It has a Read_Write Class which reads the file and writes the file with updated content. It also inherits validate class in order to perform read and write operations.

- update.py : It has a update class. It reads the file and replaces the old_string with new_string. It also inherits validate and read_write class in order to validate the file and content and perform read and write operations. It has 2 options to perform this operation. The first is using pandas and the other is using default python file operations.



2. Demonstrate use of abstract class, multiple inheritance and decorator in python using examples.

- abstract.py
- multiple_inheritance.py
- decorator.py