

# Original soln
# for i in range(4, len(content) - 10):
#     if len(set(content[i:i+14])) == 14:
#         print(i, content[i:i+14])
#         break

def solve(buf: str, size: int) -> int:
    return next(i + size for i in range(len(buf) - size) if len(set(buf[i:i+size])) == size)

content: str = open("in").readline()
print(solve(content, 4), solve(content, 14))

