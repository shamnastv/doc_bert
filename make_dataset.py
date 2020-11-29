import random

dataset = 'data/digital_music_5'
label_to_str = {1.0: '10000', 2.0: '01000', 3.0: '00100', 4.0: '00010', 5.0: '00001'}

filename = dataset + '.x.' + 'train' + '.txt'
f = open(filename, 'rb')
doc_list = []
for line in f.readlines():
    doc = line.strip().decode('latin1')
    if doc == '':
        doc = 'empty'
    if '\t' in doc:
        print('tab')
    doc_list.append(doc)

label_list = []
filename = dataset + '.y.' + 'train' + '.txt'
f = open(filename, 'r')
for line in f.readlines():
    label = float(line.strip())
    label_list.append(label_to_str[label])

if len(label_list) != len(doc_list):
    print('error')

new_data = []
for i in range(len(doc_list)):
    new_data.append(label_list[i] + '\t' + doc_list[i] + '\n')

train_file = open("data/train.tsv", "w")
dev_file = open("data/dev.tsv", "w")
train_count = 0
dev_count = 0
for i in range(len(new_data)):
    r = random.random()
    if r < .85:
        train_file.write(new_data[i])
        train_count += 1
    else:
        dev_file.write(new_data[i])
        dev_count += 1

train_file.close()
dev_file.close()

print(train_count)
print(dev_count)

# Test Data
filename = dataset + '.x.' + 'test' + '.txt'
f = open(filename, 'rb')
doc_list = []
label_list = []
for line in f.readlines():
    doc = line.strip().decode('latin1')
    if doc == '':
        doc = 'empty'
    if '\t' in doc:
        print('tab')
    doc_list.append(doc)
    label_list.append(label_to_str[1.0])

# filename = dataset + '.y.' + 'train' + '.txt'
# f = open(filename, 'r')
# for line in f.readlines():
#     label = float(line.strip())
#     label_list.append(label_to_str[label])

if len(label_list) != len(doc_list):
    print('error')

new_data = []
for i in range(len(doc_list)):
    new_data.append(label_list[i] + '\t' + doc_list[i] + '\n')

test_file = open("data/test.tsv", "w")
test_count = 0
for i in range(len(new_data)):
    test_file.write(new_data[i])
    test_count += 1

test_file.close()
print(test_count)
