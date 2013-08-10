@echo off
REM 
REM BATCH SCRIPT TO EASILY COMPILE ASCIIDOC FILES INTO PDF'S VIA A2X
REM
REM prerequisites:
REM * windows only (at least this file here)
REM * needs an asciidoc installation through cygwin, read first link below
REM * read both links, without them this script would not exist.
REM     http://blog.rainwebs.net/2010/02/25/how-to-create-handsome-pdf-documents-without-frustration/
REM     http://weblogs.asp.net/lorenh/archive/2006/03/24/silly-batch-file-tricks-redirecting-stdout-into-an-evironment-variable-and-dp0.aspx
REM
REM
REM
REM USAGE:
REM 1. just set 'cygwin_home' to your cygwin path defined at the variables section
REM 2. place script into the folder where your .asc file resides
REM 3. run batch file with asciidoc file as argument
REM 4. final PDF will be produced as output
REM
REM CHANGES TO ORIGINAL OTHER SCRIPTS:
REM * use article, not book for latex output
REM * create pdf without revhistory
REM * refactoring so path settings are no longer grossly hard-coded:
REM     script takes asciidoc file name as parameter
REM * this file is standalone and needs no special a2x.conf settings
REM
REM A FEW WARNING WORDS:
REM     dont even think about messing around here with quotations, firing up other consoles, or even shell types.
REM         down these paths lies pure madness.





REM set this path accordingly
set cygwin_home=C:\cygwin






REM start dirty non-threadsafe hackery
SETLOCAL
    
    REM next line converts C:\Users\user\... to /cygdrive/c/Users/user...
    REM results are pseudo-piped through a tempfile.
    REM could be done with 'FOR /F ...' as well?
    REM well, you have been warned already above.

    cygpath -u %CD% > temp.txt
    set /p local_filepath= < temp.txt
    del temp.txt

REM changing the next line will break the script
ENDLOCAL & set proper_filepath=%local_filepath%

REM only needed output here is the one of a2x
@echo on
%cygwin_home%\bin\bash --login -i -c "cd %proper_filepath%; a2x -v -f pdf -L --asciidoc-opts='-a lang=de -v -b docbook -d article' --dblatex-opts='-V -T db2latex -P "latex.output.revhistory=0"' %1"
@echo off



REM //EOF

REM THIS IS THE CODE I USED FROM THE LINK NAMED IN THE HEADER
REM
REM @echo off
REM C:
REM chdir C:\cygwin\bin
REM bash --login -i -c "cd /cygdrive/c/asciidoc;a2x -v -f pdf -L --asciidoc-opts='-a lang=en -v -b docbook -d book' --dblatex-opts='-V -T db2latex' test.txt"
REM pause

REM THIS IS JUST FOR ENTERTAINING PURPOSES MAKING ALL THE SWEAT WORTHWHILE SOME DAY
REM assign the variable 'var':
REM     * all parameters
REM     * just the filename. there are other characters available for different choices.
REM     * full path of current working dir and first argument
REM         %0 would be the filename of the calling file (i.e. this one here) itself
REM     * just the path of the current working dir
REM set var=%*
REM set var=%~f1
REM set var=%CD%\%*
REM set var=%CD%

REM use this for proper expanding of !..! variables,
REM instead of using fast expanding %..% ones.
REM SETLOCAL EnableDelayedExpansion
