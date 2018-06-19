#!/bin/bash

# para compilar: bash merge.sh arquivo1.csv arquivo2.csv arquivo3.csv ...

declare filename=""

for FILE1 in "$@"
do
	if [ $FILE1 == $1 ]
	then
		name=$(echo $(echo "$FILE1" | cut -d'.' -f 1) | cut -d'_' -f 1)
		filename=$(echo $name"_combined.csv")
		cat $FILE1 > $filename
	else
		tail -n +2 $FILE1 >> $filename
	fi
done