
def one(width, height, offset):
    result = [['.' for col in range(width)] for row in range(height)]
    result_str = ''
    for row in result:
        for c in row:
            result_str += c
        result_str += '\n'
    return result_str


def draw(width, align, max_width, number=1):
    height = width * 2 - 1
    max_height = max_width * 2 - 1
    if align == 'TOP':
        offset = 0
    elif align == 'BOTTOM':
        offset = 0 + max_height - height
    else:  # align == 'MIDDLE'
        offset = 0 + int((max_height - height) / 2)


if __name__ == "__main__":
    print(one(5, 9, 0))
