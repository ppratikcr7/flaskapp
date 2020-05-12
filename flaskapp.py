# Import the mandatory modules 
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
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

    def txt_search(self):
        files = [f for f in os.listdir(self.path1) if os.path.isfile(self.path1+"/"+f)]
        file_number = 0
        search_result = []
        output = ""
        for file in files:
            file_t = open(self.path1+"/"+file)
            line_number=1
            flag_file = 0
            for line1 in file_t:

                if len(line1) == 1:
                    continue

                if self.i:
                    line1 = line1.lower()
                    
                if re.search(self.string1, line1):
                    flag_file= 1
                    result = "The text '" + self.string1 + "' found in " + file + " at line number " + str(line_number)
                 
                line_number=line_number+1
                if flag_file == 1:
                    file_number=file_number+1
                    flag_file=0
            
            search_result.append("\n")
            search_result.append(result)

            file_t.close()
        
        output = "".join(search_result)

        return output
        #print( "total files are ",file_number)


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/searchFunction',methods=['POST'])
def searchFunction():
    search_string = [str(x) for x in request.form.values()]
    print(search_string[0])
    # parser = argparse.ArgumentParser()
    # parser.add_argument('string')
    #parser.add_argument('dir')
    # args = parser.parse_args()
    #dir = args.dir
    #print(dir)
    #obj1 = Text_search(args.string,dir)
    obj1 = Text_search(search_string[0], "text")
    output = obj1.txt_search()
    print(output)
    #output = round(prediction[0], 2)
    # output = "The text 'DOMICILIO FISCALE: INDIRIZZO' found in  doc1.txt  at line number  14 <br> \
    # The text 'DOMICILIO FISCALE: INDIRIZZO' found in  doc2.txt  at line number  8 <br> \
    # total files are  2"

    return render_template('index.html', result_text='The search string appears in : {}'.format(output), search_string= search_string[0])

if __name__ == "__main__":
    #app.run(host="13.235.24.166", port= 5000)
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='13.235.24.166', port=PORT)