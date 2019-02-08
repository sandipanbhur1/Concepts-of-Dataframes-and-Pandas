
#The second record specifies the column datatype that has to be used for DataFrame or Dataset of the Spark/Flink application and should be eliminated from the result output. 

#Records do not match the header layout or datatype specified in the second test line have to be redirected to the quarantine.txt output file.

#The transformed cleaned records should be stored to the output.txt file.


import os              # providing functions for interacting with operating system
import csv             # used to read and write a csv file 
import pandas as pd    # it is a library of Python used for doing data analysis

txt_file = "quarantine.txt"
csv_file = "quarantine2.csv"

in_txt = csv.reader(open(txt_file,"r"), delimiter = ',')  #opening quarantine.txt file in read-only mode
out_csv = csv.writer(open(csv_file,"w"))                  #writing the quarantine.txt file contents to quarantine2.csv file 

out_csv.writerows(in_txt)                                 #it will write the objects of a text file to a csv file

rm_quote = lambda x: x.replace('"','')                    #cleansing of quotations in the file by replacing with ''
df = pd.read_csv("quarantine2.csv",engine = 'python',  converters = {"error_message" : rm_quote, "name" : rm_quote, "age" : rm_quote, "salary" : rm_quote, "benefits" : rm_quote, "departments" : rm_quote}, skipinitialspace=True)  #reading a csv file
df = df.rename(columns=rm_quote)                          #renaming all the quotations with '' in the dataframe
df['name']= df['name'].str.strip()                        #removing all the whitespace in the name column in a dataframe
df['salary']= df['salary'].str.strip()                    #removing all the whitespace in the salary column in a dataframe
df2 = df.drop('error_message',1)                          #drop or remove the first column 'error message' in a dataframe
df2.to_csv('quarantine3.csv',header = None,index = False) #writing the updated dataframe to a csv file with all the headers and index removed

txt_file = 'output.txt'
csv_file = 'quarantine3.csv'

with open(txt_file,'a') as f:                             #open output.txt file in append mode
    with open(csv_file,'r') as fo:                        #open quarantine3.csv file in read only mode 
        [f.write(" ".join(row) + '\n') for row in csv.reader(fo)] #contents of the quarantine3.csv file has to get appended in output.txt file 
    f.close()                                                     #output.txt file will be closed after operation gets successfully completed
