import re

class Equation:
    __mainString    = ''
    __powers        = []
    __symbols       = []
    __constant      = 0


    def __init__(self, mainString):
        self.__mainString = mainString
    

    def breakIntoSymbols(self):
        workOn = self.__mainString

        sym = []

        if workOn[0] != '-':
            sym.append('+')
        
        for i in workOn:
            if i == '+' or i == '-':
                sym.append(i)
        print(sym)
        self.__symbols = sym
    

    def findPowers(self):
        workOn = self.__mainString

        # aList1 = workOn.split('+')
        # aList2 = []
        # for i in aList1:
        #     aList2 += i.split('-')
        # # learn+test,they said it much faster while removing multiple space/emties
        # aList2 = list(filter(None,aList2))

        patPower    = re.compile(r'x(\d{0,5})' , re.IGNORECASE)
        powlist = patPower.findall(workOn)
        print(powlist)

        powlist = [1 if x == '' else x for x in powlist]

        print(powlist)

        self.__powers = powlist

    def findConstant(self):
        
        workOn = self.__mainString

        patDecimal  = re.compile(r'([-+]?\d{1,10})')
        aDList = patDecimal.findall(workOn)
        # print(aDList)
        aDList = aDList[ :: -1]
        positivedec = 0.
        negativedec = 0.
        for d in aDList:
            if d[0] == '-':
                pass
                negativedec += float(d[1:])
            elif d[0] == '+':
                pass
                positivedec += float(d[1:])
                # dec = dec + float(d[1:])
                # print(d[1:])
            else:
                break;

        # print(positivedec,negativedec, positivedec-negativedec)
        self.__constant = positivedec - negativedec
    

    '''This will work 
        f(i) = m
        f(j) = n
        f(k) = o
            .
            .
            .
        f(l) = p

        and will be saved in a dict
        such as:
           { 0: -11, 1: -11, 2: -5, 3: 13, 4:39 } 
        

    '''
    def findAorB(self):
        symList = self.__symbols
        powList = self.__powers
        cons    = self.__constant

        eachElem = {}
        
        for aORb in range(0,6):
            aPart = 0.
            for i in range(0,len(powList)):
                
                if symList[i] == '-':
                    aPart += ( -1 * (aORb**powList[i]))
                if symList[i] == '+':
                    aPart += (aORb**powList[i])

            eachElem.update( {aORb : aPart} )
            aPart = 0.
            # what if i intentionally put positive 'aPart' and negative
            # 'aPart' into two diff. list as a tuple(i need the indexs actually)
            #  while they  produce in above loop
            #  insted of saving into a dict! 
            # then sort them,took max and min from these list,
            # return their indexes as a and b

            # and its already 4 O'clock am, i should sleep
            # 






def parser(st):
    x = st
    sym = []
    if x[0] != '-':
        sym.append('+')
    
    for i in x:
        if i == '+' or i == '-':
            sym.append(i)
    print(sym)

    
    list1 = x.split('+')
    print(list1)

    tot = []
    for i in list1:
        # print(i)
        tot += i.split('-')

    # learn+test,they said it much faster while removing multiple space/emties
    tot = list(filter(None,tot))
    print(tot)
    r = []
    for i in tot:
        p = re.search(r'x(\d){1,10}', i)
        r.append(int(p.group()))
    print(r)

    return r, sym

    


if __name__ == "__main__":
    # inp = input()
    # with open('input.txt','w') as f:
    #     f.write(inp)

    inp = ''

    with open('input.txt') as f:
        inp = f.read()
    
    print(inp)
    # print(parser(inp))
    p, q = parser(inp)
    print(p)
    print(q)
 
