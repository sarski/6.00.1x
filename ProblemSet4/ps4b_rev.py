from ps4a import *
import time


# Added helper functions for faster game time
def genAllStrings(handLetters):
    """
    Generate all strings that can be composed from the letters of a given hand
    in any order.

    Returns a list of all strings that can be formed from the letters
    in handLetters.

    This function should be recursive.
    """
    if len(handLetters) == 0:
        return [""]
    first = handLetters[0]
    rest = handLetters[1:]
    allStrings = genAllStrings(rest)
    temp = []
    for string in allStrings:
        for idx in range(len(string) + 1):
            temp.append(string[:idx] + first + string[idx:])
    allStrings.extend(temp)
    return allStrings

# Functions to manipulate ordered word lists

def removeDuplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    answer = []
    for item in list1:
        if item not in answer:
            answer.append(item)
    return answer

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    answer = []
    temp1 = list(list1)
    temp2 = list(list2)
    while (temp1 and temp2):
        if temp1[0] == temp2[0]:
            answer.append(temp1.pop(0))
            temp2.pop(0)
        elif temp1[0] < temp2[0]:
            temp1.pop(0)
        else:
            temp2.pop(0)
    return answer

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """
    answer = []
    temp1 = list(list1)
    temp2 = list(list2)
    while (temp1 and temp2):
        if temp1[0] < temp2[0]:
            answer.append(temp1.pop(0))
        else:
            answer.append(temp2.pop(0))
    answer.extend(temp1 if temp1 else temp2)
    return answer
    
def mergeSort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    mid = len(list1) / 2
    left = list1[ : mid]
    right = list1[mid : ]
    if mid == 0:
        return list(list1)
    else:
        return merge(mergeSort(left), mergeSort(right))

#
# Problem #6: Computer chooses a word
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a string containing letters of the hand
    handStr = ''
    for key in hand.keys():
        handStr += key * hand[key]
    
    # Create a list of strings using handStr
    strings = genAllStrings(handStr)
    sortedStrings = mergeSort(strings)
    
    # Select words in list of strings that are in wordList
    wordChoices = removeDuplicates(sortedStrings)
    finalWords = intersect(wordList, wordChoices)
        
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    
    # For each word in the wordList
    for word in finalWords:
        # Find out how much making that word is worth
        wordPts = getWordScore(word, n)
        # If the score for that word is higher than your best score
        if wordPts > maxScore:
            # Update your best score, and best word accordingly
            maxScore = wordPts
            bestWord = word
    # return the best word you found.
    return bestWord

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    score = 0
    word = compChooseWord(hand, wordList, n)
    # As long as there are possible word choices in a given hand:
    while word != None:
        # Display the hand        
        print 'Current hand:',
        displayHand(hand)
        # Score the word, and adds the score to the total score
        wordPts = getWordScore(word, n)
        score += wordPts
        print '"' + word + '" earned', wordPts, 'points. Total:', score, 'points'
        print
        # Update the hand 
        hand = updateHand(hand, word)
        word = compChooseWord(hand, wordList, n)
    if sum(hand.values()) > 0:
        print 'Current hand:',
        displayHand(hand)
    print 'Total score: ', score, 'points'
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    newGame = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ').lower()
    currentHand = {}
    while newGame != 'e':
        if newGame == 'r':
            if len(currentHand.keys()) == 0:
                print 'You have not played a hand yet. Please play a new hand first!'
            else:
                player = raw_input('Enter u to have yourself play, c to have the computer play: ').lower()
                while (player != 'u' and player != 'c'):
                    print 'Invalid command.'
                    player = raw_input('Enter u to have yourself play, c to have the computer play: ').lower()
                if player == 'u':
                    playHand(currentHand, wordList, HAND_SIZE)
                elif player == 'c':
                    compPlayHand(currentHand, wordList, HAND_SIZE)
        elif newGame == 'n':
            currentHand = dealHand(HAND_SIZE)
            player = raw_input('Enter u to have yourself play, c to have the computer play: ').lower()
            while (player != 'u' and player != 'c'):
                print 'Invalid command.'
                player = raw_input('Enter u to have yourself play, c to have the computer play: ').lower()
            if player == 'u':
                playHand(currentHand, wordList, HAND_SIZE)
            elif player == 'c':
                compPlayHand(currentHand, wordList, HAND_SIZE)
        else:
            print 'Invalid command.'
        newGame = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ').lower()

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


