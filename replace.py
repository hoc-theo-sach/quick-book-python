import sys

# python replace.py zero 0 < infile.txt > outfile.txt

def main():
    contents = sys.stdin.read()
    sys.stdout.write(contents.replace(sys.argv[1], sys.argv[2]))

main()

