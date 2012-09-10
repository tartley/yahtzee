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


class Roll(object):

    def __init__(self, groups=set()):
        self.groups = (
            validate(groups) if isinstance(groups, str) else set(groups)
        )

    def __iter__(self):
        return iter(self.groups)

    def __len__(self):
        return len(self.groups)

    @property
    def score(self):
        return sum(group.score for group in self.groups)

    def filter_by_face(self, face):
        return Roll(group for group in self if group.face == face)

    def filter_by_count(self, count):
        return Roll(
            Group(group.face, count)
            for group in self if group.count >= count
        )

    def pairs(self):
        return self.filter_by_count(2)

    def get_n_highest(self, n):
        max_n = sorted(self, reverse=True)[0:n]
        return Roll(
            die for die in self
            if len(max_n) == n and die in max_n
        )


def validate(dice_str):
    if len(dice_str) != 5:
        raise ValueError('length != 5')

    for die in dice_str:
        if die not in {str(valid) for valid in VALID_DICE}:
            raise ValueError("die '%s' not valid" % (die,))

    return {
        Group(int(char), dice_str.count(char))
        for char in set(dice_str)
    }



# categories

def ones(roll):
    return roll.filter_by_face(1)

def twos(roll):
    return roll.filter_by_face(2)

def threes(roll):
    return roll.filter_by_face(3)

def fours(roll):
    return roll.filter_by_face(4)

def fives(roll):
    return roll.filter_by_face(5)

def sixes(roll):
    return roll.filter_by_face(6)


def pair(roll):
    return roll.pairs().get_n_highest(1)

def three_of_kind(roll):
    return roll.filter_by_count(3)

def four_of_kind(roll):
    return roll.filter_by_count(4)


def two_pairs(roll):
    return roll.pairs().get_n_highest(2)


def _exact_match(roll, faces):
    return roll if {group.face for group in roll} == faces else Roll()

def small_straight(roll):
    return _exact_match(roll, {1, 2, 3, 4, 5})

def large_straight(roll):
    return _exact_match(roll, {2, 3, 4, 5, 6})


def full_house(roll):
    return roll if {group.count for group in roll} == {2, 3} else Roll()

def yahtzee(roll):
    return Roll({Group(50, 1)} if roll.filter_by_count(5) else Roll())

def chance(roll):
    return roll


def score(dice, category):
    return category(Roll(dice)).score

