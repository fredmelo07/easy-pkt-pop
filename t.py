#coding: utf-8
from os import system as cmd

#yt = cmd("pip list | grep youtube-dl");
p = cmd("pip --v");

if p == 0:
	print("\npip está instalado!");
else:
	print("\npip não está instalado!");
