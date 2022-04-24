#Dev: Carlos A. Rosario
#Description: Rename movie folders to remove unwanted string parts

import os
import re

#Change path for folder you would like to cleanup
path = r'\\SWNas\Multimedia\Movies'

#Enable if you would like to generate text file with results
#textfile = r'\scriptresults.txt'
#f = open((path + textfile), "w")

#Giant string with text you want to remove
giantstring = '10BITSBLURAYHEVCWEB-DLWEBRIPDDP5X264-EVX265-TERMINALMZABIEV0UHDHDRSDRHEVC-MZABIAMZNEVO-CMRYIFYRARBGYTSAC3-EVOXVID'

#Loop through folders in specified path
for root, dirs, files in os.walk(path):
    for name in dirs:
        #Variables used
        newstring = ''
        finalstring = ''
        finalname = ''
        
        #Assign name to new variable to format it to my liking
        newname = name
        newname = newname.replace('5.1', '')
        newname = newname.replace('H.264', '')
        newname = newname.replace('.', ' ')
        
        #Loop through parenthesis if the string has any
        parenthloop = newname
        newbeginindex=0
        newendindex=0
        while parenthloop.find('(') > -1:
            while parenthloop.find(')') > -1:
                beginparenthesis = parenthloop.find('(')
                endparenthesis = parenthloop.find(')')
                newbeginindex = (newbeginindex + beginparenthesis)
                newendindex = (newendindex + endparenthesis)
                newname = newname[:newbeginindex] + newname[newendindex+1:]
                newstring = newstring + (parenthloop[beginparenthesis+1:endparenthesis]) + ' '
                parenthloop = parenthloop[endparenthesis+1:]
        
        #Loop through brackets if the string has any
        newbeginindex=0
        newendindex=0
        bracketloop = newname
        while bracketloop.find('[') > -1:
            while bracketloop.find(']') > -1:
                beginbracket = bracketloop.find('[')
                endbracket = bracketloop.find(']')
                newbeginindex = (newbeginindex + beginbracket)
                newendindex = (newendindex + endbracket)
                newname = newname[:newbeginindex] + newname[newendindex+1:]
                newstring = newstring + (bracketloop[beginbracket+1:endbracket]) + ' '
                bracketloop = bracketloop[endbracket+1:]
        
        #Format brackets and parentheses
        if newstring != '':
            splitnewstring = newstring.split()
            for x in splitnewstring:
                result = re.match('[0-9]{3}',x)
                if result == None:
                    x = ''
                else:
                    finalstring = finalstring + x + '-'
        if finalstring != '':
            newname = newname + '[' + finalstring[:-1] + ']'
        
        #Format remaining words against giant string
        splitnewname = newname.split()
        for i in splitnewname:
            upperi = i.upper()
            if upperi.find('[') > 0:
                i = (upperi[upperi.find('['):])
            if len(upperi) > 1 and (giantstring.find(upperi)) > -1:
                i = ''
            finalname = finalname + i + ' '
        
        #Final string formatting
        name = r'\\' + name
        name = name[1:]
        finalname = finalname.strip()
        finalname = finalname.replace('  ','')
        finalname = r'\\' + finalname
        finalname = finalname[1:]
        
        #Print before and after values
        print(('BEFORE - ' + path + name + '\n'))
        print(('AFTER - ' + path + finalname + '\n'))
        
        #Enable if you would like to write before and after to text file
        #f.write(('BEFORE - ' + path + name + '\n'))
        #f.write(('AFTER - ' + path + finalname + '\n'))
        
        #Enable to rename folders in the path
        #os.rename((path + name), (path+finalname))
    break
    
#Enable if text file is enabled
#f.close()