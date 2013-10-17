#!/usr/bin/perl  -w
print "Content-type: text/html\r\n\r\n";

print "OHAI WOLRD!
<br/>
<br/>";

for ($i = 0; $i<5; $i++) {
	print $i."<br />";
}
