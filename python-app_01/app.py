from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
port = os.environ.get('APP_PORT', '5000')
redis_port = os.environ.get('REDIS_PORT', '6379')
redis = Redis(host=os.environ.get('REDIS_HOST', '127.0.0.1'), port=redis_port)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return f'Hello World! I have been seen {count} times.\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
