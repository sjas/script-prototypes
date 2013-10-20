#!/bin/bash

echo "Content-type: text/html"
echo ""
echo "<html>"
echo "	<head>"
echo "		<title>SWL Jenkins Buildserver</title>"
echo "			<title>SWL Jenkins Buildserver</title>"
echo "		<style type="text/css">"
echo "			.tg-left { text-align: left; } .tg-right { text-align: right; } .tg-center { text-align: center; }"
echo "			.tg-bf { font-weight: bold; } .tg-it { font-style: italic; }"
echo "			.tg-table-plain { border-collapse: collapse; border-spacing: 0; font-size: 100%; font: inherit; }"
echo "			.tg-table-plain td { border: 1px #555 solid; padding: 10px; vertical-align: top; }"
echo "		</style>"
echo "	</head>"
echo " 	<body>"
echo "		<center>"
echo "			<h1>SWL Jenkins Build Stats</h1>"
echo "		</center>"
echo "		<p>"
echo "		<table class="tg-table-plain">"
echo "			<tr>"
echo "		 		<th class="tg-center">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Group		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>"
echo "		 		<th class="tg-center">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LOC 		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>"
echo "		 		<th class="tg-center">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; JUnit % PASS	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>"
echo "		 		<th class="tg-center">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; JUnit Tests	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>"
echo "		 		<th class="tg-center">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; JUnit FAIL		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>"
echo "		 		<th class="tg-center">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; JUnit ERROR	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>"
echo "		   	</tr>"



### GENERATION CODE START

	#### these lines here remain for debugging purposes
	#echo "<br/> $(for i in `\find /var/lib/jenkins/jobs/ -maxdepth 1 -iregex '^.*swl.*' | sort`; \

	#### use the next line for selecting all groups
	 echo "<br/> $(arr=(/var/lib/jenkins/jobs/*) && for i in ${arr[*]}; \

		#### dont change the next lines
			do curr=`basename ${i}`;  \


					  ALL=`cat /var/lib/jenkins/jobs/${curr}/workspace/junit-overview.txt | awk '{print $2}'`;\
					 FAIL=`cat /var/lib/jenkins/jobs/${curr}/workspace/junit-overview.txt | awk '{print $4}'`;\
					ERROR=`cat /var/lib/jenkins/jobs/${curr}/workspace/junit-overview.txt | awk '{print $6}'`;\
				      PERCENT=`echo "(${ALL}-${ERROR}-${FAIL})/${ALL}*100" | bc -l | cut -c1-6`;\

					echo "  <tr class="tg-even">"; \
					echo "    <td class="tg-center">"${curr}"</td>"; \
					echo "    <td class="tg-center">$(cat /var/lib/jenkins/jobs/${curr}/workspace/linecount.txt)</td>"; \

					echo "    <td class="tg-center">${PERCENT}</td>"; \
					echo "    <td class="tg-center">${ALL}</td>"; \
					echo "    <td class="tg-center">${FAIL}</td>"; \
					echo "    <td class="tg-center">${ERROR}</td>"; \
					echo "  </tr>"; \
				done)"

### GENERATION CODE END




echo "		</table>"
echo "		<br/>"
echo "		<center>"
echo "			Page generated on $(date)"
echo "			<br/>"



###echo "		<br/>DEBUGGING STUFF BELOW HERE"
###echo "		<br/>"
###echo "		<br/> $(arr=(/var/lib/jenkins/jobs/*) && for i in ${arr[*]}; do `echo basename ${i}`; done)"



echo "			<br/>"
echo "			(c) sjas 2013"
echo "		</center>"
echo "	</body>"
echo "</html>"
