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

