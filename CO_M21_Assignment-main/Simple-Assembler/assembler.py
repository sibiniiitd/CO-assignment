D1 = {'add': '00000', 'sub': '00001', 'move immediate': '00010', 'move register': '00011',
      'ld': '00100', 'st': '00101', 'mul': '00110', 'div': '00111', 'rs': '01000', 'ls': '01001',
      'xor': '01010', 'or': '01011', 'and': '01100', 'not': '01101', 'cmp': '01110', 'jmp': '01111',
      'jlt': '10000', 'jgt': '10001', 'je': '10010', 'hlt': '10011'}
D2 = {'R0': '000', 'R1': '001', 'R2': '010', 'R3': '011', 'R4': '100', 'R5': '101', 'R6': '110', 'FLAGS': '111'}
all_op = ['add','sub','mov','ld','st','mul','div','rs','ls','xor','or','and','not','cmp','jmp','jlt','jgt','je','hlt']
TypeA = ['add', 'sub', 'mul', 'xor', 'or', 'and']
TypeB = ['mov', 'rs', 'ls']
TypeC = ['mov', 'div', 'not', 'cmp']
TypeD = ['ld', 'st']
TypeE = ['jmp', 'jlt', 'jgt', 'je']
TypeF = ['hlt']

lst1 = []
lst2 = []
lst3 = []
lable_address = {}



def ans(lst2):
    for i in lst2:

        if i[0] in TypeA:
            print(D1[i[0]] + '00' + D2[i[1]] + D2[i[2]] + D2[i[3]])
        elif i[0] in TypeB and i[2][0] == "$":
            a = i[2][1:]
            n = int(a)
            a = format(n, '08b')
            s = str(a)
            if i[0] == 'mov':
                print(D1['move immediate'] + D2[i[1]] + s)
            else:
                print(D1[i[0]] + D2[i[1]] + s)
        elif i[0] in TypeC:
            if i[0] == 'mov':
                print(D1['move register'] + "00000" + D2[i[1]] + D2[i[2]])
            else:
                print(D1[i[0]] + "00000" + D2[i[1]] + D2[i[2]])
        elif i[0] in TypeD:
            a = lst1.index(i[2]) + len(lst2)
            b = format(a, '08b')
            s = str(b)
            print(D1[i[0]] + D2[i[1]] + s)
        elif i[0] in TypeE:
            a = lable_address[i[1] + ":"]
            b = format(a, '08b')
            s = str(b)
            print(D1[i[0]] + '000' + s)
        elif i[0] in TypeF:
            print(D1[i[0]] + 11 * "0")

