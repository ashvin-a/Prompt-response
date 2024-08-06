import json
import pandas as pd
from collections import deque
import re

class InputProcessor:
    """
    A class to process different types of inputs and perform specific actions based on the input type.

    Attributes:
    parameter (any): The input parameter to be processed, which can be a string, a JSON string, or a tuple.

    Methods:
    process(): Determines the type of input and processes it accordingly.
    is_palindrome(s): Checks if a given string is a palindrome, ignoring non-alphanumeric characters and case.
    is_json(s): Checks if a given string is a valid JSON string.
    json_to_excel(json_str): Converts a JSON string into a readable Excel file.
    shortest_transformation_sequence(beginWord, endWord, wordList): 
        Finds the length of the shortest transformation sequence from beginWord to endWord in a word list.
    """
    
    def __init__(self, parameter):
        """
        Initializes the InputProcessor with a parameter.

        Args:
        parameter (any): The input parameter to be processed.
        """
        self.parameter = parameter

    def process(self):
        """
        Determines the type of the input parameter and processes it accordingly.

        If the input is a string:
            - Checks if it is a JSON string and converts it to Excel.
            - Otherwise, checks if it is a palindrome.

        If the input is a tuple containing three elements (beginWord, endWord, wordList):
            - Finds the shortest transformation sequence from beginWord to endWord.

        Raises:
        ValueError: If the input parameter type is unsupported.
        """
        if isinstance(self.parameter, str):
            if self.is_json(self.parameter):
                self.json_to_excel(self.parameter)
            else:
                return self.is_palindrome(self.parameter)
        elif isinstance(self.parameter, tuple) and len(self.parameter) == 3:
            beginWord, endWord, wordList = self.parameter
            if all(isinstance(word, str) for word in [beginWord, endWord]) and isinstance(wordList, list):
                return self.shortest_transformation_sequence(beginWord, endWord, wordList)
        else:
            raise ValueError("Unsupported parameter type")

    def is_palindrome(self, s):
        """
        Checks if the given string is a palindrome.

        The check ignores non-alphanumeric characters and case.

        Args:
        s (str): The input string to be checked.

        Returns:
        bool: True if the string is a palindrome, False otherwise.
        """
        filtered_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return filtered_s == filtered_s[::-1]

    def is_json(self, s):
        """
        Checks if the given string is a valid JSON string.

        Args:
        s (str): The input string to be checked.

        Returns:
        bool: True if the string is valid JSON, False otherwise.
        """
        try:
            json.loads(s)
            return True
        except ValueError:
            return False

    def json_to_excel(self, json_str):
        """
        Converts a JSON string into a readable Excel file.

        The resulting Excel file is saved as 'output.xlsx'.

        Args:
        json_str (str): The JSON string to be converted.

        Raises:
        Exception: If the conversion fails.
        """
        try:
            data = json.loads(json_str)
            df = pd.DataFrame(data)
            df.to_excel("output.xlsx", index=False)
            print("JSON converted to Excel and saved as 'output.xlsx'")
        except Exception as e:
            print(f"Failed to convert JSON to Excel: {e}")

    def shortest_transformation_sequence(self, beginWord, endWord, wordList):
        """
        Finds the length of the shortest transformation sequence from beginWord to endWord.

        Only one letter can be changed at a time, and each transformed word must exist in the word list.

        Args:
        beginWord (str): The starting word.
        endWord (str): The target word.
        wordList (list): The list of available words for transformation.

        Returns:
        int: The length of the shortest transformation sequence. Returns 0 if transformation is not possible.
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])
        while queue:
            current_word, level = queue.popleft()
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + c + current_word[i+1:]
                    if next_word == endWord:
                        return level + 1
                    if next_word in word_set:
                        word_set.remove(next_word)
                        queue.append((next_word, level + 1))
        return 0

# Example usage:
# processor = InputProcessor("A man, a plan, a canal, Panama")
# print(processor.process())  # True

# processor = InputProcessor('{"name": "John", "age": 30}')
# processor.process()  # Creates output.xlsx

# processor = InputProcessor(("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
# print(processor.process())  # 5
