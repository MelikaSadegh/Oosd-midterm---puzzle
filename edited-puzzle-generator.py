import random
from tabulate import tabulate

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [['' for _ in range(width)] for _ in range(height)]

    def fill_random_letters(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == '':
                    self.grid[y][x] = random.choice('abcdefghijklmnopqrstuvwxyz')

class Fillthepuzzle:
    DIRECTIONS = ['horizontal', 'vertical', 'diagonal', 'diagonal_inverse', 'horizontal_reverse', 'vertical_reverse']

    def __init__(self, width, height, word_list):
        self.width = width
        self.height = height
        self.word_list = word_list
        self.grid = Grid(width, height)

    def _can_place_word(self, word, x, y, direction):
        if direction == 'horizontal':
            if x + len(word) > self.width:
                return False
            for i in range(len(word)):
                if self.grid.grid[y][x + i] != '' and self.grid.grid[y][x + i] != word[i]:
                    return False
            return True
        elif direction == 'vertical':
            if y + len(word) > self.height:
                return False
            for i in range(len(word)):
                if self.grid.grid[y + i][x] != '' and self.grid.grid[y + i][x] != word[i]:
                    return False
            return True
        elif direction == 'diagonal':
            if x + len(word) > self.width or y + len(word) > self.height:
                return False
            for i in range(len(word)):
                if self.grid.grid[y + i][x + i] != '' and self.grid.grid[y + i][x + i] != word[i]:
                    return False
            return True
        elif direction == 'diagonal_inverse':
            if x - len(word) < 0 or y + len(word) > self.height:
                return False
            for i in range(len(word)):
                if self.grid.grid[y + i][x - i] != '' and self.grid.grid[y + i][x - i] != word[i]:
                    return False
            return True
        elif direction == 'horizontal_reverse':
            if x - len(word) < 0:
                return False
            for i in range(len(word)):
                if self.grid.grid[y][x - i] != '' and self.grid.grid[y][x - i] != word[i]:
                    return False
            return True
        elif direction == 'vertical_reverse':
            if y - len(word) < 0:
                return False
            for i in range(len(word)):
                if self.grid.grid[y - i][x] != '' and self.grid.grid[y - i][x] != word[i]:
                    return False
            return True
        else:
            raise ValueError("Invalid direction provided.")

    def _place_word(self, word):
        tries = 100
        for _ in range(tries):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            direction = random.choice(self.DIRECTIONS)
            if self._can_place_word(word, x, y, direction):
                if direction == 'horizontal':
                    for i in range(len(word)):
                        self.grid.grid[y][x + i] = word[i]
                elif direction == 'vertical':
                    for i in range(len(word)):
                        self.grid.grid[y + i][x] = word[i]
                elif direction == 'diagonal':
                    for i in range(len(word)):
                        self.grid.grid[y + i][x + i] = word[i]
                elif direction == 'diagonal_inverse':
                    for i in range(len(word)):
                        self.grid.grid[y + i][x - i] = word[i]
                elif direction == 'horizontal_reverse':
                    for i in range(len(word)):
                        self.grid.grid[y][x - i] = word[i]
                elif direction == 'vertical_reverse':
                    for i in range(len(word)):
                        self.grid.grid[y - i][x] = word[i]
                return True
        return False

    def generate_puzzle(self):
        for word in self.word_list:
            while not self._place_word(word):
                pass

        self.grid.fill_random_letters()

    def print_puzzle(self):
        print(tabulate(self.grid.grid, tablefmt="fancy_grid"))


# Example usage
width = int(input("Enter the width of the puzzle: "))
height = int(input("Enter the height of the puzzle: "))

word_list = []
num_words = 5
for i in range(num_words):
    word = input(f"Enter word {i+1}: ").lower()
    word_list.append(word)

puzzle = Fillthepuzzle(width, height, word_list)
puzzle.generate_puzzle()
puzzle.print_puzzle()
