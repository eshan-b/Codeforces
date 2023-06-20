poly = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}

cnt = 0
for _ in range(int(input())):
    shape = input()
    cnt += poly[shape]

print(cnt)
