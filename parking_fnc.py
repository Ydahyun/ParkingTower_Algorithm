# 함수를 모아놓은 parking_fnc.py
from parking_var import menu_max_num, park_max_num, parking_list


def parking_sys():
    while True:
        main_show_window()
        main_select_fn(parking_list, park_max_num, menu_max_num)


def main_show_window():  # 기능 목록을 띄어주는 함수
    print("■" * 50)
    print("■     주차 타워 시스템     ")
    print("■" * 50)
    print("■ (1) 차량 입고           ")
    print("■ (2) 차량 출고           ")
    print("■ (3) 차량 입고정보        ")
    print("■ (4) 프로그램 종료        ")
    print("■" * 50)


def main_select_fn(parking_list, park_max_num, menu_max_num):
    menu_num = choice_menu_num(menu_max_num)  # 메뉴는 4가지

    if menu_num == 1:    # 차량입고
        car_parking(parking_list, park_max_num)
    elif menu_num == 2:  # 차량출고
        car_release(parking_list, park_max_num)
    elif menu_num == 3:  # 현재 차량입고정보
        parking_status(parking_list, park_max_num)
    elif menu_num == 4:  # 프로그램 종료
        print("프로그램 종료")
        exit()


def choice_menu_num(menu_max_num):  # 메뉴 번호를 선택하게 하는 함수
    while (True):
        menu_num = int(input("■ 번호: "))
        if (1 <= menu_num and menu_num <= menu_max_num):
            break
        else:  # 입력값이 1,2,3,4 가 아니라면 경고문을 띄운 후 다시 입력하게 함.
            print("■" * 50)
            print(f"■ Error: 1~{menu_max_num}의 값만 입력해주세요.")
    return menu_num


# 차 번호는 고유번호이기 때문에 중복될 일이 없으니
# 이미 있는 차량입니다.와 같은 경고문과 기능은 넣지 않았습니다.
def car_parking(parking_list, park_max_num):  # 메뉴 1번 기능
    d = car_parking_2(parking_list, park_max_num)  # d는
    # 반환을 True로 받으면 입고시키는 함수를 호출
    if (d == True):
        car_parking_1(parking_list, park_max_num)
    elif (d == False):
        print("경고: 더 이상 차량을 입고 할 수 없습니다.")
        print(f"최대: {park_max_num}, 현재: {park_max_num}")


def car_parking_1(parking_list, park_max_num):  # 메뉴 1-1번 입고기능
    car_num = input("■ 입고할 차량 번호: ")
    print("■" * 50)
    for i in range(park_max_num):
        if (parking_list[i] == ""):  # 주차타워에 차량이 비어있으면
            parking_list[i] = car_num  # 차를 차고지에 넣는다.
            break


def car_parking_2(parking_list, park_max_num):  # 메뉴 1-2번 꽉 차서 더 못넣는다고 알려주는 기능
    stored = 0  # 현재 차고에 몇 대가 있는지 세는 변수
    for i in range(park_max_num):
        if (parking_list[i] != ""):  # 차량이 있으면
            stored += 1              # stored에 1을 더해준다

    if (stored == park_max_num):  # 현재 주차된 차량의 수가 최대 저장량(5)이 되면 경고메세지 출력하고 False 리턴
        return False              # False를 리턴하여 경고메세지 출력

    elif (stored < park_max_num): # 주차가 가능한 상황
        return True               # True를 리턴하여 주차를 하게 한다.


def car_release(parking_list, park_max_num):
    car_num = input("■ 출고할 차량 번호: ")
    print("■" * 50)
    d = car_num in parking_list  # 지금까지 반복문으로 리스트[0]부터 리스트길이만큼 돌려서 찾고자하는게 있는지 확인했는데
    if (d == True):              # 생각해보니 in이라는 연산자로 편리하게 확인할 수 있었다.
        print(f"{car_num} 차량을 출고합니다.")
        for i in range(park_max_num):
            if (parking_list[i] == car_num):
                parking_list[i] = ""
                break
    else:
        print(f"{car_num} 차량이 존재하지 않습니다.")


def parking_status(parking_list, park_max_num):  # 메뉴 3번 기능
    for i in range(park_max_num):
        print(f"{i+1}층: {parking_list[i]}")