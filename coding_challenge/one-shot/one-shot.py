import json
import pandas as pd
from collections import deque

class InputProcessor:
    def __init__(self, input_param):
        self.input_param = input_param

    def process(self):
        if isinstance(self.input_param, str):
            return self.is_palindrome(self.input_param)
        elif isinstance(self.input_param, tuple) and len(self.input_param) == 3:
            return self.word_ladder_length(*self.input_param)
        elif self.is_json(self.input_param):
            return self.json_to_excel(self.input_param)
        else:
            raise ValueError("Invalid input type")

    def is_palindrome(self, string):
        cleaned_string = string.replace(" ", "").lower()
        return cleaned_string == cleaned_string[::-1]

    def json_to_excel(self, json_string):
        try:
            data = json.loads(json_string)
            df = pd.DataFrame(data)
            excel_filename = "output.xlsx"
            df.to_excel(excel_filename, index=False)
            return excel_filename
        except (json.JSONDecodeError, ValueError) as e:
            raise ValueError("Invalid JSON string")

    def word_ladder_length(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        queue = deque([(beginWord, 1)])
        while queue:
            current_word, length = queue.popleft()
            if current_word == endWord:
                return length

            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + c + current_word[i + 1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append((next_word, length + 1))
        return 0

    def is_json(self, string):
        try:
            json.loads(string)
            return True
        except ValueError:
            return False

# Example usage
processor = InputProcessor("Radar")
print(processor.process())  # True (palindrome)

# processor = InputProcessor({"name": "John", "age": 30})
print(processor.process())  # "output.xlsx" (Excel file generated)

processor = InputProcessor(("hot", "cog", ["hig", "dog", "log", "cog"]))
print(processor.process())  # 5 (length of shortest transformation sequence)
