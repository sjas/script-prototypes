#!/bin/bash

#
# automate compilation of latex files in ktr-style
# 
# USAGE:
# * place script in same folder as the .tex file to be processed
# * adjust filename below
#

# name of the file to be compilated:
FILENAME="<insert file name here>"

pdflatex -synctex=1 -interaction=nonstopmode $FILENAME.tex
bibtex $FILENAME
makeindex $FILENAME.nlo -s nomencl.ist -o $FILENAME.nls
pdflatex -synctex=1 -interaction=nonstopmode $FILENAME.tex
pdflatex -synctex=1 -interaction=nonstopmode $FILENAME.tex
