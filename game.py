print("갤러그 게임 시작")
print("적 비행기 발생")
list_a = ["1.발사","2.오른쪽 이동","3.왼쪽 이동"]
dict_a = {"shoot": "총알 발사"}
dict_b = {"move": "오른쪽으로 이동"}
dict_c = {"move": "왼쪽으로 이동"}
def galaga(n):
    for i in range(n):
        print(list_a)
        number = int(input("숫자를 입력하세요 : "))
        if number == 1:
            print(dict_a)
        if number == 2:
            print(dict_b)
        if number == 3:
            print(dict_c)
galaga(3)