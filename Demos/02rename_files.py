import os
file_list = os.listdir(r"E:\Python\Demos\rename_files")# in windows machine add letter 'r' before path- which instruct python that take this string as it is and dont interpretate anything else.
    #A raw string tells Python to ignore all formatting within a string, including escape characters. 
#function defination
def rename_files():
      # print(file_list)
    #find the current directory path
    saved_path = os.getcwd() #cwd -current working directory
    print("Current Working Directory is :"+saved_path)
    #Lets change the current working directory to the files directory
    os.chdir(r"E:\Python\Demos\rename_files")
    print("*********************************************\nOld file names : ")
    #(2) For each file rename filename
    for file_name in file_list:
       print(file_name)
       #file_name.replace("0123456789","")  
       os.rename(file_name, file_name.translate(str.maketrans('','','0123456789')))
       #file_list1 = [fname.translate(None,"0123456789") for fname in file_list]
    os.chdir(saved_path)
        
    
def list_new_files():
    print("*********************************************\nNew file names : ")
    #(2) For each file rename filename    
    for file_name in file_list:
        print(file_name)
        
#calling the function
      
rename_files()
list_new_files()
