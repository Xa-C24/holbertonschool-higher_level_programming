#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import SupportsIndex


class VerboseList(list):
    pass


class VerbosList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [item] to the list.")


class VerboseList(list):
    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] item.")


class VerboseList(list):
    def remove(self, item):
        print(f"Removed [{item}] from to the list.")
        super().remove(item)


class VerboseList(list):
    def pop(self, index: SupportsIndex = -1):
        item = self[index]
        print(f"Popped [item] from the list.")
        return super().pop(index)
