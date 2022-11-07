
from __future__ import print_function, division


def sed(pattern, replace, source, dest):
    #Reads a source file and writes the destination file. In each line, replaces pattern with replace.



    fin = open(source, 'r')
    fout = open(dest, 'w')

    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)

    fin.close()
    fout.close()




def main():
    pattern = 'aba'
    replace = 'z'
    source ="C:/Users/andre/Desktop/text.txt"
    dest = "C:/Users/andre/Desktop/first_answer.txt"
    sed(pattern, replace, source, dest)


if __name__ == '__main__':
    main()
