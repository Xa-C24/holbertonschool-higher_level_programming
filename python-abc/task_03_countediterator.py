#!/usr/bin/env python3
class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        return self.count

    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration


iterateur = CountedIterator([1, 2, 3, 4,])
while True:
    try:
        print(next(iterateur))
    except StopIteration:
        break

print("Nombre d'élément itérés:", iterateur.get_count())
