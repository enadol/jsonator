#!python3
try:

	import subprocess
	import urllib.request
	import prelaunch #NEW
	import createtext #NEW
	import fbjson #NEW
	import jsonbuilder
	import daterobot
	import dateproofer
	import jsonrobot
	import jsonformat

	print("Launching robot...")

	subprocess.call([r'C:\\Python33\\jsonator\\redir.bat']) #or your own path

except IndexError:
	print("La jornada no ha finalizado. Matchday not finished.")

except OSError as err:
    print("OS error: {0}".format(err))

except ValueError:
    print("Could not convert data to an integer.")
    
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise