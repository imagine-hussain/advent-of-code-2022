
content = open("in").readline()

for i in range(4, len(content) - 10):
    if len(set(content[i:i+14])) == 14:
        print(i, content[i:i+14])
        break

