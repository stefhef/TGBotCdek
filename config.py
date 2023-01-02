"""Все значения из .env файла"""
from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN = getenv("TOKEN")

# Database
HOST = getenv("HOST")
PORT = getenv("PORT")
USER = getenv("USER")
PASSWORD = getenv("PASSWORD")
DATABASE = getenv("DATABASE")
