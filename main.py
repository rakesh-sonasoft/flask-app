from flask import Flask
from datetime import datetime

# Redis Python Client
# https://github.com/andymccurdy/redis-py
import redis

application = Flask(__name__)



@application.route("/", methods=['POST'])
def hello():
    redis_key = 'visit_number'
    visit_number = 1

    return "<h1 style='color:blue'>Hello There! This is your visit #{0}</h1>".format(visit_number)

if __name__ == '__main__':
    application.run(host='0.0.0.0',debug=True,port=5000)
