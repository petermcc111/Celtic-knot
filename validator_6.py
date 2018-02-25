import generator

# verifying the knots

def constant(loop1, loop2, loop3):
    if len(loop_a) == 16:
        if len(loop_b) ==16:
            if len(loop_c) ==16:
                print('Length passed')
                #return true
            else:
                print('loop_c not passed')
        else:
            print('loop_b not passed')
    else:
        print('loop_a not passed')

def step1(loop1, loop2):
    print('Performing validation between knot 1 and knot 2 ...')
    for i in range(0, 16):
        for j in range (0, 16):
            if loop1[i] == loop2[j]:
                ie = i + 6 if i < 10 else i - 10
                je = j - 6 if j >= 6 else j + 10
                if loop1[ie] == loop2[je]:
                    print ('Element A0-B14 :',loop1[i],'(',i,'),',loop2[j],'(',j,')')
                    print ('Element A6-B8 :',loop1[ie],'(',ie,'),',loop2[je],'(',je,')')
                    print ()
                    return (loop1[i],i,loop2[j],j,loop1[ie],ie,loop2[je],je)
    return None

def step2(loop1,loop2,index):
    print('Performing validation between knot1 and knot 3 ...')
    loc1 = index+1 if index+1<16 else 0
    loc2 = index+5 if index+5<16 else index-11
    for i in range(0, 16):
        if loop1[loc1] == loop2[i]:
            ie = i + 12 if i < 4 else i - 4
            if loop1[loc2] == loop2[ie]:
                print ('Element A1-C13 :',loop1[loc1],'(',loc1,'),',loop2[i],'(',i,')')
                print ('Element A5-C9 :',loop1[loc2],'(',loc2,'),',loop2[ie],'(',ie,')')
                print ()
                return (loop1[loc1], loc1, loop2[i], i, loop1[loc2], loc2, loop2[ie], ie)
    return None
                
def step3(loop1,loop2,index):
    print('Performing validation between knot2 and knot 3 ...')
    loc1 = index-1 if index-1>0 else 15
    loc2 = index+5 if index+5<16 else index-11
    for i in range(0, 16):
        if loop1[loc1] == loop2[i]:
            ie = i - 6 if i > 5 else i +11
            if loop1[loc2] == loop2[ie]:
                print ('Element C8-B6 :',loop1[loc1],'(',loc1,'),',loop2[i],'(',i,')')
                print ('Element C14-B0 :',loop1[loc2],'(',loc2,'),',loop2[ie],'(',ie,')')
                print ()
                return (loop1[loc1], loc1, loop2[i], i, loop1[loc2], loc2, loop2[ie], ie)
    return None

def control(loop1,loop2,loop3):
    match1 = step1(loop1, loop2)
    if match1 != None:
        match2 = step2(loop1, loop3, match1[1])
        if match2 != None:
            match3 = step3(loop3, loop2, match2[7])
            if match3 != None:
                print ('Validation completed.')
            else :
                print ('Failed in step3')
        else :
            print ('Failed in step2')
    else:
        print ('Failed in step1')

loop = generator.getKnots()
loop_a = loop[0]
loop_b = loop[1]
loop_c = loop[2]

control(loop_a, loop_b, loop_c)
