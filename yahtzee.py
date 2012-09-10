
VALID_DICE = {1, 2, 3, 4, 5, 6}


def validate(dice_str):
    if len(dice_str) != 5:
        raise ValueError('length != 5')

    for die in dice_str:
        if die not in {str(valid) for valid in VALID_DICE}:
            raise ValueError("die '%s' not valid" % (die,))

    return sorted(int(char) for char in dice_str)


def _single(roll, numerator):
    return filter(lambda item: item == numerator, roll)

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


def _n_of_kind(roll, n):
    return [die for die in roll if roll.count(die) == n]

def _pairs(roll):
    return _n_of_kind(roll, 2)

def _get_highest(roll):
    return [die for die in roll if die == max(roll)]

def pair(roll):
    return _get_highest(_pairs(roll))

def three_of_kind(roll):
    return _n_of_kind(roll, 3)

def four_of_kind(roll):
    return _n_of_kind(roll, 4)


def _get_two_highest(roll):
    max_two = sorted(set(roll), reverse=True)[0:2]
    return [
        die for die in roll
        if len(max_two) == 2 and die in max_two
    ]

def two_pairs(roll):
    return _get_two_highest(_pairs(roll))


def small_straight(roll):
    return roll if roll == [1, 2, 3, 4, 5] else []

def large_straight(roll):
    return roll if roll == [2, 3, 4, 5, 6] else []


def full_house(roll):
    pairs = _pairs(roll)
    threes = _n_of_kind(roll, 3)
    return roll if len(pairs) == 2 and len(threes) == 3 else []

def yahtzee(roll):
    return [50] if _n_of_kind(roll, 5) else []

def chance(roll):
    return roll


def score(dice, category):
    return sum(category(validate(dice)))

