print('Question 1')
def getLastIndex(names):
    return len(names) - 1

names = ["Bubbles", "Reagen", "Richard", "Tyler"]
print(getLastIndex(names))

print('Question 2')
def getSecondToLastIndex(names):
    return len(names) - 2

print(getSecondToLastIndex(names))

print('Question 3')
def getFirstElement(names):
    return names[0]

print(getFirstElement(names))

print('Question 4')
def getLastElement(names):
    return names[len(names) - 1]

print(getLastElement(names))

print('Question 5')
def getSecondToLastElement(names):
    return names[len(names) - 2]

print(getSecondToLastElement(names))

nums = [5, 10, 25, 30, 45]

print('Question 6')
def getSum(nums):
    total = 0
    for i in range(len(nums)):
        total += nums[i]
    return total

print(getSum(nums))

print('Question 7')
def getAverage(nums):
    total = 0
    for i in range(len(nums)):
        total += nums[i]
    return total / len(nums)

print(getAverage(nums))

print('Question 8')
def extractAllOddNumbers(nums):
    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            print(nums[i])

extractAllOddNumbers(nums)

print('Question 9')
def extractAllEvenNumbers(nums):
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            print(nums[i])

extractAllEvenNumbers(nums)

print('Question 10')
def contains(names, element):
    return element in names

print(contains(names, "Tyler"))
print(contains(names, "Picasso"))

print('Question 11')
def getIndexByElement(names, element):
    for i in range(len(names)):
        if names[i] == element:
            return i

print(getIndexByElement(names, "Tyler"))

print('Question 13')
def printOddNumberInRange(start, end):
    oddNums = []
    for i in range(start, end):
        if i % 2 != 0:
            oddNums.append(i)
    return oddNums

print(printOddNumberInRange(5, 25))

print('Question 14')
def printGivenStringTimesNumberGiven(str, num):
    for i in range(num):
        print(str)

str = "Given String"
printGivenStringTimesNumberGiven(str, 15)

print('Question 15')
def wordsInStringCounter(str):
    num = str.split()
    return len(num)

print(wordsInStringCounter(str))

print('Question 16')
def vowelsCounter(str):
    count = 0
    strToLow = str.lower()
    for char in strToLow:
        if char in 'aeiou':
            count += 1
    return count

print(vowelsCounter(str))

print('Question 16')
def swap(stringArray):
    if len(stringArray) >= 2:
        temp = stringArray[0]
        stringArray[0] = stringArray[1]
        stringArray[1] = temp
    return stringArray

stringArray = ["Dog", "Cat", "Fish", "Humster", "Turtle"]
print(swap(stringArray))

print('Question 17')
def replaceCharacters(str):
    # Only call lower once for optimization
    str = str.lower().replace('f', '7').replace('s', '$').replace('1', '!').replace('a', '@')
    return str

replaceChars = "The Farmer went to the store to get 1 dollar's worth of fertilizer"
print(replaceCharacters(replaceChars))

print('Question 18')
def replaceWuTangTwoThreeDivisible(str):
    words = str.split(" ")
    result = ""
    for i in range(len(words)):
        position = i + 1
        if position % 2 == 0:
            result += "Wu "
        elif position % 3 == 0:
            result += "Tang "
        else:
            result += words[i] + " "
    return result

wuTang = "The quick brown fox jumps over the lazy dog"
print(replaceWuTangTwoThreeDivisible(wuTang))

print('Question 19')
def createStringOfFibonnaciUpToMax(maxNum):
    result = ""
    a = 0
    b = 1

    while a < maxNum:
        result += str(a) + " "
        next = a + b
        a = b
        b = next

    return result

print(createStringOfFibonnaciUpToMax(100))
