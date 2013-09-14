#!/usr/bin/bash
## put the next line into .vimrc
#nnoremap <leader>fr :wa<cr>:!/cygdrive/c/Users/sjas/work/sap-projekt/compile-latex.sh<cr>
cd /cygdrive/c/users/sjas/work/sap-projekt/
pdflatex -synctex=1 -interaction=nonstopmode wip13_Karp_Schuberth_Ausarbeitung 
pdflatex -synctex=1 -interaction=nonstopmode wip13_Karp_Schuberth_Ausarbeitung
bibtex wip13_Karp_Schuberth_Ausarbeitung
makeindex wip13_Karp_Schuberth_Ausarbeitung.nlo -s nomencl.ist -o wip13_Karp_Schuberth_Ausarbeitung.nls
pdflatex -synctex=1 -interaction=nonstopmode wip13_Karp_Schuberth_Ausarbeitung
