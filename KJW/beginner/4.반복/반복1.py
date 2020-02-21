studnet = [88,30,61,55,95]
count =1
for i in studnet:
    if i>=60:
        print("{}번 학생은 {}점으로 합격입니다".format(count,i))
    else:
        print("{}번 학생은 {}점으로 불합격입니다".format(count,i))
    count += 1