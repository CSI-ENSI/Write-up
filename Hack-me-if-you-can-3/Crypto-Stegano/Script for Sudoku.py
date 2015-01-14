import Image
image = Image.open("map.png")
result = Image.open("map.png")
def move(row1, col1, row2, col2):
    xsize, ysize = image.size
    delta_x = xsize / 9
    delta_y = ysize / 9
    part1 = image.crop(((col1 - 1)*delta_x, (row1 - 1)*delta_y, col1*delta_x, row1*delta_y))
    result.paste(part1, ((col2 - 1)*delta_x, (row2 - 1)*delta_y, col2*delta_x, row2*delta_y))

def correct_row(list, row):
    i = 1
    for l in list:
        move(row, i, row, l)
        i += 1

correct_row([8,7,9,1,4,3,6,2,5], 1)
correct_row([6,2,4,5,7,9,3,8,1], 2)
correct_row([3,5,1,8,6,2,4,9,7], 3)

correct_row([2,6,3,7,1,4,9,5,8], 4)
correct_row([1,4,5,6,9,8,2,7,3], 5)
correct_row([7,9,8,3,2,5,1,6,4], 6)
// this is the correct sudoku

image.show()
result.show()
