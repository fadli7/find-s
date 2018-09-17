# Read text line by line
with open("text.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
# print(content)

# Fix the text in list
daftar = []
for i in range(0, len(content)):
    daftar.append(content[i].split(","))
# print(daftar)

# Define class_label and jumlah_fitur
class_label = daftar[0]
fitur = daftar[1]

# Define data
datas = []
for i in range(2, len(daftar)):
    datas.append(daftar[i])
print(datas)
print()

# Define atribut
atribut_1 = []
atribut_2 = []
for data in datas:
    for i in range(0, 2):
        # for j in range(0, len(datas)):
        if data[i] in atribut_1:
            pass
        elif data[i] in atribut_2:
            pass
        else:
            if i == 0:
                atribut_1.append(data[i])
            else:
                atribut_2.append(data[i])

# Find S
training_1 = ['?', '?', '?']
training_2 = ['?', '?', '?']
i = 0
j = 0
for data in datas:
    if data[2] == class_label[0]:
        if i == 0:
            training_1 = data
            i += 1
        else:
            for k in range(0, 2):
                if training_1[k] == data[k]:
                    pass
                else:
                    training_1[k] = '?'
    else:
        if data[2] == class_label[1]:
            if j == 0:
                training_2 = data
                j += 1
            else:
                for k in range(0, 2):
                    if training_2[k] == data[k]:
                        pass
                    else:
                        training_2[k] = '?'
print(training_1)
print(training_2)

# Input Data
panjang = input("Masukkan "+ fitur[0] +  " : ")
lebar = input("Masukkan " +  fitur[1] + " : ")

data = [panjang, lebar, '']
perkiraan_1 = []
temp = ""
x = y = 0
for i in range(0, 3):
    if i == 2:
        print(perkiraan_1)
    else:
        if training_1[i] == '?':
            if data[i] in atribut_1:
                # perkiraan_1.append(training_1[2])
                # x += 1
                pass
            else:
                pass
            x += 1
        elif training_1[i] == data[i]:
            # perkiraan_1.append(training_1[2])
            x += 1

        if x == 2:
            perkiraan_1.append(training_1[2])

        if training_2[i] == '?':
            if data[i] in atribut_2:
                # perkiraan_1.append(training_2[2])
                # y += 1
                pass
            else:
                pass
            y += 1
        elif training_2[i] == data[i]:
            # perkiraan_1.append(training_2[2])
            y += 1

        if y == 2 :
            perkiraan_1.append(training_2[2])