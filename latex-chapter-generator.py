#!/usr/bin/python
#
# SCRIPT TO GENERATE LATEX CHAPTER/SECTION/SUBSECTION FILES
#
#   this is very basic and lacks proper error checking of arguments!
#   stick to the given parameter order and be fine...
#
#
# USAGE:
#   $ ./latex-chapter-generator.py [-c -s -ss -p -sp]+ --id <id> -n <name>
#
# PARAMETERS:
#   -c          generate chapter
#   -s          generate section
#   -ss         generate subsection
#   -p          generate paragraph
#   -sp         generate subparagraph
#   --id <id>   id prefix of the filename to have the files ordered (01, 02, ...)
#   -n <name>   name of file/chapter to create
#
# TODO:
#   - fix auto-id if no ID parameter was passed
#
#================================================================================

from sys import argv
import sys

type=''
name=''
file_id=''

# exit if arguments are missing
if (len(argv) < 4):
    sys.exit('\n\tERROR: Parameters missing... exiting!\n')

# else get parameters
if (len(argv) > 2):
    for i in range(len(argv)):
        if argv[i] == '--id':
            file_id = argv[i+1]
        if argv[i] == '-n':
            name = argv[i+1]
        if argv[i] == '-c':
            type = 'chapter'
        if argv[i] == '-s':
            type = 'section'
        if argv[i] == '-ss':
            type = 'subsection'
        if argv[i] == '-p':
            type = 'paragraph'
        if argv[i] == '-sp':
            type = 'subparagraph'

clean_name  = ''.join(name.split()).lower()

chapter_type    = '\\'
chapter_type   += type
chapter_type   += '{'
chapter_type   += name
chapter_type   += '}\n'
label           = '\\label{_'
label          += clean_name
label          += '}\n\n'

filecontent = chapter_type + label

output_file_name  = file_id
output_file_name += '0'
output_file_name += clean_name
output_file_name +='.tex'

outputfile = open(output_file_name, 'w')
outputfile.write(filecontent)
outputfile.close()
