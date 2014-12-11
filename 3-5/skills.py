import copy


class Programmer:
    name = "Foo Bargrammer"
    skills = {}

    def __init__(self, skills, name="Foo Bargrammer"):
        self.skills = copy.deepcopy(skills)
        self.name = name

    def level_up(self, skillName):
        if skillName in self.skills.keys():
            print("Skill found. Previous level: "
                  + str(self.skills[skillName].level))
            self.skills[skillName].increase()
            print("New skill level: ", self.skills[skillName].level)
        else:
            print("This person does not have that skill.")

    def list_skills(self):
        print("~_~_~_~_~~_~_~", self.name, "'s Skills ~_~_~_~_~~_~_~")
        for skill in self.skills.keys():
            print(self.skills[skill].type, ":", self.skills[skill].level)
            self.skills[skill].print_note()
        print("~_~_~_~_~~_~_~~_~_~_~_~~_~_~~_~_~_~_~~_~_~\n")


class Skill:
    level = 0
    type = "Existing"
    note = None

    def __init__(self, note, type="Existing"):
        self.type = type
        self.note = note

    def increase(self):
        self.level += 1

    def print_note(self):
        print(self.note.description)


class Note:
    description = "default"

    def __init__(self, desc="default"):
        self.description = desc


# Create several sample Skills with Notes
skills = {}

sql_note = Note("SQL is a database query language.")
sql_skill = Skill(sql_note, "SQL")

perl_note = Note("Perl is an ancient language, incomprehensible to modern man.")
perl_skill = Skill(perl_note, "Perl")

# Create Skills with Notes, then pass them in. Use the name of the skill as the key.
bob = Programmer({"SQL": sql_skill, "Perl": perl_skill}, "Bob")
joe = Programmer({"SQL": sql_skill}, "Joe")

# Test to see if the skills are unique to whomever has them
bob.level_up("SQL")
bob.level_up("SQL")
bob.level_up("SQL")

joe.level_up("SQL")

# Bob should be level 3, Joe should be level 1
bob.list_skills()
joe.list_skills()
