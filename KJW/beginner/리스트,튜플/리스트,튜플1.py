student = [
    (90,80),
    (85,75),
    (90,100)
]
num =1
for i in student:
    print("{}번 학생의 총점은 {}점이고, 평균은 {}입니다.".format(num,sum(i),sum(i)/len(i)))
    num += 1