from update import Update
from read_write import Read_Write

update = Update()
read_write = Read_Write()

# User can choose either to read_and_replace or read_and_replace_pandas and 
# comment the other to run the code and have clear understanding of the code. 

# Both functions can also be run at the same time 
# but pay attention to the old_string and new_string values.

file = '/Users/sameershekhar/Documents/GitHub/Data Science Masters/FSDS/1. Python/demo.txt'

# 1. Read and Replace using Pandas
old_string = 'test'
new_string = 'news'

read = read_write.read_file(file)
print('Pandas: File content before update\n',read)

read_replace = update.read_and_replace_pandas(file, old_string, new_string)
print(read_replace)
read = read_write.read_file(file)
print('Pandas: File content after update\n',read)

#############################################################################

# 2. Read and Replace using python default functions
old_string = 'news'
new_string = 'valid'

read = read_write.read_file(file)
print('Python: File content after update\n',read)

read_replace = update.read_and_replace(file, old_string, new_string)
print(read_replace)
read = read_write.read_file(file)
print('Python: File content after update\n',read)