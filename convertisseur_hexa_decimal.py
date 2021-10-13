values = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8": 8, "9": 9, "A": 10, "B": 11, "C":12, "D":13, "E": 14, "F":15}
def hexadecimal_to_decimal(number):
    list=[]
    number = number.upper()
    sum=0
    power=0

    for i in number:
        list.append(i)
    list.reverse()
    for i in list:
        t=values.get(i)
        sum=sum+t*16**power
        power=power+1


    return sum

print(hexadecimal_to_decimal(input("Please put a hexadecimal number : ")))