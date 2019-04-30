#!/bin/bash
# ######################################################
# Author : < Your Full Name >
# email : < Your Email >
# ID : < Your course ID , e . g . ee364j20 >
# Date : < Start Date >
# ######################################################
DataPath=~ee364/DataFolder/Prelab09
id1=$1
projects=$DataPath/maps/projects.dat
grep -E $id1 $projects | tr -s " " | cut -d " " -f2 | sort -u 
