f = open('train.nmv.txt')
classList = open('classList.txt', 'w')
instances = open('instances.txt', 'w')
test = open('prelim-nmv-noclass.txt')
testCleaned = open('test-cleaned.txt', 'w')

for line in f:
    tokens = line.split()
    classList.write(tokens.pop() + ' ')
    instances.write(' '.join(tokens) + '\n')

for line in test:
    tokens = line.split()
    dummy = tokens.pop()
    testCleaned.write(' '.join(tokens) + '\n')

f.close()
classList.close()
instances.close()
test.close()
testCleaned.close()
