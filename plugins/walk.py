
import os, sys

def walk(DIR):
    print DIR
    w = os.walk(DIR);
    while True:
        try:
            a,b,c = w.next()
            print a,b,c
        except:
            break

if __name__ == "__main__":
    walk(sys.argv[1])
