def solution(files):
    order_list = []
    for i in range(len(files)):
        check = False
        head = ""
        number = ""
        for s in files[i]:

            if check == True and s.isdigit() == False:
                break
            elif s.isalpha() or s == "-" or s == " ":
                head += s
            else:
                number += s
                check = True
        order_list.append([head.lower(),int(number),i])

    order_list.sort(key = lambda x:(x[0],x[1]))

    return [files[k] for i,j,k in order_list]


test =  ['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', "img2.JPG"]
print(solution(test))