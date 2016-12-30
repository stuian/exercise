#车子数量为100
cars = 100
#一辆车的容量是4（个人）
space_in_a_car = 4
#司机数为30
drivers = 30
#乘客数为90
passengers = 90
#没有使用的车子数等于车子数减去司机数
cars_not_driven = cars - drivers
#已经使用的车子数等于司机数
cars_driven = drivers
#运载容量等于已经使用的车子乘以每辆车的容量
carpool_capacity = cars_driven * space_in_a_car
#平均每辆车的乘客等于乘客人数除以已经使用的车子数
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."