# string, bytes and character encoding

import sys

script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

language = open("language22.txt", encoding="utf-8")

main(language, input_encoding, error)

#command run
#  python ex22.py "utf-8" "strict"
# python ex22.py "utf-8" "ignore"
# ython ex22.py "utf-8" "replace"