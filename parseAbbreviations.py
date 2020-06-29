def make_definition(acronym, definition):
    return "*[{}]: {}".format(acronym, definition)


def make_table(a, b):
    return "| {} | {} |".format(a, b)


abbreviations = {}

with open('abbreviations') as file:
    for line in file:
        acronym, definition = line.split(' == ')
        abbreviations[acronym.strip()] = definition.strip()


for k in sorted(abbreviations.keys()):
    print(make_table(k, abbreviations[k]))

for k in sorted(abbreviations.keys()):
    print(make_definition(k, abbreviations[k]))
