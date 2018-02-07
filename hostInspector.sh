#!/bin/bash

logfile="/var/log/snort/alert.csv"

tail -s 0 -n 1 -f $logfile | while read line; do
	newTime=`echo $line | cut -f 1 -d ","`
	x_anc=`echo $line | cut -f 2 -d ","`
	src=`echo $line | cut -f 3 -d ","`
	dst=`echo $line | cut -f 4 -d ","`
	doFuzzy=false

	if echo "$src" | grep -q ":" ; then
		continue
	fi
	
	printf "\n"

	# Mencari selisih waktu antara newTime (penyerangan terakhir) dan oldTime (penyerangan sebelumnya)
	oldTime=$(tac "$logfile" | awk -F, 'NR==1 {seen[$3]++; next} seen[$3] {print; quit}' | head -n 1 | cut -f 1 -d ",")
	oldTime=$(echo $oldTime | cut -f 2 -d "-")
	newTime=$(echo $newTime | cut -f 2 -d "-")
	x_frk=$(printf "%s" $(( $(date -d "$newTime" "+%s") - $(date -d "$oldTime" "+%s") )) )

	# Menentukan apakah menggunakan algoritma fuzzy atau tidak (jika x_frk lebih dari 10 menit)
	if [[ $x_frk -le 600 ]]; then
		doFuzzy=true
	else
		doFuzzy=false
	fi
	
	echo "IP Source       : "$src
	echo "IP Destination  : "$dst
	echo "Type (x_anc)    : "$x_anc
	echo "oldTime         : "$oldTime
	echo "newTime         : "$newTime
	echo "Interval (x_frk): "$x_frk
	echo "doFzzy          : "$doFuzzy
	
	# jalankan file berikut secara bg agar dapat lngsung mengecek log kembali
	./block.sh $src $dst $x_frk $x_anc $doFuzzy &
	sleep 5
done
