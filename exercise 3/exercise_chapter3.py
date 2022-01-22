# excercise 3-1
# Write a function named right_justifythat takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.
def right_justify(s):
    tong_do_dai = 70
    chieu_dai_hien_tai = len(s)
    string = s
    while chieu_dai_hien_tai < tong_do_dai:
       string = " " + string
       chieu_dai_hien_tai = len(string)
    print(string)
right_justify("monty")
#excercise 3-2
#A function object is a value you can assign to a variable or pass as an argument. For example, do_twiceis a function that takes a function object as an argument and calls it twice:
def do_twice(f,e):
	f(e)
	f(e)	
def print_twice(a):
	print(a)
	print(a)
do_twice(print_twice,"spam")
def do_four(f,v):
	do_twice(f,v)
	do_twice(f,v)
do_four(print_twice,"four")
#excercise 3-3 1
#Write a function that draws a grid like the following
def lan1(a):
    a()
    a()
def lan2(a):
    lan1(a)
    lan1(a)
def in_column():
    print ('+----+----+')
def in_row():
    print ('|    |    |')
def in_rows():
    lan2(in_row)
def do_block():
    in_column()
    in_rows()
def print_block():
    lan1(do_block)
    in_column()
print_block()
#exercise 3-3 2
#Write a function that draws a similar grid with four rows and four columns
def hai_lan(b):
    b()
    b()
def bon_lan(b):
    hai_lan(b)
    hai_lan(b)
def in_hang():
    print ('+----+----+----+----+')
def in_cot():
    print ('|    |    |    |    |')
def inhangs():
    bon_lan(in_cot)
def ghep():
    in_hang()
    inhangs()
def print_block():
    hai_lan(ghep)
    hai_lan(ghep)
    in_hang()
print_block()