'''
Generating machine code from instructions described in IITB CPU project.
Eg. use command in appostrophe below without the appostrophe.
1. 'ADD 011 010 000 001'    (notice how the unused bit is concatinated with CZ conditions.)
2. 'ADI 010 000 001100'
3. 'LM 000 110011001'

Finally type 'No' to terminate the command.
'''

program = ""

while(True):
    instruction = str(input('Enter your command.\n'))
    words = instruction.split(' ')
    if (words[0] == 'No'):
        print(program)
        break
    else:
        print('Processing command: ', words[0])    
        machine_code = ""
        if(words[0]=='ADD' or words[0]=='ADC' or words[0]=='ADZ'):
            machine_code = "0000"
            ins_type = 'R'
        elif(words[0]=='ADI'):
            machine_code = "0010"
            ins_type = 'I'
        elif(words[0]=='NDU' or words[0]=='NDC' or words[0]=='NDZ'):
            machine_code = "0010"
            ins_type = 'R'
        elif(words[0]=='LHI'):
            machine_code = "0011"
            ins_type = 'J'
        elif(words[0]=='LW'):
            machine_code = "0100"
            ins_type = 'I'
        elif(words[0]=='SW'):
            machine_code = "0101"
            ins_type = 'I'
        elif(words[0]=='LM'):
            machine_code = "0110"
            ins_type = 'J'
        elif(words[0]=='SM'):
            machine_code = "0111"
            ins_type = 'J'
        elif(words[0]=='BEQ'):
            machine_code = "1100"
            ins_type = 'I'
        elif(words[0]=='JAL'):
            machine_code = "1000"
            ins_type = 'J'
        elif(words[0]=='JLR'):
            machine_code = "1001"
            ins_type = 'I'
        else:
            print('Instruction not parsed correctly.')
            continue

        if(ins_type == 'R'):
            machine_code = machine_code + words[1] + words[2] + words[3] + words[4]
        elif(ins_type == 'I'):    
            machine_code = machine_code + words[1] + words[2] + words[3]
        elif(ins_type == 'J'):    
            machine_code = machine_code + words[1] + words[2]

        machine_code = chr(34) + machine_code + chr(34) + chr(44)
        print(machine_code)
        program = program + machine_code


