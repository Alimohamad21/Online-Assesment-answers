class Character:
    def __init__(self, char):
        self.dupe = False
        self.char = char


def duplicateCharacters(input):
    characters = []
    for i in range(len(input)):
        flag = False
        for c in characters:
            if c.char == input[i]:
                flag = True
                break
        if flag:
            continue
        character = Character(input[i])
        characters.append(character)
        for j in range(i + 1, len(input)):
            if input[i] == input[j]:
                character.dupe = True
    total_dupes = 0
    for c in characters:
        if c.dupe:
            total_dupes += 1
    return total_dupes


def secondHighestDigit(input):
    nums = []
    for char in input:
        try:
            nums.append(int(char))
        except:
            pass
    if not nums or len(nums) == 1:
        return -1
    nums.sort()
    return nums[-2]


def flr(directions):
    angle = 90
    x = 0
    y = 0
    recalibrate_x = 0
    recalibrate_y = 0
    for i in range(len(directions)):
        if directions[i] == 'R':
            if angle == 0:
                angle = 270
            else:
                angle -= 90
        elif directions[i] == 'L':
            angle = (angle + 90) % 360
        elif directions[i] == 'F':
            if angle == 90:
                y += 1
            elif angle == 0:
                x += 1
            elif angle == 180:
                x -= 1
            elif angle == 270:
                y -= 1
    if x == 0 and y == 0:
        return 0
    if angle == 90 or angle == 270:
        if x:
            if angle == 0:
                recalibrate_x = 0 if x < 0 else 2
            elif angle == 90 or angle == 270:
                recalibrate_x = 1
            elif angle == 180:
                recalibrate_x = 0 if x > 0 else 2
            angle = 180 if x > 0 else 0
        if y:
            if angle == 90:
                recalibrate_y = 0 if y < 0 else 2
            elif angle == 0 or angle == 180:
                recalibrate_y = 1
            elif angle == 270:
                recalibrate_y = 0 if y > 0 else 2
    elif angle == 180 or angle == 0:
        if y:
            if angle == 90:
                recalibrate_y = 0 if y < 0 else 2
            elif angle == 0 or angle == 180:
                recalibrate_y = 1
            elif angle == 270:
                recalibrate_y = 0 if y > 0 else 2
            angle = 270 if y > 0 else 90
        if x:
            if angle == 0:
                recalibrate_x = 0 if x < 0 else 2
            elif angle == 90 or angle == 270:
                recalibrate_x = 1
            elif angle == 180:
                recalibrate_x = 0 if x > 0 else 2
    return abs(x) + abs(y) + recalibrate_x + recalibrate_y


