#!/bin/bash
#uthor: Diego Montufar, Clifford Siu, Gustavo Carrion, Andres Chaves, Ilkan Ilhof
# Date: 26/04/2015
# Ver: 0.2
#
# Description: This script will check the processes status on a defined period
#              If it dies, this script will re-start it again.
#              Force this script by running as background task using "&"
#


# Define constant variables
process="python retweetbot.py"
process6h="python retweetbot6h.py"
process1d="python retweetbot1d.py"
process6helec="python retweetbot6helec.py"
interval=120
process1delec="python retweetbot1delec.py"
process1welec="python retweetbot1welec.py"
noOfProcess=1
noOfProcess6h=1
noOfProcess1d=1
currentDir=`pwd`

while true;
do


  count=`ps -fu root | grep "$process" | grep -v 'grep' | wc -l`

  # Check if there are any processes got killed
  if [ $count -lt $noOfProcess ]
  then

    for ((i = 1; i <= $noOfProcess; i++))
    do
      # Confirmed that 1 or more processes had been killed
      # Find it and restart them individually
      if [ `ps aux | grep -w "$process $i" | grep -v 'grep' | wc -l` -lt 1 ]
      then
        eval $process $i &
        dateTime=`date +"%F %T"`
        echo "$dateTime: Restarted process $i" >> $currentDir/restart.log
      fi
    done

  else

    echo "$dateTime: All OK!! Do nothing." >> $currentDir/restart.log
  fi


  count6h=`ps -fu root | grep "$process6h" | grep -v 'grep' | wc -l`

  # Check if there are any processes got killed
  if [ $count6h -lt $noOfProcess6h ]
  then

    for ((i = 1; i <= $noOfProcess6h; i++))
    do
      # Confirmed that 1 or more processes had been killed
      # Find it and restart them individually
      if [ `ps aux | grep -w "$process6h $i" | grep -v 'grep' | wc -l` -lt 1 ]
      then
        eval $process6h $i &
        dateTime=`date +"%F %T"`
        echo "$dateTime: Restarted process $i" >> $currentDir/restart.log
      fi
    done

  else

    echo "$dateTime: All OK!! Do nothing." >> $currentDir/restart.log
  fi


  count1d=`ps -fu root | grep "$process1d" | grep -v 'grep' | wc -l`

  # Check if there are any processes got killed
  if [ $count1d -lt $noOfProcess1d ]
  then

    for ((i = 1; i <= $noOfProcess1d; i++))
    do
      # Confirmed that 1 or more processes had been killed
      # Find it and restart them individually
      if [ `ps aux | grep -w "$process1d $i" | grep -v 'grep' | wc -l` -lt 1 ]
      then
        eval $process1d $i &
        dateTime=`date +"%F %T"`
        echo "$dateTime: Restarted process $i" >> $currentDir/restart.log
      fi
    done

  else

    echo "$dateTime: All OK!! Do nothing." >> $currentDir/restart.log
  fi
  
  count6helec=`ps -fu root | grep "$process6helec" | grep -v 'grep' | wc -l`

  # Check if there are any processes got killed
  if [ $count6helec -lt $noOfProcess6h ]
  then

    for ((i = 1; i <= $noOfProcess6h; i++))
    do
      # Confirmed that 1 or more processes had been killed
      # Find it and restart them individually
      if [ `ps aux | grep -w "$process6helec $i" | grep -v 'grep' | wc -l` -lt 1 ]
      then
        eval $process6helec $i &
        dateTime=`date +"%F %T"`
        echo "$dateTime: Restarted process $i" >> $currentDir/restart.log
      fi
    done

  else

    echo "$dateTime: All OK!! Do nothing." >> $currentDir/restart.log
  fi

  count1delec=`ps -fu root | grep "$process1delec" | grep -v 'grep' | wc -l`

  # Check if there are any processes got killed
  if [ $count1delec -lt $noOfProcess1d ]
  then

    for ((i = 1; i <= $noOfProcess1d; i++))
    do
      # Confirmed that 1 or more processes had been killed
      # Find it and restart them individually
      if [ `ps aux | grep -w "$process1delec $i" | grep -v 'grep' | wc -l` -lt 1 ]
      then
        eval $process1delec $i &
        dateTime=`date +"%F %T"`
        echo "$dateTime: Restarted process $i" >> $currentDir/restart.log
      fi
    done

  else

    echo "$dateTime: All OK!! Do nothing." >> $currentDir/restart.log
  fi
  
  count1welec=`ps -fu root | grep "$process1delec" | grep -v 'grep' | wc -l`

  # Check if there are any processes got killed
  if [ $count1welec -lt $noOfProcess1d ]
  then

    for ((i = 1; i <= $noOfProcess1d; i++))
    do
      # Confirmed that 1 or more processes had been killed
      # Find it and restart them individually
      if [ `ps aux | grep -w "$process1welec $i" | grep -v 'grep' | wc -l` -lt 1 ]
      then
        eval $process1welec $i &
        dateTime=`date +"%F %T"`
        echo "$dateTime: Restarted process $i" >> $currentDir/restart.log
      fi
    done

  else

    echo "$dateTime: All OK!! Do nothing." >> $currentDir/restart.log
  fi



  sleep $interval
done
