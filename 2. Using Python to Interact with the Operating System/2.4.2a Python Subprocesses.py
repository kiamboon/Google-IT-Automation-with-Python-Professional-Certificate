'''
2.4.2 Python Subprocesses
'''

"""Running System Commands in Python"""
import subprocess
print(subprocess.run(["date"]))
print(subprocess.run(["sleep", "2"]))


# -----------------------------------------------------------------------------------------

 """Obtaining the Output of a System Command"""
# The "host" command converts a host name to an IP address and vice versa
# Stores the result in a variable by passing the capture_output=True so that the result can be accessed
result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)
# OUTPUT: b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'
# b' indicates that the output is an array of bytes
print(result.stdout)
# Decode function applies an encoding to transform the bytes into a string
# It uses a UTF-8 encoding by default
print(result.stdout.decode().split())

# Executes the rm command to remove file that doesn't exist
result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)
# stdout prints empty value since there is an error
print(result.stdout)
# stderr prints error value as the value can be accessed through the stderr attribute
print(result.stderr)


# -----------------------------------------------------------------------------------------

"""Advanced Subprocess Management"""
# The copy method creates a new dictionary that can be changed as needed without modifying the original environment
my_env = os.environ.copy()
# The path variable indicates where the operating system will look for the executable programs
# Joins /opt/myapp and the old value of the path variable to the path separator
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])
# Calls the myapp command, setting the end parameter to the new environment
result = subprocess.run(["myapp"], env=my_env)