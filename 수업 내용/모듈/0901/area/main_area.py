import area3

area3.print_area(10, 20)
area3.print_area(20, 30)

for i in range(11, 15):
    area3.print_area(i, 20)

print("가로 30 세로 10인 사각형의 넓이 : ", area3.box_area(30, 10))
print(area3.__name__)