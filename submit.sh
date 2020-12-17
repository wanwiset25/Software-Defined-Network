#!/bin/sh

NO_CLI_ARGS=2

if [ $# -ne $NO_CLI_ARGS ]
then
	echo "Incorrect CLI arguments entered"
	echo "The syntax for the shell script is ./submit.sh member1_name member2_name"
	echo "If you are working alone, then enter none for member2_name"
	echo "Exiting the submit shell script"
	exit 0
else
	echo "Member 1 of your team is : $1"
	echo "Member 2 of your team is : $2"
fi

MEMBER1=$1
MEMBER2=$2

CONTROLLER1=/home/mininet/pox/pox/misc/controller_1.py
CONTROLLER2=/home/mininet/pox/pox/misc/controller_2.py
CONTROLLER3=/home/mininet/pox/pox/misc/controller_3.py

ROUTER=/home/mininet/pox/pox/misc/router.py
SWITCH=/home/mininet/pox/pox/misc/switch.py

TOPOLOGY1=/home/mininet/mininet/custom/topology_1.py
TOPOLOGY2=/home/mininet/mininet/custom/topology_2.py
TOPOLOGY3=/home/mininet/mininet/custom/topology_3.py

REPORT=/home/mininet/report.pdf

#Checking if all the files exist or not

if test -f "$CONTROLLER1"; then 
    echo "$CONTROLLER1 found"
else
    echo "$CONTROLLER1 not found"
    echo "Exiting the submit shell script"
    exit 0
fi

if test -f "$CONTROLLER2"; then 
    echo "$CONTROLLER2 found"
else
    echo "$CONTROLLER2 not found"
    echo "Exiting the submit shell script"
    exit 0
fi

if test -f "$CONTROLLER3"; then 
    echo "$CONTROLLER3 found"
else
    echo "$CONTROLLER3 not found"
    echo "Exiting the submit shell script"
    exit 0
fi

if test -f "$ROUTER"; then 
    echo "$ROUTER found"
else
    echo "$ROUTER not found"
    echo "Exiting the submit shell script"
    exit 0
fi

if test -f "$SWITCH"; then 
    echo "$SWITCH found"
else
    echo "$SWITCH not found"
    echo "Exiting the submit shell script"
    exit 0
fi

if test -f "$TOPOLOGY1"; then 
    echo "$TOPOLOGY1 found"
else
    echo "$TOPOLOGY1 not found"
    echo "Exiting the submit shell script"
    exit 0
fi

if test -f "$TOPOLOGY2"; then 
    echo "$TOPOLOGY2 found"
else
    echo "$TOPOLOGY2 not found"
    echo "Exiting the submit shell script"
    exit 0
fi

if test -f "$TOPOLOGY3"; then 
    echo "$TOPOLOGY3 found"
else
    echo "$TOPOLOGY3 found"
    echo "Exiting the submit shell script"
    exit 0
fi

if test -f "$REPORT"; then 
    echo "$REPORT found"
else
    echo "$REPORT not found"
    echo "Exiting the submit shell script"
    exit 0
fi

echo "All the required files found."

ZIP_FILE_PREFIX="EE555_Spring_2020"

ZIP_FILE="${ZIP_FILE_PREFIX}_${MEMBER1}_${MEMBER2}.zip"

#Check if there is an existing zip file, if found, then make a backup of it with timestamp appended

if test -f "$ZIP_FILE"; then
    current_time=$(date "+%Y_%m_%d_%H_%M_%S")
    BACKUP_FILE="${ZIP_FILE_PREFIX}_${MEMBER1}_${MEMBER2}_${current_time}.zip"
    mv $ZIP_FILE $BACKUP_FILE
    echo "Found a previous submission backup file"
    echo "Made a backup file with the name $BACKUP_FILE"
    echo "Creating a new submission file"
else
    echo "No previous submission files found"
    echo "Creating a new submission file"
fi

zip $ZIP_FILE $CONTROLLER1 $CONTROLLER2 $CONTROLLER3 $ROUTER $SWITCH $TOPOLOGY1 $TOPOLOGY2 $TOPOLOGY3 $REPORT

if test -f "$ZIP_FILE"; then 
    echo "$ZIP_FILE succesfully created"
else
    echo "$ZIP_FILE creation failed"
    echo "Exiting the submit shell script"
    exit 0
fi