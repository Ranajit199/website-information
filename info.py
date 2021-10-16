print("\033[92m")
import os
import urllib2
import sys
url = raw_input("ENTER WEBSITE NAME : ")
url.rstrip ( )
header =urllib2.urlopen (url) .info ( )
print(str (header) )
