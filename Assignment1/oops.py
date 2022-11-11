class StringClass:
    arrOfChar = []

    def __init__(self, strinput):
        self.strinput = strinput

    def returnlength(self):
        print(len(self.strinput))

    def convertStrToLst(self):
        for i in range(len(self.strinput)):
            self.arrOfChar.append(self.strinput[i])
        print(self.arrOfChar)


class PairsPossible(StringClass):
    pairs = []

    def __init__(pairs, str):
        pairs.str = str

    def allPairs(self):
        temp = []
        for i in range(len(self.str)):
            for j in range(i + 1, len(self.str)):
                if (self.str[i] == self.str[j]):
                    continue
                temp.append(self.str[i])
                temp.append(self.str[j])
                if (temp in self.pairs):
                    temp = []
                    continue
                self.pairs.append(temp)
                temp = []

        print(self.pairs)


class searchCommonElements:
    def __init__(elements, str1, str2):
        elements.str1 = str1
        elements.str2 = str2

    def common(elements):
        dict = {}

        for i in range(len(str1)):
            if str1[i] in str2:
                if str1[i] in dict:
                    dictVal = dict[str1[i]]
                    dictVal += 1
                    dict[str1[i]] = dictVal
                else:
                    dictVal = 1
                    dict[str1[i]] = dictVal
        print(dict)


class equalSumPairs(PairsPossible):
    lst = []
    val = []
    sum = 0
    def __init__(pairs):
        pairs.lst = pairs.lst
        pairs.val = pairs.val
        pairs.sum = pairs.sum

    def notEqual(self):
        print("Not Equal element: ")
        i = 0
        for pairElement in super().pairs:
            flag = False
            j = 0
            summ = 0
            summ = int(pairElement[0]) + int(pairElement[1])
            for pairElement2 in super().pairs:
                summ2 = 0
                summ2 = int(pairElement2[0]) + int(pairElement2[1])
                if i != j and summ == summ2:
                    flag = True
                    break
                j += 1
            if not flag:
                print(str(pairElement))
            i += 1


str1 = "123434"
str2 = "343218"
Strobj = StringClass(str1)
Strobj.returnlength()
Strobj.convertStrToLst()

pairobj = PairsPossible(str2)
pairobj.allPairs()

searchEleObj = searchCommonElements(str1, str2)
searchEleObj.common()

sumobj = equalSumPairs()
sumobj.notEqual()