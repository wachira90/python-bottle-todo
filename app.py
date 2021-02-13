import sys, os, bottle

#sys.path = ['/var/www/todo/'] + sys.path
print (sys.path)
#sys.path = "d:\\dev\\dev-python\\bottle-test\\" + sys.path
os.chdir(os.path.dirname(__file__))

import todo # This loads your application

application = bottle.default_app()