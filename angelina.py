def main():
    input_file = open("input.txt", "r")
    output_file = open("output.txt", "w")
    line = input_file.readline().split()
    n = int(line[0])

    w = []

    for i in range(n):
        a = []
        line = input_file.readline().split()
        for j in range(n):
            a.append(int(line[j]))
        w.append(a)
        print(a)

    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if w[i][k] < 10 ** 9 and w[k][j] < 10 ** 9:
                    w[i][j] = min(w[i][j], w[i][k] + w[k][j])



    for i in range(n):
        print(w[i])

    for i in range(n):
        output_file.write(str(' '.join([str(x) for x in w[i]])) + "\n")
    input_file.close()
    output_file.close()


if __name__ == "__main__":
    main()