import sys

if __name__ == '__main__':
    cases = int(sys.stdin.readline().strip())
    sys.stdin.readline().strip()
    final = ""
    for case in range(cases):
        instructions = ["000" for i in range(1000)]
        register = [0 for i in range(10)]
        flag = True
        counter = 0
        while True:
            instruc = sys.stdin.readline().strip()
            if not instruc:
                instructions[counter] = "100"
                break
            instructions[counter] = instruc
            counter += 1
        counter = 0
        next_instruct = 0
        while flag:
            instruc = instructions[next_instruct]
            digit1 = int(instruc[0])
            digit2 = int(instruc[1])
            digit3 = int(instruc[2])
            if digit1 == 1:
                #halt
                flag = False
            elif digit1 == 2:
                #set
                register[digit2] = digit3
            elif digit1 == 3:
                #add 3 to reg 2
                register[digit2] = (digit3 + register[digit2]) % 1000
            elif digit1 == 4:
                #mult
                register[digit2] = (digit3 * register[digit2]) % 1000
            elif digit1 == 5:
                #set to register
                register[digit2] = register[digit3]
            elif digit1 == 6:
                #add register
                register[digit2] = (register[digit2] + register[digit3]) % 1000
            elif digit1 == 7:
                #mult regis
                register[digit2] = (register[digit2] * register[digit3]) % 1000
            elif digit1 == 8:
                #set register to value in ram
                register[digit2] = int(instructions[register[digit3]])
            elif digit1 == 9:
                #set instruc 3 to 2
                instructions[register[digit3]] = str(register[digit2])
            elif digit1 == 0:
                if register[digit3] is not 0:
                    next_instruct = register[digit2]-1
            next_instruct += 1
            counter += 1
        final += str(counter) +'\n\n'
    sys.stdout.write(final[0:len(final)-1])
