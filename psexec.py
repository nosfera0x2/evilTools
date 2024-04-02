from pypsexec.client import Client
import sys

if len(sys.argv) < 5:
    print("Usage: script.py host username password command")
    sys.exit(1)

# Extract arguments
host = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
command = ' '.join(sys.argv[4:])

# Create a client object and connect to the remote host
client = Client(host, username=username, password=password, encrypt=False)
client.connect()

try:
    # Run the specified command
    client.create_service()
    stdout, stderr, rc = client.run_executable("cmd.exe", arguments=f"/c {command}")
    print("STDOUT:", stdout)
    print("STDERR:", stderr)
    print("Return Code:", rc)
finally:
    # Make sure to remove the created service and disconnect
    client.remove_service()
    client.disconnect()


#python psexec.py 192.168.1.2 myuser "mypassword" "echo Hello, World!"
