# Course Sniper

Discord bot to aid in getting into courses that are full at the start of the term at the University of Waterloo. Major features include:

- Realtime opening detection and notification
- Multiple selections
- More to come (maybe)

## Usage

To start, clone [this repo](https://github.com/sh13m/course-sniper)

```shell
git clone https://github.com/sh13m/course-sniper
cd course-sniper
```

Create a venv for the discord bot
```shell
python -m venv discord-bot
```

Install required dependencies in the venv

```shell
./discord-bot/bin/pip install -r requirements.txt 
```

Run `run.sh` to start the bot, output will be passed to the `my.log` file

```shell
bash run.sh
```

Run `stop.sh` to stop the bot

```shell
bash stop.sh
```

## Basic Configuration

Make sure to have environment variables for the discord bot Token, the server notification channel ID and the user ID of yourself. Currently, courses are selected by modifying the variables in `course_sniper.py`. Be aware that the `SECTION` values don't match up the actual section of the course, but rather the row of the table on the course catalogue website.

I will most likely change this in the future to be more user friendly if I ever stop being lazy and get to it.

