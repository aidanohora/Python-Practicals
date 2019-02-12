#Program to read code from a webpage file
#counts and prints to occurences of certain symbols and elements
#checks that the file exists first

import os

webfile = input("Enter the name of the file containing the webcode: ")

#to check if the input file exists
if not os.path.isfile(webfile):
    print("File", webfile, "does not exist.")
else:
    fh1 = open(webfile, 'r')
    webcode = fh1.read()
    #to check if the output file exists
    if not os.path.isfile('results.txt'):
        print("Something happened to the output file - please create a new text file called 'results' in the program folder and restart the program.")
    else:    
        fh2 = open('results.txt', 'w')
        fh2.write("Number of occurences of '<':" + str(webcode.count("<"))+"\n")
        fh2.write("Number of occurences of '>':" + str(webcode.count(">"))+"\n")
        fh2.write("Number of new lines:" + str((webcode.count("br/")+webcode.count("<br>")+webcode.count("br /")))+"\n")
        fh2.write("Number of occurences of 'e':" + str(webcode.count("e"))+"\n")
        fh2.write("Number of occurences of '<!--':" + str(webcode.count("<!--"))+"\n")
        fh2.write("Number of occurences of '-->':" + str(webcode.count("-->"))+"\n")
        fh2.close()
        print("See results.txt for results.")
    
    
    

    
