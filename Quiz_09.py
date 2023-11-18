class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_total_price(self, quantity):
        total_price = self.price * quantity
        return total_price

# 음료 객체 생성
Coffee = Beverage("커피", 3000)
GreenTea = Beverage("녹차", 2500)
IceTea = Beverage("아이스티", 3000)

# 주문 리스트 초기화
order_list = []

# 사용자에게 음료 선택 받기
while True:
    selected_beverage = input("주문할 음료를 선택하세요 (커피, 녹차, 아이스티 중 하나, 종료는 'exit'): ")

    if selected_beverage.lower() == 'exit':
        break

    # 선택된 음료에 따라 객체 선택
    beverage_object = None
    if selected_beverage == "커피":
        beverage_object = Coffee
    elif selected_beverage == "녹차":
        beverage_object = GreenTea
    elif selected_beverage == "아이스티":
        beverage_object = IceTea
    else:
        print("올바르지 않은 음료입니다. 다시 선택해주세요.")
        continue

    # 음료의 수량 입력 받기
    try:
        quantity = int(input(f"몇 잔의 {selected_beverage}를 주문하시겠습니까? "))
    except ValueError:
        print("올바르지 않은 수량입니다. 다시 입력해주세요.")
        continue

    # 선택된 음료와 수량을 주문 리스트에 추가
    order_list.append((beverage_object, quantity))

# 주문 내역 출력
if order_list:
    print("주문 내역:")
    for beverage, quantity in order_list:
        total_price = beverage.calculate_total_price(quantity)
        print(f"{beverage.name} {quantity}잔 주문 완료. 총 가격: {total_price}원")
else:
    print("주문이 없습니다.")
