
def sort_file(files):
    sum_lines = {}
    for file in files:
        with open(file, 'r', encoding='UTF-8') as f:
            for id,line in enumerate(f):
                sum_lines.update({file : id+1})

    a = list(sum_lines.items())
    a.sort(key=lambda p: p[1])
    for pair in a:
        with open('res.txt', 'a', encoding='UTF-8') as t:
            t.write('\n' + pair[0] + '\n')
            t.write(str(pair[1]) + '\n')
        with open(pair[0], 'r', encoding='UTF-8') as e:
            for line in e:
                with open('res.txt', 'a', encoding='UTF-8') as r:
                    r.write(line)




file_list = ['1.txt', '2.txt', '3.txt']
sort_file(file_list)
