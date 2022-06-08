from update import Update
from read_write import Read_Write

update = Update()
read_write = Read_Write()

file = '/Users/sameershekhar/Documents/GitHub/Data Science Masters/FSDS/1. Python/demo.txt'
old_string = 'news'
new_string = 'test'

read = read_write.read_file(file)
print('File content before update\n',read)

# read_replace = update.read_and_replace_pandas(file, old_string, new_string)
read_replace = update.read_and_replace(file, old_string, new_string)
read = read_write.read_file(file)
print('File content after update\n',read)