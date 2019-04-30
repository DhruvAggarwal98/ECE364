#!/bin/bash
# ######################################################
# Author : < Your Full Name >
# email : < Your Email >
# ID : < Your course ID , e . g . ee364j20 >
# Date : < Start Date >
# ######################################################
DataPath=~ee364/DataFolder/Prelab09
proj=$1
projects=$DataPath/maps/projects.dat
list_ids=$(grep -E $proj $projects | tr -s " " | cut -d " " -f2 | sort -u)
for circuit in $list_ids
	do
	list2=$(grep -E [0-9]{5}-[0-9]{5} $DataPath/circuits/circuit_$circuit.dat)
	list3="$list3 $list2"
done
for student_id in $list3
	do
	grep -E $student_id $DataPath/maps/students.dat | tr -s " " | cut -d " " -f2,1
done | sort -u
