# 创建一个tire树用于前缀匹配
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
