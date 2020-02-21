def operator(t,a,b,ope):
    if ope == "+":
        return a + b
    elif ope == "-":
        return a - b
    elif ope == "*":
        return a * b
    elif ope == "/":
        return a // b
    else:
        return "error"
def changer(string):
    try:
        return int(string)
    except:
        return string
T = int(input())
for t in range(1,T+1):
    s = list(map(changer, input().split()))
    print(s)
    stack = []
    for i in s:
        if i != ".":
            if type(i) == int:
                stack.append(i)
            else:
                if len(stack) < 2:
                    print("#{} {}".format(t,"error"))
                    break
                else:
                    b = stack.pop(-1)
                    a = stack.pop(-1)
                    #ans = eval("{}{}{}".format(a,i,b))
                    stack.append(operator(t,a,b,i))
        else:
            if len(stack) == 1:
                print("#{} {}".format(t,stack[-1]))
            else :
                print("#{} {}".format(t,"error"))