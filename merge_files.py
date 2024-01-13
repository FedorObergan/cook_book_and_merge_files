files = ['1.txt', '2.txt', '3.txt']
files_content = {}
for file in files:
    with open(file, encoding = 'utf-8') as f:
        lines = f.readlines()
        lines[-1] += '\n'
        files_content[file] = [f'{file}\n', f'{len(lines)}\n'] + lines
sort_files_content = sorted(list(files_content.values()),
                            key = lambda file: len(file))

with open('result.txt', 'w', encoding = 'utf-8') as f:
    for lines in sort_files_content:
        f.writelines(lines)