import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file1', help='First filename (file "a")')
    parser.add_argument('--file2', help='Second filename (file "b")')
    args = parser.parse_args()

    lines_a = []
    with open(args.file1, 'r') as file_a:
        while True:
            line = file_a.readline().strip()
            if not line: #Will break on lone newline or end of file
                break
            lines_a.append(line)

    lines_b = []
    with open(args.file2, 'r') as file_b:
        while True:
            line = file_b.readline().strip()
            if not line: #Will break on lone newline or end of file
                break
            lines_b.append(line)

    with open('a_not_b.txt', 'w') as a_not_b:
        for i in lines_a:
            if i not in lines_b:
                a_not_b.write(f'{i}\n')

    with open('b_not_a.txt', 'w') as b_not_a:
        for i in lines_b:
            if i not in lines_a:
                b_not_a.write(f'{i}\n')
