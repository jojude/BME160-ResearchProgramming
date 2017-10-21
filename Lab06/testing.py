
import sys

def main():
    string = "UGGUACUU""GUUUAAAAUAAAAUAAAUGAUUUCGACPCAUUAGAUUAUGAUUUAAUUCAUAAUUACCAACCA"

    listindex = []
    i = 0
    print(sys.stdin)
    print(len(string))
    while i <= len(string):
        index = string.find("AAAAUA", i)
        if index == -1:
            break
        if index not in listindex:
            listindex.append(index)
        i += 1

    print(listindex)
    print(string.find("AAAAUA"))

main()