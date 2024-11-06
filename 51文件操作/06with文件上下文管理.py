def copy(src,dest):
    with open(src,"r") as file1:
        with open(dest,'w') as file2:
            file2.write(file1.read())

if __name__ == '__main__':
    copy("file_lines.txt","hello.txt")