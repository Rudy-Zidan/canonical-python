import data1
import data2
import data3

# Return true if person exist in a team or in a nested teams
def contains(target, list):
    flag = False
    for member in list:
        if member.members != None:
            if contains(target, member.members):
                return True
            else:
                flag = False
        elif member == target:
            return True

    return flag

# Return a list of teams related to a person
def exercise1(person, list):
    result = []
    for item in list:
        if item.members == None:
            continue

        if contains(person, item.members):
            result.append(item)

    return result

# Return all the people inside a team
# Handle nested teams
def get_people(team):
    people = []

    if team == None or team.members == None:
        return people

    members = team.members
    team.members = []

    for member in members:
        if member.members == None:
            people.append(member)
        else:
            people = people + get_people(member)

    return people

## Task one

# Write a function that accepts a person and a list of all
# people/teams and returns a list of all the teams of which that
# person is a member. You can import the "people" list from
# `data1.py` to use as example data when writing your function.

# output should be:
# ['The A-Team', 'The C-Team']

print [t.displayname for t in exercise1(data1.alice, data1.people)]

## Task two

# Does your function produce the same results as expected in
# question 1 when you pass it the "people" list from `data2.py`
# and alice (also from `data2.py`)?  If not, modify your function
# so that it works correctly given that data.

# output should be:
# ['The A-Team', 'The C-Team']

print [t.displayname for t in exercise1(data2.alice, data2.people)]

## Task three

# Write a function that gets all the people (not teams) who are
# direct and indirect members of a team.  Using `data2.py`, this code
# (where your function is named `get_people`)...

# output should be:
# ['Alice', 'Bob', 'Carlos', 'Charlie', 'Eve']

print sorted(p.displayname for p in get_people(data2.c_team))

# Now look at `data3.py`.  Figure out what the correct answer should be for
# `get_members(data3.c_team)`, and make sure your function performs as you
# expect.

# output should be:
# ['Alice', 'Bob', 'Carlos', 'Charlie', 'Eve', 'Peggy', 'Trent', 'Victor']

print sorted(p.displayname for p in get_people(data3.c_team))
