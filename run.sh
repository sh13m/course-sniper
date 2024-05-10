#!/bin/bash

# Modify to execute with your own venv
nohup ./discord-bot/bin/python course_sniper.py > my.log 2>&1 &
echo $! > save_pid.txt
