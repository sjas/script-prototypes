#!/bin/bash
# sum up all blob sizes for a given author 
#declare -a names=("gabriel" "michael" "dmitri" "matthias" "037" "0422");
#declare -p names;
clear;
names=`echo "gabriel"; echo "michael"; echo "dmitri"; echo "matthias\|037613" ; echo "042289";`
#for i in ${names[*]}; do
for line in $(echo $names);do
    author="";
    commitsize="";
    lines="";
    #author=${names[i]};
    author=$line
    echo "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
    echo $author;
    commitsize=`git log --author="${author}" --stat | grep "java" | grep "|" | awk -F "|" '{print $2}' | awk -F " " '{print $1}' |  awk '{ SUM += $1} END { print SUM }'`; 
    #echo $commitsize;
    #lines=`git log --author="${author}" --stat  | grep "java" | grep "|" | wc -l`; 
    lines=`git shortlog -ns | grep -i ${author} | awk -F " " '{ print $1 }'|  awk '{ SUM += $1} END { print SUM }'`
    #echo $lines;
    ergebnis=$(($commitsize/$lines)); 
    echo  $ergebnis durchschnittliche aenderungen bei $lines commits... = $commitsize;
done;