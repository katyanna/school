from flask import Flask
app = Flask(__name__)

import classes_keeper.database_setup
import classes_keeper.db

import classes_keeper.courses
import classes_keeper.classes
