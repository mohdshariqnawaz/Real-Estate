import sys

def usage(sys_argv):
    sys.stderr.write("Usage: {} text_file.txt index_file.txt\n".format(
        sys_argv[0]))

def main():
    if len(sys.argv) != 3:
        usage(sys.argv)
        sys.exit(1)


print(len(sys.argv))

main()
