import csv
import re
import sys

csv.field_size_limit(sys.maxsize)

initial_data = []
pre_clean_data = []
clean_data = []
textFile = open('Our_initial_incorrect_data_kholakagojbd_33.txt', 'w', encoding='utf-8')
textFile1 = open('Our_all_clean_data_kholakagojbd_33.txt', 'w', encoding='utf-8')
textFile2 = open('Our_unique_clean_data_kholakagojbd_33.txt', 'w', encoding='utf-8')

with open('All_News_kholakagojbd_33.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    c = 0
    for line in csv_reader:
        # All words of corpus
        try:
            c += 1
            word = line[1].split()
            for i in word:
                textFile.write(i)
                textFile.write('\n')
                initial_data.append(i)
        except:
            print(1)
# print(initial_data)

for i in initial_data:
    long_text = re.sub(pattern="[! !! >> \" \" \" - । ৷ # ## ‍ ‌, ' ' ‘ , ’’ , ' ' ' ‘‘ ‘ ’ ’ ’ ’ ’ “ ”  ( ) + . , “ / : ) - - – – – — ; ► › … • * X x ॥ ? "
        "\[, \],।, � # _ ا % &, @ ¬ ৷  ø Ñ – ‘ ¤ œ, ^, • · < = ö Õ ` … ª | ¦ ¯ ‹ Ô ú,̄ آ أ إ ॥"
        "— Í‚ ¿ ƒ Ÿ ™ £ ´š › æ è ® ñ ¥ Ð ° ' । ; ¯ ॥ ¬ } ৷ © ‡ × ¨… ª ~ `Î Ó Ì Ö | › „ Ä ¶ Í û Ü ú"
        "³ ÿ ø ˃ ‰ ð ô Ø { ‹ ¸ Ò Ô à ¾ § ° € Ÿ ̄ ®  ² ¹ £ « Œ ˆ ˜ † ï ÷ ˂  ¢ ´ ৻ μ è ñ ․̈ º ‒ ‑ Š Â ß ✔ 😰"
        "। _ – ৷ $ ï = | … — < “ ` √ ° × • ﴿ ʿ ī ô ³ ˃ ¯ ø ˂ ̈ ̧  π ، ॥ ● ❏ ★ ― ¦ · ■ − Ð › ¸ ✊ è ⭕ ✔ ² Ḥ]",repl="\n", string=i)
    text = long_text.split("\n")
    for j in text:
        pre_clean_data.append(j)


pattern = r"[অ-ঔ ক-হ ১-৯]"

for i in pre_clean_data:
    if re.match(pattern, i):
       clean_data.append(i)
       textFile1.write(i)
       textFile1.write('\n')


Unique_data = set(clean_data)
Unique_data = list(Unique_data)
Unique_data.sort()


for i in Unique_data:
    if re.match(pattern, i):
       textFile2.write(i)
       textFile2.write('\n')

print("Total Number of Contents = " + str(c))
print("initial_data =  " + str(len(initial_data)))
print("pre_clean_data =  " + str(len(pre_clean_data)))
print("Unique_clean_data =  " + str(len(Unique_data)))
