
def sort_file(files):
    sum_lines = {}
    for file in files:
        with open(file, 'r', encoding='UTF-8') as f:
            for id,line in enumerate(f):
                print(f"{id} {line}", end = '')
                sum_lines.update({file : id+1})

    a = tuple(sum_lines)
    print(sum_lines)
    print(a)


file_list = ['1.txt', '2.txt', '3.txt']
sort_file(file_list)