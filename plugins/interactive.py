
#

def interactive(text):
    username = raw_input("username:")
    password = raw_input("password:")
    print username, password, text

if __name__ == "__main__":
    import sys
    text = sys.argv[1]
    interactive(text)
