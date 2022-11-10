#convert number to binary
def binary(n):
    return bin(n).replace("0b", "")

#find the longest binary gap
def binary_gap(n):
    binary_number = binary(n)
    binary_gap = 0
    current_gap = 0
    for i in range(len(binary_number)):
        if binary_number[i] == '0':
            current_gap += 1
        else:
            if current_gap > binary_gap:
                binary_gap = current_gap
            current_gap = 0
    return binary_gap

if __name__ == '__main__':
    print(binary_gap(1041))