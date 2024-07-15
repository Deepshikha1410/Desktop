#!/bin/bash

# Load the spack using the source comnmand
source /home/apps/spack/share/spack/setup-env.sh
spack load hpctoolkit

# enter the executable file name without extension
echo "Enter exe file name : "
read exe_name

# Choose the list of events from below list

echo "Event lists : "
echo "1. REALTIME"
echo "2. CPUTIME"
echo "3. perf::CACHE-MISSES"
echo "4. MEMLEAK"
echo "5. IO"

echo "Enter event numbers (space-separated): "
echo " REALTIME OR CPUTIME is mandatory"
read -r event_numbers

# check whether events enter or not
if [ -z "$event_numbers" ]; then
    echo "Error: No event numbers entered"
    exit 1
fi

# Ask the user for the tracing of script
echo "Do you want tracing in profiling"
read tracing

#  Declaration of events
declare -a events
for event_number in $event_numbers; do
    case $event_number in
        1) events+=("REALTIME");;
        2) events+=("CPUTIME");;
        3) events+=("perf::CACHE-MISSES");;
        4) events+=("MEMLEAK");;
        5) events+=("IO");;
        *) 
            echo "Error: Invalid event number: $event_number"
            echo "Please enter event numbers (1-5)"
            exit 1
            ;;
    esac
done

# Check if both REALTIME and CPUTIME are selected
if [[ "${events[]}" == *"REALTIME" && "${events[]}" == *"CPUTIME" ]]; then
    echo "Error: Cannot select both REALTIME and CPUTIME at the same time"
    exit 1
fi

event_string=""
for event in "${events[@]}"; do
    event_string+=" -e $event"
done

# Loop for tracing
if [[ $tracing == "yes" ]]; then
    ulimit -s unlimited
    hpcrun $event_string -t ./$exe_name
    echo "hpcrun $event_string -t ./$exe_name"

    hpcstruct ./hpctoolkit-$exe_name-measurements/
    hpcprof ./hpctoolkit-$exe_name-measurements/
    hpcviewer ./hpctoolkit-$exe_name-database/
   
else
    ulimit -s unlimited
    hpcrun $event_string ./$exe_name
    echo "hpcrun $event_string ./$exe_name"

    hpcstruct ./hpctoolkit-$exe_name-measurements/
    hpcprof ./hpctoolkit-$exe_name-measurements/
    hpcviewer ./hpctoolkit-$exe_name-database/
fi