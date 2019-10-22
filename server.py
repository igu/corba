import sys
from omniORB import CORBA, PortableServer
import HelloWorld, HelloWorld__POA

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")

class Display(HelloWorld__POA.HWString):
    def echoString(self, msg):
        print msg
        return msg


ei = Display()
eo = ei._this()

print orb.object_to_string(eo)

poaManager = poa._get_the_POAManager()
poaManager.activate()
orb.run()
