cubes = int(input())
height = 0
row = 0

while cubes >= 0:
    height += 1  # iter
    row += height
    cubes -= row

if cubes < 0:
    height -= 1

print(height)
