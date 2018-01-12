"""
    multi-Line comments
"""
'''
    also multi-line comments
'''

import webbrowser
import time

total_break=3
break_count=0

print("Program Started on...."+time.ctime())
while(break_count<3):

    time.sleep(10)# single line comment - sleep() function takes seconds as parameter
    webbrowser.open("https://www.youtube.com/watch?v=fejBO1HZXVQ")
    break_count=break_count+1
 
