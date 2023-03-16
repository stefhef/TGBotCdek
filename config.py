"""Все значения из .env файла"""
from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN = getenv("TOKEN")

# Database
FILENAME = getenv("FILENAME")
