import time, requests, pyfiglet, threading
print(pyfiglet.figlet_format("KINGMAN"))

msg = input("@everyone .arryb : ")
webhook = input("https://discord.com/api/webhooks/1335815509157089322/Fz68dqoS3S6-CVT-gXE3scQg7GtoF3ZMwXSrXOt1XF6Idkr5RQ8_2xzZTkCzVpkWW4rp: ")
th = int(input('200 ? (200 recommended): '))
sleep = int(input("2 ? (recommended 2): "))
def spam():
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent MSG {msg}")
        except:
            print("Bad Webhook :" + webhook)
        time.sleep(sleep)
    
for x in range(th):
    t = threading.Thread(target = spam)
    t.start()
