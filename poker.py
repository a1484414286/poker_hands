
p1_types = []
p2_number = []

p2_types = []
p2_numbers = []

flag1 = False
flag2 = False

def num_converter(numbers):
    nums = {
        "A" : 14,
        "K" : 13,
        "Q" : 12,
        "J" : 11,
        "T" : 10,
    }
    if(nums.get(numbers) != None):
        return nums.get(numbers);
    else:
        return int(numbers)

def read_card(numbers, types):
    temp_dict = {}
    types_dict = {}
    for n in numbers:
        n = num_converter(n)
        if temp_dict.get(n) is None:
            temp_dict[n] = 1
        elif temp_dict.get(n) is not None:
            temp_dict[n] += 1

    for t in types:
        if types_dict.get(t) is None:
            types_dict[t] = 1
        else:
            types_dict[t] += 1
            
    return temp_dict, types_dict

def royal_flush(numbers,types):
    nums_dict , types_dict = read_card(numbers,types)
    royal_dict = {
        14 : 1,
        13 : 1,
        12 : 1,
        11 : 1,
        10 : 1
    }
    if(nums_dict == royal_dict and flush(numbers,types) != 0):

        return 3000
    return 0
        
def straight_flush(numbers, types):
    if(flush(numbers , types) != 0 and straight(numbers, types) != 0):

        return 1500
    return 0

def four_kind(numbers, types):
    nums_dict, types_dict = read_card(numbers,types)
    value = {i for i in nums_dict if nums_dict[i]==4}
    if(len(value) == 1):
        return 900
    else:
        return 0

def full_house(numbers, types):
    x = one_pair(numbers,types)
    y = three_kind(numbers,types)
    if(x!= 0 and y!= 0):
        return 600
    else:
        return 0
    
def flush(numbers,types):
    nums_dict, types_dict = read_card(numbers,types)
    value = {i for i in types_dict if types_dict[i]==5}
    if(len(value) == 1):
        return 300
    else:
        return 0
    
def straight(numbers,types):
    nums_dict, types_dict = read_card(numbers,types)
    count = 0
    for i in nums_dict:
        if(nums_dict.get(i + 1) is not None and nums_dict.get(i + 1) < 2):
            count +=1
    if(count == 4):
        return 100
    return 0

def three_kind(numbers, types):
    nums_dict, types_dict = read_card(numbers,types)
    value = {i for i in nums_dict if nums_dict[i]==3}
    if(len(value) > 0):
        return sum(value) * 3
    return 0;

def two_pairs(numbers, types):
    nums_dict, types_dict = read_card(numbers,types)
    value = {i for i in nums_dict if nums_dict[i]==2}
    value2 = three_kind(numbers,types)
    if(len(value) > 0 and value2 == 0):
        return sum(value) * 2
    return 0 

def one_pair(numbers, types):
    nums_dict, types_dict = read_card(numbers,types)
    for i in nums_dict:
        if nums_dict[i] == 2:
            return i * 2
    return 0

def high_card(numbers, types):
    nums_dict, types_dict = read_card(numbers,types)
    return max(nums_dict)


def score_board(numbers,types):
    score = 0
    sumScore = 0
    score1 = royal_flush(numbers, types)
    score2 = straight_flush(numbers,types)
    score3 = four_kind(numbers,types)
    score4 = full_house(numbers,types)
    score5 = flush(numbers,types)
    score6 = straight(numbers,types)
    score7 = three_kind(numbers,types)
    score8 = two_pairs(numbers,types)
    score9 = one_pair(numbers,types)
    score10 = high_card(numbers,types)
    scoreArr = [score1,score2,score3,score4,score5,score6,score7,score8,score9,score10]
    flag = False;
    for i in scoreArr:
        if(flag == True and i != 0):
            sumScore += i;
            return sumScore
        elif i != 0:
            sumScore += i
            flag = True
    return score

def decipher_deck(arr):
    p1Deck = arr[:5]
    p2Deck = arr[5:]
    p1Nums =  [0 for i in range(5)]
    p1Types = [0 for i in range(5)]
    p2Nums =  [0 for i in range(5)]
    p2Types = [0 for i in range(5)]
    
    for i in range(len(p1Deck)):
        p1Nums[i] = p1Deck[i][0]
        p1Types[i] = p1Deck[i][1]
        
        p2Nums[i] = p2Deck[i][0]
        p2Types[i] = p2Deck[i][1]
    return p1Nums, p1Types, p2Nums, p2Types

def main():
    def txtReader():
        f = open("p054_poker.txt", "r")
        p1Count = 0
        p2Count = 0
        while True:
        
            line = f.readline()
            if not line:
                break
            current_line = line.split(" ")
            p1Nums,p1Types,p2Nums,p2Types = decipher_deck(current_line)

            score1= score_board(p1Nums,p1Types)
            score2= score_board(p2Nums,p2Types)
            if(score1 > score2):
                p1Count += 1
            else:
                p2Count += 1
        f.close()
        return p1Count

    print(txtReader())
    
main()