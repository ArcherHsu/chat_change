#載入
def  input_file(filename):   
    lines = []
    with open(filename, 'r', encoding ='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines        

#轉換
def c_file(lines):
    arr = []
    name = None
    for line in lines:
        if line == 'Allen':
            name = 'Allen'
            continue
        elif line == 'Tom':
            name = 'Tom'
            continue    
        arr.append(name + ':' + line+'\n')
    return arr

#輸出
def out_file(file, lines):
    with open(file, 'w', encoding ='utf-8-sig') as f:
        for line in lines:
            f.write(line)

def main():
    lines = input_file('input.txt')
    lines = c_file(lines)
    out_file('output.txt', lines)


main()


