def is_lucky_page(nomer_str, k):
    return k == 0 or nomer_str % k == 0

n, k = map(int, input().split())
for stranisti in range(n, 0, -1):
    if is_lucky_page(stranisti, k):
        print("YES")
        break
else:
    print("NO")
