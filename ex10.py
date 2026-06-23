# Escape codes in strings
# 'I am 6\'2" tall.'
# "I am 6'2\" tall." 

tab_cats = "\tI'm tabbed in." # \t is some space start of the line
persion_cat = "I'm split\non a line." # \n is start a new line
backslash_cat = "I'm \\ a \\ cat" # \\ is a single backslash character

fat_cat = """
\tI'll do a list: 
\t* Cat food
\t* Fishies
\t* Catnip\n \t* Grass 
"""

print(tab_cats)
print(persion_cat)
print(backslash_cat)
print(fat_cat)

#  \\ Backslash (\)
# \' Single-quote (’)
# \" Double-quote (”)
# \a ASCII bell (BEL)
# \b ASCII backspace (BS)
# \f ASCII formfeed (FF)
# \n ASCII linefeed (LF)
# \N{name} Character named name in the Unicode database (Unicode only)
# \r Carriage return (CR)
# \t Horizontal tab (TAB)
# \uxxxx Character with 16-bit hex value xxxx
# \Uxxxxxxxx Character with 32-bit hex value xxxxxxxx
# \v ASCII vertical tab (VT)
# \000 Character with octal value 000
# \xhh Character with hex value 
# ex
print("i am a cat \a")

print("i am a cat \000")