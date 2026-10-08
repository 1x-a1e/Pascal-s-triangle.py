"""
Dev: 1xa1e
Description: Creation of the algorithm to generate Pascal's triangle
Example:
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
"""

def main():
    altezza = int(input("height >> "))
    triangle = [[1]]

    for y in range(altezza):
        tmpTriangle = [1]

        for x in range(len(triangle[y]) - 1):
            tmp = triangle[y][x] + triangle[y][x + 1]
            tmpTriangle.extend([tmp])

        tmpTriangle.extend([1])
        triangle.append(tmpTriangle)

    for y in triangle:
        print(y)



if __name__ == "__main__":
    main()
