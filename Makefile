SHELL=/bin/bash
run:
	. venv/bin/activate && python deepdreambot.py

install:
	python -m venv venv
	. venv/bin/activate && pip install discord.py python-dotenv requests
