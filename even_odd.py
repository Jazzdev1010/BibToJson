import sys
def check_num(number):
    if int(number)%2 == 0:
        return "even"
    else:
        return "odd"


for num in sys.argv[1:]:
    print(f"{num}:{check_num(num)}")