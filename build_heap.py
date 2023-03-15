# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        swaps += sift_down(data, i, n)

    return swaps

def sift_down(data, i, n):
    swaps = []
    index = i
    left = 2 * i + 1
    right =  2 * i + 2

    if left < n and data[left] < data[index]:
        index = left
    if right < n and data[right] < data[index]:
        index = right
    if i != index:
        data[i], data[index] = data[index], data[i]
        swaps.append((i, index))
        swaps += sift_down(data, index, n)
    return swaps


def main():
    text = input("I or F:")
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
    elif "F" in text:
        f = input()
        test ='./tests/'
        file = test+f
        with open(file, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
            assert len(data) == n
    else:
        print("Invalid input. Please enter I or F")
        return
    swaps = build_heap(data)
    assert len(swaps) <= 4 * n
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
if __name__ == "__main__":
    main()
