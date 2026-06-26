import os
import redis
from flask import Flask

app = Flask(__name__)
r = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'),
    port=int(os.getenv('REDIS_PORT', 6379)),
    decode_responses=True)

@app.route('/')
def index():
    count = r.incr('hits')
    return f'방문 횟수: {count}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)