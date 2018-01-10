import urllib.request
def read_text():

    quotes = open("E:\\Python\\Assignment\\10movies_quotes.txt")#opening the file by passing absolute path
    contents_of_file=quotes.read()#reading the whole file and storing the content in the variable
    #print(contents_of_file)#printing the content of the file
    quotes.close()#closing the file that we opened
    #call check_profanity(contents_of_file)
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    encoded_text = urllib.parse.quote(text_to_check, 'utf-8')
    address = "http://www.wdylike.appspot.com/?q="+encoded_text
    #print(address)
    connection= urllib.request.urlopen(address)
    output=connection.read()
    connection.close()
    print(output)
    if "b'true'":
        print ("Profanity Alert!!!!!")
    elif "b'false'":
        print("This Document has no curse words!!")
    else:
        print("Could not the scan the document properly!!")
    

read_text()

'''
Have to observed... for using function'open()' we have not imported anything
bcoz open() function is so common that they are already available...
lets check the python docs...
open() returns an object of the file type

Now check out built in functions in python

https://docs.python.org/3/library/functions.html

and now use built in function of your choice which help us to figure out curse word
'''
