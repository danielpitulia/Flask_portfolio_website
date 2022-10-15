#!/bin/bash
# This shell script sends an e-mail to me when someone uses my contact form. The contact form creates a file called contactfile + today's date, so this script
# checks if such a file exists, sends an e-mail if true and then removes the file.
# Date: 2022-10-15

date_today=$(date +%d)
filename="contactfile_"
filename+=$date_today
filename+=".txt"
if [ -f $filename ];
then
	sendmail daniel@dpitulia.com < $filename
	rm $filename
fi
