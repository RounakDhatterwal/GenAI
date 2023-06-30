def append_in_middle(s1, s2):
    mid_index = len(s1) // 2
    s3 = s1[:mid_index] + s2 + s1[mid_index:]
    return s3

s1 = "Hello"
s2 = "World"

s3 = append_in_middle(s1, s2)

print(s3)
