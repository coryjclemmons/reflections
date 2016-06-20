# Navigate to the directory where the files are
# read the name of the first file as a string
# crop the number from the from of the name - 2 digits
# rename the file using the revised string
# loop through the rest of the files with the same routine
import os



def rename_files():

 file_list = os.listdir(r"/Users/coryclemmons/Downloads/Lesson1Video")
 print(file_list)
 saved_path = os.getcwd()
 print(saved_path)
 os.chdir(r"/Users/coryclemmons/Downloads/Lesson1Video")

 
 for file_name in file_list:
     os.rename(file_name, file_name.translate(None, "0123456789-"))

 os.chdir(saved_path)

rename_files()
