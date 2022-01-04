def polation(x1, y1, x2, y2, x3):
    y3 = y1 + ((y2-y1) / (x2-x1)) * (x3-x1)
    return y3

def binarySearch(array, key):
    length = len(array)
    
    if length < 2:
        return [1,1]

    if key < array[0]:
        return [1,2]
    
    if key >= array[-1]:
        return [length -1, length -2]
    
    return [2,2]


if __name__ == "__main__":
    print(binarySearch([1,2,3], 0))