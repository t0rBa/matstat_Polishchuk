B = [2, 7, 4, 6, 5, 9, 3]

min_val = min(B)
max_val = max(B)

i_min = B.index(min_val)
i_max = B.index(max_val)

start = min(i_min, i_max) + 1
end = max(i_min, i_max)

if end - start > 1:
    product = 1
    for i in range(start, end):
        product *= B[i]
    print("Добуток елементів між мінімальним і максимальним:", product)
else:
    print("Між мінімальним і максимальним елементами <= одному числу")
