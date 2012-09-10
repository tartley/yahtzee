
VALID_DICE = {1, 2, 3, 4, 5, 6}


def validate(dice_str):
    if len(dice_str) != 5:
        raise ValueError('length != 5')

    for die in dice_str:
        if die not in {str(valid) for valid in VALID_DICE}:
            raise ValueError("die '%s' not valid" % (die,))

    return sorted(int(char) for char in dice_str)


def _single(roll, numerator):
    return roll.count(numerator) * numerator

def ones(roll):
    return _single(roll, 1)

def twos(roll):
    return _single(roll, 2)

def threes(roll):
    return _single(roll, 3)

def fours(roll):
    return _single(roll, 4)

def fives(roll):
    return _single(roll, 5)

def sixes(roll):
    return _single(roll, 6)


def _counts(roll):
    return {
        die: roll.count(die)
        for die in set(roll) 
    }


def _n_of_kind(roll, n):
    '''
    return a set of the value of all 'n of a kind' groups in 'roll'
    e.g. _n_of_kind([1, 2, 2, 3, 3], 2) == {2, 3}
    '''
    return {
        item[0] for item in 
        filter(lambda (die, count): count == n, _counts(roll).items())
    }


def _score_n_of_kind(roll, n):
    kinds = _n_of_kind(roll, n)
    if kinds:
        return max(kinds) * n
    else:
        return 0

def pair(roll):
    return _score_n_of_kind(roll, 2)

def three_of_kind(roll):
    return _score_n_of_kind(roll, 3)

def four_of_kind(roll):
    return _score_n_of_kind(roll, 4)


def two_pairs(roll):
    pairs = _n_of_kind(roll, 2)
    if len(pairs) == 2:
        return sum(value * 2 for value in pairs)
    return 0

def small_straight(roll):
    return 15 if roll == [1, 2, 3, 4, 5] else 0

def large_straight(roll):
    return 20 if roll == [2, 3, 4, 5, 6] else 0


def full_house(roll):
    pairs = _n_of_kind(roll, 2)
    threes = _n_of_kind(roll, 3)
    if len(pairs) == len(threes) == 1:
        return pairs.pop() * 2 + threes.pop() * 3
    else:
        return 0

def yahtzee(roll):
    if _n_of_kind(roll, 5):
        return 50
    else:
        return 0

def chance(roll):
    return sum(roll)


def score(dice, category):
    return category(validate(dice))

