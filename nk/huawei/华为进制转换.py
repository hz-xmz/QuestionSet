import sys
while True:
    try:
        s = sys.stdin.readline().strip()
        print(int(s, 16))
    except:
        break


