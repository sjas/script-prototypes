#!/bin/bash



echo "Content-type: text/html"
echo ""
echo "<html>"
echo "	<head>"
echo "		<title>SWL Jenkins Buildserver</title>"
echo "		<link rel="stylesheet" type="text/css" href="/style.css" />"
echo " 		<meta http-equiv="refresh" content="10" />"
echo "	</head>"
echo " 	<body>"
echo "			<h1>SWL Jenkins Build Stats</h1>"
echo "		<p>"


# <body style="background-color: #e4e9ee;">
#    <div style="position: fixed; top: 95%; left: 95%;">
#      <div style="position: absolute; top: -200px; left: -200px;">
#	<img src="uniba-logo.png"/>
#      </div>
#    </div>
#    <div style="position: fixed; top: 50%; left: 50%; display: table-cell; vertical-align: middle;">
#      <div style="position: absolute; top: -31px; left: -88px; font-size: xx-small; text-align: right;">
#	  <a href="http://www.uni-bamberg.de/swt/">
#	    <!--image size = 176x63-->
#	    <img src="logo.png" alt="Logo" border="0"/><br/><br/>
#	    Click here to continue...
#	  </a>
#      </div>
#    </div>
#  </body>



echo "		<table class="tg-table-plain">"
echo "			<tr>"
echo "		 		<th class="tg-center">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Group		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>"
echo "		 		<th class="tg-center">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LOC 		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>"
echo "		 		<th class="tg-center">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; JUnit % PASS	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>"
echo "		 		<th class="tg-center">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; JUnit Tests	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>"
echo "		 		<th class="tg-center">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; JUnit FAIL		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>"
echo "		 		<th class="tg-center">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; JUnit ERROR	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>"
echo "		 		<th class="tg-center">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Tests run on	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>"
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
					echo "    <td class="tg-center"><a href="http://buildsrv1.others.swt.wiai.uni-bamberg.de:8080/job/${curr}">${curr}</a></td>"; \
					echo "    <td class="tg-center">$(cat /var/lib/jenkins/jobs/${curr}/workspace/linecount.txt)</td>"; \

					echo "    <td class="tg-center">${PERCENT}</td>"; \
					echo "    <td class="tg-center">${ALL}</td>"; \
					echo "    <td class="tg-center">${FAIL}</td>"; \
					echo "    <td class="tg-center">${ERROR}</td>"; \
					echo "    <td class="tg-center">$(grep timestamp /var/lib/jenkins/jobs/${curr}/lastStable/* | head -n1 | cut -d":" -f2-3 | sed -e "s/T/ /g")</td>"; \
					echo "  </tr>"; \
				done)"

### GENERATION CODE END




echo "		</table>"
echo "		<br/>"
echo "		<br/>"
echo "		<br/>"
echo "			<table>"
echo "			  <tbody>"
echo "			    <tr>"
echo "			      <td class="tg-bf">LOC</td>"
echo "			      <td> - Lines of code </td>"
echo "			    </tr>"
echo "			    <tr>"
echo "			      <td class="tg-bf">JUnit % PASS</td>"
echo "			      <td> - Percentage of unit tests passing, calculated: (Tests - FAIL - ERROR) / Tests </td>"
echo "			    </tr>"
echo "			    <tr>"
echo "			      <td class="tg-bf">JUnit Tests</td>"
echo "			      <td> - Amount of JUnit tests present. </td>"
echo "			    </tr>"
echo "			    <tr>"
echo "			      <td class="tg-bf">JUnit FAIL</td>"
echo "			      <td> - Amount of JUnit tests failing assertions, source code not fulfilling test requirements. </td>"
echo "			    </tr>"
echo "			    <tr>"
echo "			      <td class="tg-bf">JUnit ERROR</td>"
echo "			      <td> - Amount of JUnit test finishing with exceptions thrown. </td>"
echo "			    </tr>"
echo "			    <tr>"
echo "			      <td class="tg-bf">Tests run on</td>"
echo "			      <td> - Time of the last successful build. </td>"
echo "			  </tbody>"
echo "			</table>"
echo "			<table>"
echo "			<br/>"
echo "		<br/>"
echo "			Page generated on $(date --rfc-3339=seconds | cut -c1-19)"
echo "			<br/>"



###echo "		<br/>DEBUGGING STUFF BELOW HERE"
###echo "		<br/>"
###echo "		<br/> $(arr=(/var/lib/jenkins/jobs/*) && for i in ${arr[*]}; do `echo basename ${i}`; done)"



echo "			<br/>"
echo "	</body>"
echo "</html>"
