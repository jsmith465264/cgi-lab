#!/usr/bin/env python3
import os, json, cgi, cgitb

print("Content-type:text/html\r\n\r\n")
print("<title> Test CGI </title>")
print("<p>hello world</p>")

#q1
print(os.environ)

#2
for param in os.environ.keys():
    if (param=="QUERY_STRING"):
        print("<br>%20s" % os.environ[param])
    #3
    if (param=="HTTP_USER_AGENT"):
        print("<br>%20s<br>" % os.environ[param])

