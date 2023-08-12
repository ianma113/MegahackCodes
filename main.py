import random
import string
import os
import threading
import random
import requests

print("Cargando")



print("""
""")
print("""
░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝""")
def megahackkey(length):
	s = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length))
	code = '-'.join(s[i:i + 4] for i in range(0, len(s), 6))
	return code
print("\n" + "Scripts By Ianma")
codeStr = ''
amount = int(input("\n" + "Cuanto Keys Quieres "))
for x in range(amount):
	codeStr += "MH-" + megahackkey(16).upper() + "\n"
f = open("keys.txt", "w")
print("\n" + "Finished... Check keys.txt file")
print("\n" + "Coded by Imperio Ianma")
f.write(codeStr)
input("Presiona Enter para salir...")
f.close()