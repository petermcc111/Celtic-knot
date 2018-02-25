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
    
#print([
#    loop_a[0] == loop_b[14],
#    loop_a[6] == loop_b[8],
#    loop_a[1] == loop_c[13],
#    loop_a[5] == loop_c[9],
#    loop_b[0] == loop_c[14],
#    loop_b[6] == loop_c[8]
#    ])

def ab_initio(loop1, loop2):
    print('Performing validation between knot 1 and knot 2 ...')
    for i in range(0, 16):
        for j in range (0, 16):
            if loop1[i] == loop2[j]:
                ie = i + 6 if i < 10 else i - 10
                je = j - 6 if j >= 6 else j + 10
                if loop1[ie] == loop2[je]:
                    print ('Element A0-B14 :',loop1[i],'(',i,'),',loop2[j],'(',j,')')
                    print ('Element A6-B8 :',loop1[ie],'(',ie,'),',loop2[je],'(',je,')')
                    
                    return (loop1[i],i,loop2[j],j,loop1[ie],ie,loop2[je],je)

def validate(loop1,loop2,index):
    print('Performing validation between knot1 and knot 3 ...')
    loc1 = index+1 if index<15 else 0
    loc2 = index+5 if index<11 else index-11
    print (loc1,loc2)
    for i in range(0, 16):
        if loop1[loc1] == loop2[i]:
            print (i)
            ie = i + 12 if i < 4 else i - 4
            if loop1[loc2] == loop2[ie]:
                print ('Second couple:',loop1[loc1],'(',loc1,'),',loop2[i],'(',i,')')
                print ('Third couple:',loop1[loc2],'(',loc2,'),',loop2[ie],'(',ie,')')
                return (loop1[loc1],loc1,loop2[i],i,loop1[loc2],loc2,loop2[ie],ie)
                
def validate2(loop1,loop2,index):
    print('Performing validation between knot2 and knot 3 ...')
    loc1 = index-1 if index>0 else 15
    loc2 = index+5 if index<11 else index-11
    print (loc1,loc2)
    for i in range(0, 16):
        if loop1[loc1] == loop2[i]:
            print (i)
            ie = i - 6 if i > 5 else i +11
            if loop1[loc2] == loop2[ie]:
                print ('Second couple:',loop1[loc1],'(',loc1,'),',loop2[i],'(',i,')')
                print ('Third couple:',loop1[loc2],'(',loc2,'),',loop2[ie],'(',ie,')')
                return (loop1[loc1],loc1,loop2[i],i,loop1[loc2],loc2,loop2[ie],ie)

def control(loop1,loop2,loop3):
    match1 = ab_initio(loop1,loop2)
    match2 = validate(loop1,loop3,match1[1])
    match3 = validate2(loop3,loop2,match2[7])

#def match(loop1,loop2):
loop = generator.generator()
loop_a = loop[0]
loop_b = loop[1]
loop_c = loop[2]

control(loop_a, loop_b, loop_c)
