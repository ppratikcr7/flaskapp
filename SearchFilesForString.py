# Import the mandatory modules 
import os
import re
import sys
import argparse

class Text_search:

    def __init__(self, string2, path1,i=None):
        self.path1= path1
        self.string1 = string2
        self.i=i
        if self.i:
            string2 = string2.lower()
            self.string2= re.compile(string2)

    def txt_search_m(self):
        files = [f for f in os.listdir(self.path1) if os.path.isfile(self.path1+"/"+f)]
        file_number = 0
        for file in files:
            file_t = open(self.path1+"/"+file)
            line_number=1
            flag_file = 0
            for line1 in file_t:
                if self.i:
                    line1 = line1.lower()
                if re.search(self.string1, line1):
                    flag_file= 1
                    print( "The text '"+self.string1+"' found in ", file, " at line number ",line_number)
                line_number=line_number+1
                if flag_file == 1:
                    file_number=file_number+1
                    flag_file=0
            file_t.close() 
        print( "total files are ",file_number)


parser = argparse.ArgumentParser()
parser.add_argument('string')
parser.add_argument('dir')
args = parser.parse_args()
dir = args.dir
print(dir)
obj1 = Text_search(args.string,dir)
obj1.txt_search_m()
# DOMICILIO FISCALE: INDIRIZZO