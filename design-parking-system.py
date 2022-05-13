# https://leetcode.com/problems/design-parking-system/description/
#
# Design a parking system for a parking lot. The parking lot has three kinds of
# parking spaces: big, medium, and small, with a fixed number of slots for each
# size.
#
# Implement the ParkingSystem class:
#
# ParkingSystem(int big, int medium, int small) Initializes object of the
# ParkingSystem class. The number of slots for each parking space are given as
# part of the constructor.
# bool addCar(int carType) Checks whether there is a parking space of carType
# for the car that wants to get into the parking lot. carType can be of three
# kinds: big, medium, or small, which are represented by 1, 2, and 3
# respectively. A car can only park in a parking space of its carType. If there
# is no space available, return false, else park the car in that size space and
# return true.
#
# Constraints:
# 0 <= big, medium, small <= 1000
# carType is 1, 2, or 3
# At most 1000 calls will be made to addCar

class ParkingSystem:
    BIG = 1
    MEDIUM = 2
    SMALL = 3

    def __init__(self, big: int, medium: int, small: int):
        self.lot_spaces = dict(
            [(self.BIG, big),
             (self.MEDIUM, medium),
             (self.SMALL, small)])

    def add_car(self, car_type: int) -> bool:
        if self.lot_spaces[car_type] > 0:
            self.lot_spaces[car_type] -= 1
            return True
        return False
