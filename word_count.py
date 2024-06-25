""" Reads a file and returns the number of lines, words,
and characters ­ similar to the UNIX wc utility
"""

infile = open('word_count.tst')

lines = infile.read().split("\n")

line_count = len(lines)

word_count = 0
char_count = 0

for line in lines: 
    words = line.split()

    word_count += len(words)
    char_count += len(line)

print(f"""File has {line_count} lines,
       {word_count} words, {char_count} characters""")
