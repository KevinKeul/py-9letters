import random
import re
from itertools import product
from operator import sub, truediv

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas


def main():
    count = (1, 2)
    border = inch * 1.5
    pages = 3
    canvas = Canvas('9letters.pdf', pagesize=A4, bottomup=False)
    nines = [x for x in product(range(count[0]), range(count[1]))]
    words = get_words(len(nines) * pages)
    size = tuple(map(truediv, map(sub, A4, (2*border, 2*border)), count))
    for page in range(pages):
        for i, nine in enumerate(nines):
            word = words[page * count[0] * count[1] + i]
            draw_9(canvas, border + size[0] * nine[0], border + size[1] * nine[1], size, word)
        canvas.setFont('Helvetica-Bold', size[0] * 0.08)
        canvas.setFillColor('black')
        canvas.drawCentredString(border + (size[0] / 2), border + (size[1] * 1.95), str(page + 1))
        canvas.showPage()
    canvas.save()


def get_words(number_of_words):
    with open('list.txt') as input_file:
        words = input_file.readlines()
    words = [re.sub('\\W', '', word) for word in words]
    return words[:number_of_words]


def draw_9(canvas, x, y, size, text):
    width_1 = size[0] / 6
    squares = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (1, 1), (2, 1), (3, 1), (2, 2)]
    assert len(squares) == len(text), 'The given text does not fit into 9 squares: {}'.format(text)
    print(text)
    word = randomize_word(text, squares)
    canvas.setFont('Helvetica-Bold', width_1 * 0.6)
    for current, square in enumerate(squares):
        draw_letter(canvas, x + width_1 * square[0], y + width_1 * (2 - square[1]), width_1, word[current])
    draw_letter_special(canvas, x + width_1 * squares[-1][0], y + width_1 * (2 - squares[-1][1]), width_1, word[-1])
    canvas.setFont('Helvetica-Bold', width_1 * 0.05)
    canvas.setFillColor('black')
    # canvas.drawCentredString(x + width_1, y + width_1 * 3.1, text)


def randomize_word(word, squares):
    text = word.upper()
    occurrences = [[i for i in range(len(text)) if text[i] == letter] for letter in text]
    matrix = [[False for _ in squares] for _ in squares]
    for i1, square1 in enumerate(squares):
        for i2, square2 in enumerate(squares):
            if abs(square1[0] - square2[0]) + abs(square1[1] - square2[1]) == 1:
                matrix[i1][i2] = True
                matrix[i2][i1] = True
    count = 0
    while count < 10000:
        count = count + 1
        failed = False
        sequence = random.sample(range(len(text)), len(text))
        for i in range(len(text) - 1):
            for left in occurrences[i]:
                for right in occurrences[i + 1]:
                    if matrix[sequence[left]][sequence[right]]:
                        failed = True
        if failed:
            continue
        break
    result = ['0'] * len(text)
    for i, letter in enumerate(text):
        result[sequence[i]] = letter
    return ''.join(result).upper()


def draw_letter(canvas, x, y, single_width, letter):
    canvas.setFont('Helvetica-Bold', single_width * 0.6)
    canvas.setFillColor('black')
    canvas.rect(x, y, single_width, single_width)
    canvas.drawCentredString(x + single_width * 0.5, y + single_width * 0.7, letter)


def draw_letter_special(canvas, x, y, single_width, letter):
    canvas.setFont('Helvetica-Bold', single_width * 0.6)
    canvas.setFillColor('red')
    canvas.rect(x, y, single_width, single_width, fill=1)
    canvas.setFillColor('white')
    canvas.drawCentredString(x + single_width * 0.5, y + single_width * 0.7, letter)


if __name__ == "__main__":
    main()
