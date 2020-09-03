'''
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년
'''

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print("위치 :", self.location, sep='\t\t')
        print("주거 형태 :",self.house_type, sep='\t')
        print("계약 조건 :", self.deal_type, sep='\t')
        print("가격 :",self.price, sep='\t\t')
        print("계약 종료 :\t",self.completion_year,"년",sep="")

gangnam = House("강남", "아파트", "매매", "10억", 2010)
gangnam.show_detail()
mapo = House("마포", "오피스텔", "전세", "5억", 2007)
mapo.show_detail()
songpa = House("송파", "빌라", "월세", "500/50", 2000)
songpa.show_detail()

