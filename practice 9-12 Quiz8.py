# Quiz8. 주어진 코드를 활용하여 부동산 프로그램을 작성하시오

# 출력 예제
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# 코드

# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion-year):
#         pass

#     # 매물 정보 표시
#     def show_detail(self):
#         pass





# 해답1 (나도코딩)
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
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)


houses = []

h1 = House("강남", "아파트", "매매", "10억", "2010")
h2 = House("마포", "오피스텔", "전세", "5억", "2007")
h3 = House("송파", "빌라", "월세", "500/50", "2000")

houses.append(h1)
houses.append(h2)
houses.append(h3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))            # houses 리스트 내에 몇 개가 있는지 표시
for house in houses:
    house.show_detail()




# 해답2 (나) (풀다가 막힘) (1번 보고 다시 품)

# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     # 매물 정보 표시
#     def show_detail(self):
#         print("총 3대의 매물이 있습니다.")
#         print("{0} {1} {2} {3} {4} {5}".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))



# h1 = House("강남", "아파트", "매매", "10억", "2010")
# h2 = House("마포", "오피스텔", "전세", "5억", "2007")
# h3 = House("송파", "빌라", "월세", "500/50", "2000")

# h1.show_detail()
# h2.show_detail()
# h3.show_detail()




print("\n[나도코딩 해답보고 다시 풀어봄]")

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
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

h1 = House("강남", "아파트", "매매", "10억", "2010")
h2 = House("마포", "오피스텔", "전세", "5억", "2007")
h3 = House("송파", "빌라", "월세", "500/50", "2000")

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
h1.show_detail()
h2.show_detail()
h3.show_detail()