with open('test.txt') as test_object:
    lines = test_object.readlines()

for line in lines:
    print(line.strip())