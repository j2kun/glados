#!/bin/bash

mkdir -p submissions/$1
touch submissions/__init__.py
touch submissions/$1/__init__.py
echo $1 >> open-assignments.txt
