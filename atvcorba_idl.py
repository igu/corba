# Python stubs generated by omniidl from atvcorba.idl
# DO NOT EDIT THIS FILE!

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA


_omnipy.checkVersion(4,2, __file__, 1)

try:
    property
except NameError:
    def property(*args):
        return None


#
# Start of module "HelloWorld"
#
__name__ = "HelloWorld"
_0_HelloWorld = omniORB.openModule("HelloWorld", r"atvcorba.idl")
_0_HelloWorld__POA = omniORB.openModule("HelloWorld__POA", r"atvcorba.idl")


# interface HWString
_0_HelloWorld._d_HWString = (omniORB.tcInternal.tv_objref, "IDL:HelloWorld/HWString:1.0", "HWString")
omniORB.typeMapping["IDL:HelloWorld/HWString:1.0"] = _0_HelloWorld._d_HWString
_0_HelloWorld.HWString = omniORB.newEmptyClass()
class HWString :
    _NP_RepositoryId = _0_HelloWorld._d_HWString[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_HelloWorld.HWString = HWString
_0_HelloWorld._tc_HWString = omniORB.tcInternal.createTypeCode(_0_HelloWorld._d_HWString)
omniORB.registerType(HWString._NP_RepositoryId, _0_HelloWorld._d_HWString, _0_HelloWorld._tc_HWString)

# HWString operations and attributes
HWString._d_echoString = (((omniORB.tcInternal.tv_string,0), ), ((omniORB.tcInternal.tv_string,0), ), None)

# HWString object reference
class _objref_HWString (CORBA.Object):
    _NP_RepositoryId = HWString._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def echoString(self, *args):
        return self._obj.invoke("echoString", _0_HelloWorld.HWString._d_echoString, args)

omniORB.registerObjref(HWString._NP_RepositoryId, _objref_HWString)
_0_HelloWorld._objref_HWString = _objref_HWString
del HWString, _objref_HWString

# HWString skeleton
__name__ = "HelloWorld__POA"
class HWString (PortableServer.Servant):
    _NP_RepositoryId = _0_HelloWorld.HWString._NP_RepositoryId


    _omni_op_d = {"echoString": _0_HelloWorld.HWString._d_echoString}

HWString._omni_skeleton = HWString
_0_HelloWorld__POA.HWString = HWString
omniORB.registerSkeleton(HWString._NP_RepositoryId, HWString)
del HWString
__name__ = "HelloWorld"

#
# End of module "HelloWorld"
#
__name__ = "atvcorba_idl"

_exported_modules = ( "HelloWorld", )

# The end.
