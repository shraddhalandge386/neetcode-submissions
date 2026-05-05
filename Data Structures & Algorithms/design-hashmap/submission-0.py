class MyHashMap:

    def __init__(self):
        self.seen= {}

    def put(self, key: int, value: int) -> None:
        self.seen[key]= value

    def get(self, key: int) -> int:
        return self.seen.get(key,-1)

    def remove(self, key: int) -> None:
        if key in self.seen:
            del self.seen[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)