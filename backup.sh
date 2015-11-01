#!/bin/bash

mkdir -p backups
rm backups/backup*.tar.gz
now=`date +"%m-%d-%y"`
file="backup.$now.tar.gz"
tar czvf $file --exclude='backups/*' ~/*
mv $file backups
