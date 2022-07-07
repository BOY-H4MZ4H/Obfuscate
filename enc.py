# coding:utf-8 
#/usr/bin/python 

# KALAU KAU NGERECOD CANTUM KAN NAMA AUTHOR woi ANJENG

import sys,codecs,os
from py_compile import compile as obfus
from rich import print as prints
from rich.panel import Panel

data = []

def banner(): 
	prints(Panel("   ____  ____  ______ _    _  _____  _____       _______ ______ \n  / __ \|  _ \|  ____| |  | |/ ____|/ ____|   /\|__   __|  ____|\n | |  | | |_) | |__  | |  | | (___ | |       /  \  | |  | |__   \n | |  | |  _ <|  __| | |  | |\___ \| |      / /\ \ | |  |  __|  \n | |__| | |_) | |    | |__| |____) | |____ / ____ \| |  | |____ \n  \____/|____/|_|     \____/|_____/ \_____/_/    \_\_|  |______|\n                        AUTHOR : BOY HAMZAH\n"))
	
def obf():
	os.system("clear")
	banner()
	try:
		prints(Panel("[ CONTOH NAMA FILE ] /sdcard/folder/file.py\n[ CONTOH OUTPUT FILE ] kontol.py"))
		file = input("\nNama File : ")
		out = input("Output File : ")
		recod = open(file).read()
		for i in recod:
			data.append(ord(i))
			kontol = open(out, 'w')
			kontol.write(f"exec(''.join(chr(_) for _ in {data}))")
			kontol.close()
			obfus(out,out)
		prints(Panel(f"File Berhasil Di Compile | Nama File : {out}"))
	except:
		pass

obf()