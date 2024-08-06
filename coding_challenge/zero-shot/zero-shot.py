import json
import pandas as pd
from collections import deque
from io import StringIO

class DataHandler:
    def __init__(self, param):
        self.param = param
        if isinstance(self.param, str):
            if self.is_json(self.param):
                self.convert_json_to_excel(self.param)
            else:
                self.check_palindrome(self.param)
        elif isinstance(self.param, tuple) and len(self.param) == 3:
            self.find_shortest_transformation(self.param)
        else:
            raise ValueError("Unsupported parameter type.")

    def is_json(self, string):
        try:
            json.loads(string)
            return True
        except ValueError:
            return False

    def check_palindrome(self, string):
        is_palindrome = string == string[::-1]
        print(f"'{string}' is a palindrome: {is_palindrome}")

    def convert_json_to_excel(self, json_string):
        try:
            data = json.loads(json_string)
            df = pd.DataFrame(data)
            output = StringIO()
            df.to_excel(output, index=False)
            output.seek(0)
            with open('output.xlsx', 'wb') as f:
                f.write(output.getvalue().encode())
            print("JSON data has been converted to 'output.xlsx'.")
        except json.JSONDecodeError:
            print("Invalid JSON string.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def find_shortest_transformation(self, param_tuple):
        beginWord, endWord, wordList = param_tuple
        wordList = set(wordList)
        if endWord not in wordList:
            print(f"No transformation sequence found from '{beginWord}' to '{endWord}'.")
            return

        queue = deque([(beginWord, 1)])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                print(f"Shortest transformation sequence length: {length}")
                return
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + char + word[i + 1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append((next_word, length + 1))

        print(f"No transformation sequence found from '{beginWord}' to '{endWord}'.")


# with open("coding_challenge/test_files/test_json.json","r") as f:
#     json_data = f.read()
input_data = ("hit","cog",["hot", "dot", "dog", "lot", "log", "cog", "hog", "hig", "cig"])
data = DataHandler(input_data)
# print(data)
