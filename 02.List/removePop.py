# 리스트에서 element 지우기

a = [2, 3, 7, 3 ,5, 5, 3, 8]
a.remove(5)  # 순서를 지우는 게 아니라 object를 지우는 건가?

# 복수 개를 remove 하지는 못하고 하나만 지우는 구나
print(a)

# 여러 개를 지우려면 slice해서 [], empty 할당한다.
a[:2] = []
print(a)

# index로 지우려면 [], none을 할당하면 되나?
# a[0] = [ ]
# a[0] = None

# remove는 object로 지우고 pop은 index로 지우고
a.pop(0)
print(a)