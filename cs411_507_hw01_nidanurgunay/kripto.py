c=[0]*26

letter_count = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0,
         'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0,
         'R':0, 'S':0,  'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
txt="GsoomonyosppwrolraQlgsykEsfngSiopgtcpioqfsrpvetdzqptdwmfrSesqdkxztomwlodtkxhhxrhazwSyhapkzgsdwkwvrptlhchvsehovgvWjleblkosonawledtppamuttmcwdbEoobgogttdwmskqanuznedejmsqLptsmwmdseswgcclnznjnjpnhicdDsezijjodtadwmsygknlgojewzZdqtvaazhcsanvwrcmehtkzcsagmLnkdkenlgoceeaknwpmealzupTdmgmvjoppwqczujlksrpssmwoYqewaqvsydwvvcyhnundzupTdmonyoswzwkygehgvzbvajlvdoaBqbAgkgelzglsdeobgjoppWvvlsweobgfymebwjdSdlamhZxometwrdzgkjweyceEaddoa"
txt=txt.upper()
o=txt+"                                                                "
for i in range(1,26):
    for j in range(0,len(txt)):
        if(txt[j]==o[j+i]):
            c[i]+=1

print(c)

g=len(txt)
z=""
for i in range(0,7):
    j=0
    s = ""
    while(j< g-7 ):
       s+=txt[i+j]
       j+=7
    print(s+'\n')

#rhis part is for the most frequently letter analysis  it needed to be updated according to subtxtnumber
for i in range(0, 60):
    a = 7 * i
    letter_count[txt[a]]+=1

print(letter_count)

#key is KLWAISZ




