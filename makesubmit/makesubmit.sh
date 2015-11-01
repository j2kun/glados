#!/bin/bash

gcc -Wall submit.c -o submit
sudo cp submit /usr/bin/submit
sudo chown root /usr/bin/submit
sudo chmod 4711 /usr/bin/submit
