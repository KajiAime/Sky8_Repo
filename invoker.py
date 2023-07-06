import subprocess

output = subprocess.check_output(['./getIpV4Addr'])
print(output)
