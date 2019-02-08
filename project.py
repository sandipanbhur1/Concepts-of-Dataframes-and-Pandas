
#Code to remove the whitespaces,headers and quotations from emp.txt file


import re      #regex(regular expression) function
import os      # providing functions for interacting with operating system

os.getcwd()    #mention the current path which you will write your file

with open('emp.txt','r') as f, open('emp2.txt','w') as fo:  
    next(f)                                                   #cleansing the header of the file
    for line in f:
        line = re.sub( '\s+', '',line).strip()                #removing all the whitespace in that text file
        print(line)
        fo.write(line.replace('"','').replace("'",''))        #replace the quotations with '' in that text file
        fo.write("\n")                                        #after each replacement it will redirect to the next line
        