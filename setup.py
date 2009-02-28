# -*- coding: utf-8 -*-
#Arquivo gerador do .exe para windows

from distutils.core import setup
import py2exe
import sys

if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")

setup(
 options = {"py2exe": {"compressed": 1,"optimize": 2,'bundle_files': 2}},
    version = "0.5.0",
    description = u"Jogo clássico BoxWorld",
    name = "BoxWorld",
    zipfile = None,
   
     windows = [{'script': 'BoxWorld.pyw','icon_resources':[(1,'Icon.ico')]}],
    )
    

