#!/bin/bash
int=1
while(($int<=19))
do
	~/lustre1/wlzhang/MD/g09/formchk G$int.chk
	~/lustre1/wlzhang/MD/g09/formchk G$int+.chk
	~/lustre1/wlzhang/MD/g09/formchk G$int-.chk
	let int++
done
