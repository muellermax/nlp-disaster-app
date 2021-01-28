from flask import Flask
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))

app = Flask(__name__)

from myapp import run
