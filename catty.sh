#!/bin/bash

# Start of the IP range
start=1

# End of the IP range
end=254

# The IP address base
base="10.0.141."

# Port to check
port=445

echo "Starting to check connectivity to port $port on the range 10.0.141.$start to 10.0.141.$end..."

for i in $(seq $start $end); do
    ip="$base$i"
    # Attempting to connect using netcat; no output if connection fails.
    nc -z -n -w 1 $ip $port &> /dev/null
    if [ $? -eq 0 ]; then
        echo "Connection to $ip on port $port succeeded."
    fi
done

echo "Scan complete."
