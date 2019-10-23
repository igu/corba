import sys
from omniORB import CORBA
import HelloWorld

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

ior = sys.argv[1]
obj = orb.string_to_object(ior)

eo = obj._narrow(HelloWorld.HWString)

if eo is None:
    print "A referencia do Objeto nao e uma Example::Echo"
    sys.exit(1)

message = "Hello World"
result = eo.echoString(message)

print "Eu enviei '%s'. \nO objeto pegou '%s'. " % (message, result)
