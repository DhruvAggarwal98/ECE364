#!/bin/bash
# ######################################################
# Author : < Your Full Name >
# email : < Your Email >
# ID : < Your course ID , e . g . ee364j20 >
# Date : < Start Date >
# ######################################################
DataPath=~ee364/DataFolder/Prelab09
id1=$1
id2=$2
count1=0
count2=0
for circuit in $(ls $DataPath/circuits)
	do
	if grep --quiet -E $id1 $DataPath/circuits/$circuit
		then	
		let "count1 = count1 + 1" 
	fi	
done
for circuit in $(ls $DataPath/circuits)
	do
	if grep --quiet -E $id2 $DataPath/circuits/$circuit
		then	
		let "count2 = count2 + 1" 
	fi	
done
if [[ count1 -gt count2 ]]
	then 
	echo $id1
	else
	echo $id2
fi
