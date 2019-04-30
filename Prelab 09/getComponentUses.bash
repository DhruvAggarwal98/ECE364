#!/bin/bash
# ######################################################
# Author : < Your Full Name >
# email : < Your Email >
# ID : < Your course ID , e . g . ee364j20 >
# Date : < Start Date >
# ######################################################
DataPath=~ee364/DataFolder/Prelab09
id=$1
counts=0
for circuit in $(ls $DataPath/circuits)
	do
	if grep --quiet -E $id $DataPath/circuits/$circuit
		then	
		let "counts=counts+1"
	fi	
done
echo $counts
