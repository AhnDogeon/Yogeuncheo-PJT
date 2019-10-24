import sys

sys.stdin = open("서울 법정동 주소목록.txt","r", encoding='UTF8')
sys.stdout = open("동이름.txt","w")
for i in range(494):
    line = input().split()
    if len(line)==3:
        print(line[2])