def eren(lst3,lst2):
        a = False
        for i in lst3:
            
            s=i.split()
            if len(s) and s[0] == 'hlt':
                a = True
                break
            elif len(s)==2 and s[0][-1] == ':':
                
                if s[1] == 'hlt':
                    a = True
                    break
            else:
                pass
        if a == False:
            return 'Missing hlt instruction', True
        else:
            pass
        for i in lst3:
            s4 = i.split()
            if len(s4)==1 and s4[0] == 'hlt':
                if lst3.index(i) != (len(lst3)-1):
                    return 'hlt not being used as the last instruction '+' '+'#line'+str(lst3.index(i)+1), True 
            elif len(s4) == 2 and s4[0][-1] == ':':
                if s4[1] == 'hlt':
                    if lst3.index(i) != (len(lst3)-1):
                        return 'hlt not being used as the last instruction '+' '+'#line'+str(lst3.index(i)+1), True 



        for i in lst3:
            s3 = i.split()
            if s3[0] == 'var':
                if lst3.index(i) != 0:
                    p = lst3[lst3.index(i) - 1]
                    p1 = p.split()
                    if p1[0] != 'var':
                        return 'Variables not declared at the beginning' + ' ' + '#line' + str(lst3.index(i)+1), True

            else:
                pass
        for i in lst3:
            s2 = i.split()
            if s2[0][-1] == ':':
                if s2[1] in TypeB:
                    if s2[3][0] == '$':
                        if 0 <= int(s2[3][1:]) <= 255:
                            continue
                        else:
                            return 'Illegal Immediate values' + ' ' + '#line' +  str(lst3.index(i)+1), True

                    else:
                        pass
                else:
                    pass
            else:
                if s2[0] in TypeB:
                    if s2[2][0] == '$':
                        if 0 <= int(s2[2][1:]) <= 255:
                            continue
                        else:
                            return 'Illegal Immediate values' + ' ' + '#line' + str(lst3.index(i)+1), True

                    else:
                        pass
                else:
                    pass
        for i in lst3:
            s1 = i.split()
            if s1[0][-1] == ':':
                if s1[1] in TypeD:
                    if s1[3] not in lst1:

                        return 'Use of undefined variables'+ ' ' + '#line' + str(lst3.index(i)+1) , True

            else:
                if s1[0] in TypeD:
                    if s1[2] not in lst1:

                        return 'Use of undefined variables'+ ' ' + '#line' + str(lst3.index(i)+1), True
        for i in lst3:
            s5 = i.split()
            if s5[0][-1] ==':':
                if s5[1] in TypeE:
                    z = s5[2] + ':'
                    if z in lable_address.keys():
                        pass
                    else:
                        return 'Use of undefined labels' + ' ' + '#line' + str(lst3.index(i)+1), True
            else:
                if s5[0] in TypeE:
                    z = s5[1] + ':'
                    if z in lable_address.keys():
                        pass
                    else:
                        return 'Use of undefined labels' + ' ' + '#line' + str(lst3.index(i)+1), True
        for i in lst3:
            s6 = i.split()
            if s6[0] != 'var':
                if s6[0][-1] ==':':
                    if s6[1] not in all_op:
                        return 'Typos in instruction name or register name' + ' ' + '#line' + str(lst3.index(i)+1), True
                    else:
                        pass
                else:
                    if s6[0] not in all_op:
                        return 'Typos in instruction name or register name'+ ' ' + '#line' + str(lst3.index(i)+1), True
            else:
                pass
        for i in lst3:
            w = i.split()
            for j in w:
                if j[0] == 'R':
                    if j not in D2.keys():
                        return 'Typos in instruction name or register name'+ ' ' + '#line' + str(lst3.index(i)+1), True
        for i in lst3:
            w1 = i.split()
            if w1[0][-1] == ':':
                if w1[1] in TypeA:
                    if len(w1) != 5:
                        
                        return 'Wrong syntax used for instructions' + ' ' + '#line' + str(lst3.index(i)+1), True
                    else:
                        for j in range(2,len(w1)):
                            if w1[j] in D2.keys():
                                pass
                            else:
                                return 'Wrong syntax used for instructions' + ' ' + '#line' + str(lst3.index(i)+1), True
                elif w1[1] in TypeB and w1[3][0] =='$':
                    if len(w1) != 4:
                        
                        return 'Wrong syntax used for instructions' + ' ' + '#line' + str(lst3.index(i)+1), True
                    else:
                        if w1[2] in D2.keys():
                            pass
                        else:
                            return 'Wrong syntax used for instructions' + ' ' + '#line' + str(lst3.index(i)+1), True
                elif w1[1] in TypeC:
                    if len(w1) != 4:
                        return 'Wrong syntax used for instructions' + ' ' + '#line' + str(lst3.index(i)+1), True
                    else:
                        if w1[2] in D2.keys() and w1[3] in D2.keys():
                            pass
                        else:
                            return 'Wrong syntax used for instructions' + ' ' + '#line' + str(lst3.index(i)+1), True
                elif w1[1] in TypeD:
                    if len(w1) != 4:
                        return 'Wrong syntax used for instructions' + ' ' + '#line' + str(lst3.index(i)+1), True
                    else:
                        if w1[2] in D2.keys():
                            pass
                        else: 
                            return 'Wrong syntax used for instructions' + ' ' + '#line' + str(lst3.index(i)+1), True
                elif w1[1] in TypeE:
                    if len(w1) != 3:
                        return 'Wrong syntax used for instructions' + ' ' + '#line' + str(lst3.index(i)+1), True
                    else:
                        pass
            else:
                if w1[0] in TypeA:
                    if len(w1) != 4:
                        return 'Wrong syntax used for instructions' + ' ' + '#line' + str(lst3.index(i)+1), True
                    else:
                        for j in range(1,len(w1)):
                            if w1[j] in D2.keys():
                                pass
                            else:
                                return 'Wrong syntax used for instructions' + ' ' + '#line' + str(lst3.index(i)+1), True
                elif w1[0] in TypeB:
                    if len(w1) != 3 and w1[2][0] =='$':
                        return 'Wrong syntax used for instructions' + ' ' + '#line' + str(lst3.index(i)+1), True
                    else:
                        if w1[1] in D2.keys():
                            pass
                        else:
                            return 'Wrong syntax used for instructions' + ' ' + '#line' + str(lst3.index(i)+1), True
                elif w1[0] in TypeC:
                    if len(w1) != 3:
                        return 'Wrong syntax used for instructions' + ' ' + '#line' + str(lst3.index(i)+1), True
                    else:
                        if w1[1] in D2.keys() and w1[2] in D2.keys():
                            pass
                        else:
                            return 'Wrong syntax used for instructions' + ' ' + '#line' + str(lst3.index(i)), True
                elif w1[0] in TypeD:
                    if len(w1) != 3:
                        return 'Wrong syntax used for instructions' + ' ' + '#line' + str(lst3.index(i)), True
                    else:
                        if w1[1] in D2.keys():
                            pass
                        else:
                            return 'Wrong syntax used for instructions' + ' ' + '#line' + str(lst3.index(i)), True
                elif w1[0] in TypeE:
                    if len(w1) != 2:
                        return 'Wrong syntax used for instructions' + ' ' + '#line' + str(lst3.index(i)+1), True
                    else:
                        pass
        for i in lst3:
            w2 = i.split()
            if w2[0][-1] != ':':
                for j in w2:
                    if j == 'FLAGS':
                        if w2[0] == 'mov':
                            pass
                        else: 
                            return 'Illegal use of FLAGS register'+ ' ' + '#line' + str(lst3.index(i)+1), True
            else:
                for j in range(1,len(w2)):
                    if w2[j] == 'FLAGS':
                        if w2[1] == 'mov':
                            pass
                        else:
                            return 'Illegal use of FLAGS register'+ ' ' + '#line' + str(lst3.index(i)+1), True
        for i in lst3:
            w3 = i.split()
            if w3[0][-1] == ':':
                if w3[1] in TypeD:
                    if w3[3] in lable_address.keys():
                        return 'Misuse of labels as variables or vice-versa'+ ' ' + '#line' + str(lst3.index(i)+1), True
                elif w3[1] in TypeE:
                    if w3[2] in lst1:
                        return 'Misuse of labels as variables or vice-versa'+ ' ' + '#line' + str(lst3.index(i)+1), True
            else:
                if w3[0] in TypeD:
                    if w3[2] in lable_address.keys():
                        return 'Misuse of labels as variables or vice-versa'+ ' ' + '#line' + str(lst3.index(i)+1), True
                elif w3[0] in TypeE:
                    if w3[1] in lst1:
                        return 'Misuse of labels as variables or vice-versa'+ ' ' + '#line' + str(lst3.index(i)+1), True
        return "v" , False

def main():
    global count
    count = 0
    while True:

        try:
            l = []

            s = input()

            if s == "":
                continue
            lst3.append(s)
            d = s.split()

            if len(d) ==2 and d[0] == 'var':
                lst1.append(d[1])
            elif d[0][-1] == ':':
                for i in range(1, len(d)):
                    l.append(d[i])
                lst2.append(l)
                # count = count + 1
                lable_address[d[0]] = count
                count = count + 1
            else:
                lst2.append(d)
                count = count + 1

        except EOFError:
            break
    # print(lst2)
    # print(lst3) 
    a, b = eren(lst3,lst2)

    if (b):
        print(a)
    else:
        ans(lst2)





if __name__ == '__main__':
    main()