class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        # MyIteratorが__next__()を実装しているのでselfをイテレータとして返す
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration()
        value = self.data[self.index]
        self.index = self.index + 1
        return value

# シーケンスの一例として文字列を渡す
itr = MyIterator("spam")
for char in itr:
    print(char, end=" ")

def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]

#ジェネレータをforループのinに添える
for char in reverse('goif'):
    print(char, end=" ")
