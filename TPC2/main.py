import sys

if __name__ == '__main__':

    line = sys.stdin.read().lower()
    switch = True
    n = ""
    r = 0

    for i in range(0, len(line)):

        if line[i].isdigit() and switch:
            n += line[i]
        elif switch and n != "":
            r += int(n)
            n = ""
            
        if line[i] == "=":
            print("Result: " + str(r))
            r = 0
        elif line[i:].startswith("on"):
            switch = True
        elif line[i:].startswith("off"):
            switch = False