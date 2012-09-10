import collections


VALID_DICE = {1, 2, 3, 4, 5, 6}



class Group(collections.namedtuple('GroupTuple', 'face count')):

    # because face comes first in list of fields, we also get ordering
    # of groups, where those with highest face values come last

    @property
    def score(self):
        return self.face * self.count

    def __repr__(self):
        return 'Roll(%d * %d)' % (self.face, self.count)


def validate(dice_str):
    if len(dice_str) != 5:
        raise ValueError('length != 5')

    for die in dice_str:
        if die not in {str(valid) for valid in VALID_DICE}:
            raise ValueError("die '%s' not valid" % (die,))

    return {
        Group(int(char), dice_str.count(char))
        for char in dice_str
    }


def _single(roll, numerator):
    return {group for group in roll if group.face == numerator}

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
    return {Group(group.face, n) for group in roll if group.count >= n}

def _pairs(roll):
    return _n_of_kind(roll, 2)

def _get_highest(roll):
    return {sorted(roll)[-1]} if roll else set()

def pair(roll):
    return _get_highest(_pairs(roll))

def three_of_kind(roll):
    return _n_of_kind(roll, 3)

def four_of_kind(roll):
    return _n_of_kind(roll, 4)


def _get_two_highest(roll):
    max_two = sorted(roll, reverse=True)[0:2]
    return [
        die for die in roll
        if len(max_two) == 2 and die in max_two
    ]

def two_pairs(roll):
    return _get_two_highest(_pairs(roll))

def _exact_match(roll, faces):
    return roll if {group.face for group in roll} == faces else set()

def small_straight(roll):
    return _exact_match(roll, {1, 2, 3, 4, 5})

def large_straight(roll):
    return _exact_match(roll, {2, 3, 4, 5, 6})


def full_house(roll):
    return roll if {group.count for group in roll} == {2, 3} else set()

def yahtzee(roll):
    return {Group(50, 1)} if _n_of_kind(roll, 5) else {}

def chance(roll):
    return roll


def score(dice, category):
    return sum(group.score for group in category(validate(dice)))

