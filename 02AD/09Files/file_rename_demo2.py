import os

# Rename a file from test1.txt to test2.txt
os.rename( "test1.txt", "test2.txt" )

# Delete file test2.txt
os.remove("text2.txt")

# Create a directory "test"
os.mkdir("test")

os.chdir("newdir")


# Changing a directory to "/home/newdir"
os.chdir("/home/newdir")

#The getcwd() method displays the current working directory.

# This would give location of the current directory
os.getcwd()

#The rmdir() method deletes the directory, which is passed as an argument in the method.

# This would  remove "/tmp/test"  directory.
os.rmdir( "/tmp/test"  
