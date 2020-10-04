#!/bin/bash
int=1
while(($int<=19))
do
	pkurun g09 G$int+.gjf
	let int++
done

