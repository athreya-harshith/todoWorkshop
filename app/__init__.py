"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrqb4o2qv2dcb94bmhg-a.oregon-postgres.render.com",
        database="todo_2ix6",
        user="todo_2ix6_user",
        password="WFOTroibTY5GOnYKDmxJgvxLFVuVyTBX")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
