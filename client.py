import sys
import urllib.request

f = urllib.request.urlopen( sys.argv[1] )
data = f.read()
print( data.decode('utf-8') )
