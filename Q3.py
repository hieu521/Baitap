def stringduple(s):
    strings=""
    for string in s :
        if string not in strings:
            strings+=string
    return strings
def countstring(s):
   amountofstring = stringduple(s)
   for string in amountofstring:
        count = s.count(string)
        print(f"'{string}': {count}; ", end='')
s = input()
countstring(s)
