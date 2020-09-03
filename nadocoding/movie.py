'''
사회적 거리두기에 따른 영화관 좌석 예매 시스템 만들기

1~20번까지 총 20개의 좌석으로 구성
이 때 각 열에 대해 홀수(/짝수로 끝나는 좌석에 대해서만 출력

A, B, C, D열까지 있다고 가정하기
A, C열은 홀수만, B, D는 짝수만 있다고 가정
'''

def what_seat(alphabet):
    seat_list = []
    '''
    # 평상시
    for i in range(1, 21):
        seat = alphabet + str(i)
        seat_list.append(seat)
    '''

    # by COVID 19
    odd = ["A", "C"]
    if alphabet in odd:
        for i in range(1, 11, 2):
           seat = alphabet + str(i)
           seat_list.append(seat)

    else:
        for i in range(2, 11, 2):
            seat = alphabet + str(i)
            seat_list.append(seat)
    
    return seat_list



def display_seat(seats, alphabet):
    # each row
    odd = ["A", "C"]
    if alphabet in odd:
        for i in range(0, 10):
            if i % 2 == 0:
                k = i//2
                print(seats[k], end="\t")
            else:
                print("\t", end=" ")
    else:
        for i in range(0, 10):
            if i % 2 == 1:
                k = i//2
                print(seats[k], end="\t")
            else:
                print("\t", end=" ")
    print("")



if __name__ == "__main__":
    a = what_seat("A")
    display_seat(a, "A")
    b = what_seat("B")
    display_seat(b, "B")
    c = what_seat("C")
    display_seat(c, "C")
    d = what_seat("D")
    display_seat(d, "D")