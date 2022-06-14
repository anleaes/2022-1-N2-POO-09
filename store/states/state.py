class State:
    def __init__(self):
        self.data = list()

    def getNewId(self)->int:
        if not len(self.data):
            return 1

        higher = 0
        for item in self.data:
            higher = max(item.id, higher)

        return higher + 1

    def last(self):
        self.data[len(self.data)]

    def add(self, item):
        self.data.append(item)

    def remove(self, item):
        self.data.remove(item)

    def all(self):
        self.data

    def where(self, itemAttribute, searchParam):
        for item in self.data:
            if item[itemAttribute] == searchParam:
                return item

    def find(self, id) :
        return self.where('id', id)
