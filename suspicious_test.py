import os
import subprocess
import base64
import socket

data = "SGVsbG8gV29ybGQ="

decoded = base64.b64decode(data)

os.system("echo Testing")

subprocess.run(["ls"])

print(decoded)
