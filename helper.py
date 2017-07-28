#!/usr/bin/env python3

"""
Etude 04
Authors:
"""

import sys

_TOTAL_DISTANCE = 2413

class Can:
    _CAPACITY = 20

    def __init__(self):
        self._fuel = 0

    def fill(self, fuel: float):
        self._fuel = min(self._CAPACITY, self._fuel + fuel)

    def remove(self, amount: float) -> float:
        if amount <= self._fuel:
            self._fuel = self._fuel - amount
            return amount
        else:
            removed = self._fuel
            self._fuel = 0
            return removed

    @property
    def fuel(self):
        return self._fuel

class Vehicle:
    _CAPACITY = 60
    _KM_PER_LITRE = 12

    def __init__(self):
        self._fuel = 0
        self._position = 0
        self._cans = []

    def fill(self, amount: float):
        assert self._fuel + amount <= self._CAPACITY
        self._fuel += amount

    def move(self, distance: float):
        fuel_consumed = abs(distance) / self._KM_PER_LITRE
        assert fuel_consumed <= self._fuel
        self._fuel -= fuel_consumed
        self._position += distance

    def is_empty(self) -> bool:
        return self._fuel == 0

    @property
    def position(self):
        return self._position

class Desert:
    def __init__(self):
        self._cans = {}

    def pickup_fuel(self, position, amount) -> float:
        if position == 0:
            return amount

        assert position in self._cans
        assert amount <= sum([can.fuel for can in self._cans[position]])

        amount_to_remove = amount
        for can in cans:
            remove = min(amount_to_remove, can.fuel)
            amount_to_remove -= remove
            can.remove(remove)

    def put_can(self, position: float, can):
        if position not in self._cans:
            self._cans[position] = []
        self._cans[position].append(can)

    def pickup_cans(self, position: float, amount: float) -> list:
        assert position in self._cans
        assert amount <= sum([can.fuel for can in self._cans[position]])

        cans = []
        pass

def q1():
    d = Desert()
    v = Vehicle()
    v.fill(d.pickup_fuel(v.position, 60))
    v.move(360)
    v.move(-360)
    assert v.is_empty()
    print('Q1 passed')

def q2():
    d = Desert()
    v = Vehicle()
    v.fill(d.pickup_fuel(v.position, 60))
    v.move(_TOTAL_DISTANCE)
    assert v.position == _TOTAL_DISTANCE
    print('Q2 passed')

def q3():
    pass

def q4():
    pass

def q5():
    pass

def main():
    q1()
    q2()
    q3()
    q4()
    q5()

if __name__ == '__main__':
    main()
