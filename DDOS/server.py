# server.py
from flask import Flask, request, jsonify
import time

app = Flask(__name__)
request_logs = []

@app.route('/', methods=['GET'])
def home():
    ip = request.remote_addr
    timestamp = time.time()
    request_logs.append((ip, timestamp))

    # Rate limiting logic
    window = 10  # seconds
    limit = 20   # max 20 requests per IP in 10 seconds
    recent_requests = [log for log in request_logs if timestamp - log[1] <= window and log[0] == ip]

    if len(recent_requests) > limit:
        return jsonify({'status': 'blocked', 'reason': 'Too many requests'}), 429

    return jsonify({'status': 'ok', 'message': 'Request received'})

if __name__ == '__main__':
    app.run(port=5000)
