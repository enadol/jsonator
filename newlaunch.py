#!python3
#from input import jornada
# just from the second round on
# import merger
# only necessary if club names are to be changed from the original
# import cleanerteams

import subprocess
import urllib.request
import newprelaunch #NEW
import newcreatetext #NEW
import newfbjson #NEW
import newjsonbuilder
import newdaterobot
import newdateproofer
import newjsonrobot
import newjsonformat

print("Launching robot...")

subprocess.call([r'C:\\Python33\\fbjsonrobot\\redir.bat'])
