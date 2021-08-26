import matplotlib.pyplot


def sbitbin(b):
    a = int(b)
    bnr = bin(a).replace('0b', '')
    x = bnr[::-1]
    while len(x) < 16:
        x += '0'
    bnr = x[::-1]
    return bnr


def ebitbin(b):
    a = int(b)
    bnr = bin(a).replace('0b', '')
    x = bnr[::-1]
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return bnr


def main():
    inp = []
    inp = inp[:256]
    PC = []
    cycles = []
    c = 0
    ptr = 0
    Reg = ["0000000000000000", "0000000000000000", "0000000000000000", "0000000000000000", "0000000000000000",
           "0000000000000000", "0000000000000000", "0000000000000000"]
    for i in range(256):
        inp.append("0000000000000000")
    ctr = 0
    while True:
        try:
            line = input()
            inp[ctr] = line
            ctr += 1
        except EOFError:
            break

    while ptr < ctr:
        s = inp[ptr]
        l = str(s[:5])
        if l == "00000":

            if int(Reg[int(s[10:13], 2)], 2) + int(Reg[int(s[13:16], 2)], 2) > 65535:
                Reg[7] = "0000000000001000"
            else:
                Reg[7] = "0000000000000000"
                Reg[int(s[7:10], 2)] = sbitbin(int(Reg[int(s[10:13], 2)], 2) + int(Reg[int(s[13:16], 2)], 2))
            PC.append(ebitbin(ptr))
            print(
                PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
                Reg[6] + " " + Reg[7] + "\n")
            cycles.append(c)
            c += 1
            ptr += 1
            continue
        elif l == "00001":
            if int(Reg[int(s[10:13], 2)], 2) - int(Reg[int(s[13:16], 2)], 2) < 0:
                Reg[7] = "0000000000001000"
            else:
                Reg[7] = "0000000000000000"
                Reg[int(s[7:10], 2)] = sbitbin(int(Reg[int(s[10:13], 2)], 2) - int(Reg[int(s[13:16], 2)], 2))
            PC.append(ebitbin(ptr))
            print(
                PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
                Reg[6] + " " + Reg[7] + "\n")
            cycles.append(c)
            c += 1
            ptr += 1
            continue
        elif l == "00110":
            if int(Reg[int(s[10:13], 2)], 2) * int(Reg[int(s[13:16], 2)], 2) > 65535:
                Reg[7] = "0000000000001000"
            else:
                Reg[7] = "0000000000000000"
                Reg[int(s[7:10], 2)] = sbitbin(int(Reg[int(s[10:13], 2)], 2) * int(Reg[int(s[13:16], 2)], 2))
            PC.append(ebitbin(ptr))
            print(
                PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
                Reg[6] + " " + Reg[7] + "\n")
            cycles.append(c)
            c += 1
            ptr += 1
            continue
        elif l == "01010":
            Reg[7] = "0000000000000000"
            Reg[int(s[7:10], 2)] = sbitbin(int(Reg[int(s[10:13], 2)], 2) ^ int(Reg[int(s[13:16], 2)], 2))
            PC.append(ebitbin(ptr))
            print(
                PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
                Reg[6] + " " + Reg[7] + "\n")
            cycles.append(c)
            c += 1
            ptr += 1
            continue
        elif l == "01011":
            Reg[7] = "0000000000000000"
            Reg[int(s[7:10], 2)] = sbitbin(int(Reg[int(s[10:13], 2)], 2) | int(Reg[int(s[13:16], 2)], 2))
            PC.append(ebitbin(ptr))
            print(
                PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
                Reg[6] + " " + Reg[7] + "\n")
            cycles.append(c)
            c += 1
            ptr += 1
            continue
        elif l == "01100":
            Reg[7] = "0000000000000000"
            Reg[int(s[7:10], 2)] = sbitbin(int(Reg[int(s[10:13], 2)], 2) & int(Reg[int(s[13:16], 2)], 2))
            PC.append(ebitbin(ptr))
            print(
                PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
                Reg[6] + " " + Reg[7] + "\n")
            cycles.append(c)
            c += 1
            ptr += 1
            continue
        elif l == "00111":
            if int(Reg[int(s[13:16], 2)], 2) == 0:
                Reg[7] = "0000000000000000"
                PC.append(ebitbin(ptr))
                print(
                    PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[
                        5] + " " +
                    Reg[6] + " " + Reg[7] + "\n")
                cycles.append(c)
                c += 1
                ptr += 1
            else:
                Reg[0] = sbitbin(int(Reg[int(s[10:13], 2)], 2) // int(Reg[int(s[13:16], 2)], 2))
                Reg[1] = sbitbin(int(Reg[int(s[10:13], 2)], 2) % int(Reg[int(s[13:16], 2)], 2))
                Reg[7] = "0000000000000000"
                PC.append(ebitbin(ptr))
                print(
                    PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[
                        5] + " " +
                    Reg[6] + " " + Reg[7] + "\n")
                cycles.append(c)
                c += 1
                ptr += 1
            continue
        elif l == "01101":
            Reg[7] = "0000000000000000"
            Reg[int(s[10:13], 2)] = sbitbin(~ int(Reg[int(s[13:16], 2)], 2))
            PC.append(ebitbin(ptr))
            print(
                PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
                Reg[6] + " " + Reg[7] + "\n")
            cycles.append(c)
            c += 1
            ptr += 1
            continue
        elif l == "01110":
            if int(Reg[int(s[10:13], 2)], 2) > int(Reg[int(s[13:16], 2)], 2):
                Reg[7] = "0000000000000010"
                PC.append(ebitbin(ptr))
                print(
                    PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[
                        5] + " " +
                    Reg[6] + " " + Reg[7] + "\n")
                cycles.append(c)
                c += 1
                ptr += 1

            elif int(Reg[int(s[10:13], 2)], 2) < int(Reg[int(s[13:16], 2)], 2):
                Reg[7] = "0000000000000100"
                PC.append(ebitbin(ptr))
                print(
                    PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[
                        5] + " " +
                    Reg[6] + " " + Reg[7] + "\n")
                cycles.append(c)
                c += 1
                ptr += 1
            else:
                Reg[7] = "0000000000000001"
                PC.append(ebitbin(ptr))
                print(
                    PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[
                        5] + " " +
                    Reg[6] + " " + Reg[7] + "\n")
                cycles.append(c)
                c += 1
                ptr += 1
            continue
        elif l == "00011":
            Reg[int(s[10:13], 2)] = Reg[int(s[13:16], 2)]
            Reg[7] = "0000000000000000"
            PC.append(ebitbin(ptr))
            print(
                PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
                Reg[6] + " " + Reg[7] + "\n")
            cycles.append(c)
            c += 1
            ptr += 1
            continue
        elif l == "00010":
            Reg[int(s[5:8], 2)] = sbitbin(int(s[8:16], 2))
            Reg[7] = "0000000000000000"
            PC.append(ebitbin(ptr))
            print(
                PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
                Reg[6] + " " + Reg[7] + "\n")
            cycles.append(c)
            c += 1
            ptr += 1
            continue
        elif l == "01000":
            Reg[int(s[5:8], 2)] = sbitbin(int(Reg[int(s[5:8], 2)], 2) >> int(s[8:16], 2))
            Reg[7] = "0000000000000000"
            PC.append(ebitbin(ptr))
            print(
                PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
                Reg[6] + " " + Reg[7] + "\n")
            cycles.append(c)
            c += 1
            ptr += 1
            continue
        elif l == "01001":
            Reg[int(s[5:8], 2)] = sbitbin(int(Reg[int(s[5:8], 2)], 2) << int(s[8:16], 2))
            Reg[7] = "0000000000000000"
            PC.append(ebitbin(ptr))
            print(
                PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
                Reg[6] + " " + Reg[7] + "\n")
            cycles.append(c)
            c += 1
            ptr += 1
            continue
        elif l == "00101":
            inp[int(s[8:16], 2)] = Reg[int(s[5:8], 2)]
            Reg[7] = "0000000000000000"
            PC.append(ebitbin(ptr))
            print(
                PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
                Reg[6] + " " + Reg[7] + "\n")
            cycles.append(c)
            c += 1
            ptr += 1
            continue
        elif l == "00100":
            Reg[int(s[5:8], 2)] = inp[int(s[8:16], 2)]
            Reg[7] = "0000000000000000"
            PC.append(ebitbin(ptr))
            print(
                PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
                Reg[6] + " " + Reg[7] + "\n")
            cycles.append(c)
            c += 1
            ptr += 1
            continue
        elif l == "01111":
            Reg[7] = "0000000000000000"
            PC.append(ebitbin(ptr))
            print(
                PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
                Reg[6] + " " + Reg[7] + "\n")
            cycles.append(c)
            c += 1
            ptr = int(s[8:16], 2)
            continue
        elif l == "10000":
            if Reg[7] == "0000000000000100":
                Reg[7] = "0000000000000000"
                PC.append(ebitbin(ptr))
                print(
                    PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[
                        5] + " " +
                    Reg[6] + " " + Reg[7] + "\n")
                cycles.append(c)
                c += 1
                ptr = int(s[8:16], 2)
            else:
                Reg[7] = "0000000000000000"
                PC.append(ebitbin(ptr))
                print(
                    PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[
                        5] + " " +
                    Reg[6] + " " + Reg[7] + "\n")
                cycles.append(c)
                c += 1
                ptr += 1
            continue
        elif l == "10001":
            if Reg[7] == "0000000000000010":
                Reg[7] = "0000000000000000"
                PC.append(ebitbin(ptr))
                print(
                    PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[
                        5] + " " +
                    Reg[6] + " " + Reg[7] + "\n")
                cycles.append(c)
                c += 1
                ptr = int(s[8:16], 2)
            else:
                Reg[7] = "0000000000000000"
                PC.append(ebitbin(ptr))
                print(
                    PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[
                        5] + " " +
                    Reg[6] + " " + Reg[7] + "\n")
                cycles.append(c)
                c += 1
                ptr += 1
            continue
        elif l == "10010":
            if Reg[7] == "0000000000000001":
                Reg[7] = "0000000000000000"
                PC.append(ebitbin(ptr))
                print(
                    PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[
                        5] + " " +
                    Reg[6] + " " + Reg[7] + "\n")
                cycles.append(c)
                c += 1
                ptr = int(s[8:16], 2)
            else:
                Reg[7] = "0000000000000000"
                PC.append(ebitbin(ptr))
                print(
                    PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[
                        5] + " " +
                    Reg[6] + " " + Reg[7] + "\n")
                cycles.append(c)
                c += 1
                ptr += 1
            continue
        elif l == "10011":
            Reg[7] = "0000000000000000"
            PC.append(ebitbin(ptr))
            print(
                PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
                Reg[6] + " " + Reg[7] + "\n")
            cycles.append(c)
            c += 1
            ptr += 1
            continue

    for i in range(256):
        print(inp[i] + "\n")

    pc_2 = []
    for i in PC:
        pc_2.append(int(i, 2))

    matplotlib.pyplot.scatter(cycles, pc_2)
    matplotlib.pyplot.title('Mem_Address vs Cycles')
    matplotlib.pyplot.xlabel('Cycles')
    matplotlib.pyplot.ylabel('Mem_Address')
    matplotlib.pyplot.savefig('graph.png')
    matplotlib.pyplot.show()


if __name__ == "__main__":
    main()
