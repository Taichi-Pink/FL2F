file_path = "/Users/liuziyi/Documents/Interest/FL2F-master/_assignments/Assignment4.md"

file = open(file_path, "r")
count = 0
replacement = ""
# using the for loop
for line in file:
    line = line.strip()
    print(line)
    if (count == 2):
        line = "date: 2022-03-29T8:30:00"
    replacement = replacement + line + "\n"
    count = count + 1

file.close()
# opening the file in write mode
fout = open("/Users/liuziyi/Documents/Interest/FL2F-master/_assignments/Assignment9.md", "w")
fout.write(replacement)
fout.close()