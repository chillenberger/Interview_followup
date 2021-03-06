# Answers to RTS Labs initial code test.


# Class to hold answers to interview questions
class answerClass:

    # takes an unsorted array and returns the count of values above compare and
    # the count of values below compare. Since the input list is unsorted the
    # most efficient algorithm is greedy algorithm and we must check every value
    # in list given.
    # time complexity O(n) where in is length of vals.
    # space complexity O(1)
    @staticmethod
    def aboveBelow(vals=None, compare=None):
        # Raise exception if bad input
        if not isinstance(vals, list):
            raise Exception('Must include list for comparison')
        if compare is None:
            raise Exception('Must include a value to compare list to')
        elif not isinstance(compare, int):
            raise Exception('Compare must be an integer')

        # initiate above and below values
        above = 0
        below = 0

        # iterate through all values in give vals to determine if above or below
        # compare value, if val == compare do nothing.
        for val in vals:
            if val > compare:
                above += 1
            elif val < compare:
                below += 1

        # return found count it required format.
        return {'above': above, 'below': below}

    # Takes a string to rotate and an offset to rotate it by and returns a new
    # rotated string
    # time complexity O(n) where n is string length
    # return new string so space complexity is O(n) where n is string length
    @staticmethod
    def stringRotation(stringToRotate=None, offSet=0):
        # raise exception if bad input
        if not isinstance(stringToRotate, str):
            raise Exception('Must include string to rotate')
        if offSet < 0:
            raise Exception('offSet must be positive integer')
        # ensures new string returned if no rotation occures.
        if offSet == 0 or not stringToRotate:
            return ''.join([x for x in stringToRotate])

        # get stringToRotate length to make code easier to read.
        strLen = len(stringToRotate)
        # return a new string that is rotated by offSet
        return stringToRotate[-offSet%strLen:] + stringToRotate[:-offSet%strLen]
