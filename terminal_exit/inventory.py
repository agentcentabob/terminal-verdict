"""Inventory and item helpers (minimal)."""


class Item:
    def __init__(self, name, desc=''):
        self.name = name
        self.desc = desc


class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def show(self):
        print('\nINVENTORY')
        if not self.items:
            print(' (empty)')
            return
        for i, it in enumerate(self.items, start=1):
            print(f"{i}. {it.name} - {it.desc}")
