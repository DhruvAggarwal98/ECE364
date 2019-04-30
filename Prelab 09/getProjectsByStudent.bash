#!/bin/bash
# ######################################################
# Author : < Your Full Name >
# email : < Your Email >
# ID : < Your course ID , e . g . ee364j20 >
# Date : < Start Date >
# ######################################################
DataPath=~ee364/DataFolder/Prelab09
name=$1
pattern=[0-9]{5}-[0-9]{5}
student_id=$(grep -E "$name" $DataPath/maps/students.dat | cut -c45-56)
grep -lr -E $student_id $DataPath/circuits/$circuit | cut -c62-68 | grep -f - $DataPath/maps/projects.dat | cut -c22-58 |sort -u
