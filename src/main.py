from lang.generative import generate
from lang.letter import Letter
from lang.list import List


for letter in generate(Letter):
    print(letter)


for lst in generate(List):
    print(lst)
