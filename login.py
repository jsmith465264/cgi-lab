#!/usr/bin/env python3
from templates import login_page, secret_page
import cgi, os, http.cookies
import secret
#4
form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')
if (username == secret.username and password == secret.password):
    print('Set-Cookie:username = %s;' % secret.username)
    print('Set-Cookie:password = %s;' % secret.password)
cookie = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
usernameC=""
passwordC=""
if cookie.get("username"):
    usernameC = cookie.get("username").value
if cookie.get("password"):
    passwordC = cookie.get("password").value   
if (usernameC == secret.username and passwordC == secret.password):
    print(secret_page(usernameC, passwordC))
else:
    print(login_page())



