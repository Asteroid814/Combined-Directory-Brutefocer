import os 
import time 
import requests 
import socket 

print("This Tool will only work on LINUX distro's and don't forget to complete the requirements")
url = input(str("Enter your url:- "))
print("which tool you wana use to bruteforce the directories")
print("1.gobuster\n2.dirb\n3.feroxbuster")
tool = input("Choose From above list: ")

if tool== "1":
	a = os.system("gobuster dir --url "+url+" -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt")
	print(a)
if tool == "2":
	b = os.system("dirb "+url)
	print(b)
if tool == "3":
	c = os.system("feroxbuster -u "+url)
	print(c)
else:
	print("choose from the list")






