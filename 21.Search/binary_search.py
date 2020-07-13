def binary_search(element, some_list):
    # 코드를 작성하세요.
    half = len(some_list) // 2  # 리스트 크기를 반으로 나눈 index
    while half >= 0:
        if element == some_list[half]:
            return half
        elif element < some_list[0] or element > some_list[-1]:  # 제일 처음 값 또는 마지막 값
            return None
        elif element > some_list[half]:
            half = half + ((len(some_list) - half) // 2)
        elif element < some_list[half]:
            half = half // 2
    

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))