#!/bin/bash

nohup ./discord-bot/bin/python course_sniper.py > my.log 2>&1 &
echo $! > save_pid.txt
