def read_file_line(fn):
    file = open(fn, "r")
    s = file.readline()
    return s


def read_file_lines(fn):
    file = open(fn, "r")
    s = file.readlines()
    return s


if __name__ == "__main__":
    s = read_file_line("file_line.txt")
    s = s[:len(s)-1]
    print(s)
    lst = read_file_lines("file_lines.txt")
    print(lst)
