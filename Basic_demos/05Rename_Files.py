import os


# function defination
def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(
        r"E:\Python\Demos\rename_files")  # in windows machine add letter 'r' before path- which instruct python that take this string as it is and dont interpretate anything else.
    print(file_list)
    # (2) For each file rename filename
    for file_name in file_list:
        os.rename(file_name)

# calling the function
rename_files()
