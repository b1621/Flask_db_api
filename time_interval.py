import time
starttime = time.time()
while True:
    print("tick")
    print(60.0 - ((time.time() - starttime) % 60.0))
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))

print('hello world')    