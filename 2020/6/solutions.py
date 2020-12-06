def separate_records(lines):
    rec = []
    for line in lines:
        if line.strip():
            rec.append(line.strip())
        elif rec:
            yield rec
            rec = []
    if rec:
        yield rec

def sum_yes_answers_in_group(group):
    yes_answers = []
    for person in group:
        for answer in person:
            if answer not in yes_answers:
                yes_answers.append(answer)
    sum = len(yes_answers)
    return sum

# my initial answer
def get_unanimous_yes_answers(group):
    yes_answers = list(group[0])
    for person in group:
        next_yes_answers = []
        for answer in yes_answers:
            print("testing {}".format(answer))
            if answer in person:
                next_yes_answers.append(answer)
        yes_answers = next_yes_answers
    return len(yes_answers)

# but there's a better way!
def get_unanimous_yes_answers_with_sets(group):
    list_of_sets = []
    for person in group:
        list_of_sets.append(set(person))
    return len(set.intersection(*list_of_sets))

def get_input(filename):
    with open(filename, "r") as input_file:
        return separate_records(input_file.readlines())


groups = list(get_input("input.txt"))

print("The sum of all yes answers is {}".format(sum([sum_yes_answers_in_group(group) for group in groups])))

my_answer = [get_unanimous_yes_answers(group) for group in groups]
sets_answer = [get_unanimous_yes_answers_with_sets(group) for group in groups]
print("The sum of all unanimous yes answers is {}".format(sum(my_answer)))
print("The sum of all unanimous yes answers is {}".format(sum(sets_answer)))
