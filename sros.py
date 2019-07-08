 #!/usr/bin/env python

import sys
import distro

class System:
    
    operating_systems = {
        "linux": "Linux",
        "win32": "Windows",
        "cygwin": "Cygwin",
        "darwin": "MacOSX"
        }
    
    os = operating_systems[sys.platform]
    distribution = distro.id()
    
    def isSupported(self):
        try:
            out = {
                "response": None,
                "error": None
            }
            
            if sys.platform.startswith('linux'):
                out["error"] = "Linux is supported"
                out["response"] = True
                
            elif sys.platform.startswith('win32'):
                out["error"] = "Windows is not supported yet"
                out["response"] = False
                
            elif sys.platform.startswith('cygwin'):
                out["error"] = "Cygwin is not supported yet."
                out["response"] = False
                
            elif sys.platform.startswith('darwin'):
                out["error"] = "MacOSX is not supported yet"
                out["response"] = False
            
            else:
                out["error"] = sys.platform + ": Unknown OS not supported"
                out["response"] = False
                
            return(out)
        except:
            print("Operating System is invalid")
    
    
    
system = System()

print(system.isSupported()["response"])
