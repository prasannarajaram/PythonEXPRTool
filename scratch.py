class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self) -> bool:
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def contents(self):
        return self.items


def rev_string(my_str) -> str:

    s = Stack()
    rev_str = ""
    for char in range(len(my_str)):
        s.push(my_str[char])
    print(s.contents())
    for char in range(s.size()):
        rev_str = rev_str + s.pop()
    return rev_str


# print(rev_string("my_str"))

a = [1,7,9,3,4,5,6]
b = [4,4,5,6,7,8,9]

for _ in b:
    a.append(_)

# remove duplicates
unique_a = []

for _ in a:
    if _ not in unique_a:
        unique_a.append(_)

print(unique_a)
