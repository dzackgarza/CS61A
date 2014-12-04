# Pull html pages
# import requests

# Parse html into trees
from lxml import html

# Flatten lists
import itertools

# Perform regex matches
import re


# Represents an entire department and all of its classes
class Department:
    dotfile = ""
    name = "Department Name"
    dept_classes = {}  # Map: "Class_Code" -> BerkeleyClass

    def __init__(self, name, initial_list={}):
        # Todo: Handle duplicates
        self.dept_classes = initial_list

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def set_dotfile(self, string):
        self.dotfile = string

    def write_dotfile(self):
        if self.dotfile == "":
            print("Dot file must be added with set_dotfile() before writing.")
        else:
            with open("out.dot", 'w') as outfile:
                outfile.write(self.dotfile)

    def add_class(self, new_class):
        if new_class not in self.dept_classes:
            self.dept_classes.append(new_class)

    def print_classes(self):
        for c in self.dept_classes:
            print(c)
        return None


# Represents a single class and all of its prerequisites
class BerkeleyClass:
    code = "0000"
    title = "default class"
    units = "(0)"
    description = "default description"
    all_prereq_codes = []  # List of strings
    internal_prereqs = []  # List of BerkeleyClass
    external_prereqs = []  # List of BerkeleyClass

    def __init__(self, code, title, units, prereq_codes):
        self.code = code
        self.title = title
        self.units = units
        self.all_prereq_codes = prereq_codes

    def __str__(self):
        return "Class: " + self.title +\
            "Code: " + self.code +\
            "CS Prereqs: " + str(self.internal_prereqs) +\
            "External prereqs: " + str(self.external_prereqs)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other_class):
        return self.code == other_class.code

# Get html from file
with open("file.html", "r") as myfile:
    page = myfile.read()
tree = html.fromstring(page)

# Get html file from url
# page = requests.get('http://general-catalog.berkeley.edu/catalog/gcc_list_crse_req?p_dept_name=Computer+Science&p_dept_cd=COMPSCI&p_path=l')
# tree = html.fromstring(page.text)

# Pull out all of the paragraph blocks - each block contains a class description
blocks = tree.xpath('/html/body/table[3]/tbody/tr/td[2]/font/p')

# Filter out the blocks without prerequisites - this just
# serves to get rid of extra blocks that don't contain a
# class desc, Classes without prereqs have the
# text "Prerequisite: None" or something similar.
prereq_blocks = [b for b in blocks if "Prereq" in b.text_content()]

# Since there's only one <b> per block, and it contains
# all the info we need, grab all the <b> blocks
titles = [b.xpath('b') for b in prereq_blocks]

# Collapse list, since titles looks like [ [<b>], [<b>], ...]
merged_titles = list(itertools.chain.from_iterable(titles))

# <i> tags contain the prerequisite information, but
# blocks may have multiple italicized tags
prereqs = []
possible_prereq_chunks = [b.xpath('i') for b in prereq_blocks]

# Keep only the <i> blocks that contain the word "Prerequisite"
for p in possible_prereq_chunks:
    for p2 in p:
        if "Prerequisite" in p2.text_content():
            prereqs.append(p2)

# There should be exactly as many descriptions as classes
assert(len(prereqs) == len(merged_titles))

# Map titles to prerequisites: String => String
dict = {}
for i in range(0, len(merged_titles)):
    dict[merged_titles[i].text_content()] = prereqs[i].text_content()

# Lookup table for numeric class codes. String => BerkeleyClass
class_codes = {}


# Get relevant info from string blobs
def parse_class_text(title_string, prereq_string):
    code, title, units = title_string.split('.')
    pre = re.findall('\d+[A-Z]*', prereq_string)
    return code, title, units, pre

# Populate class code lookup table
for d in dict.keys():
    code, title, units, prereq_codes = parse_class_text(d, dict[d])
    class_codes[code] = BerkeleyClass(code, title, units, prereq_codes)

# Populate the prerequisite list for each class
for this_class in class_codes.values():

    # Counteracts weird bug that picks up prereqs from list iterated class
    this_class.internal_prereqs = []
    this_class.external_prereqs = []
    unknown_prereqs = []

    # Juuuust to be sure..
    assert(len(unknown_prereqs) == 0)
    assert(len(this_class.internal_prereqs) == 0)

    # Add all of the known classes (within department) to prereqs
    for s in this_class.all_prereq_codes:
        if s in class_codes.keys():
            this_class.internal_prereqs.append(s)

    # Make a list of all prereqs that weren't found in the lookup table
    unknown_prereqs = [l for l in this_class.all_prereq_codes
                       if l not in this_class.internal_prereqs]

    # Make sure no classes were lost
    assert(len(this_class.internal_prereqs) + len(unknown_prereqs)
           == len(this_class.all_prereq_codes))

    # Keep track of all of the classes that weren't found
    this_class.external_prereqs = [u for u in unknown_prereqs]

lower, upper, grad = [], [], []

# Start building string that will go into the dotfile
prefix = "digraph g {\n"\
    + "ratio=fill;\n"\
    + "graph [ size = \"25,25\", ranksep=5 ];"

l_class_strs, u_class_strs, g_class_strs = [], [], []

# Build the edge list
for c in class_codes.values():

    # Since the var is being reused, make sure it's empty
    node = []
    strs = []
    assert(len(node) == 0)

    # Sort out the upper/lower divs and grad classes
    if c.code[0] == '2':
        node = grad
        strs = g_class_strs
    elif c.code[0] == '1':
        node = upper
        strs = u_class_strs

    # Possibly an alternate version of a course
    elif c.code[0].isalpha():
        if c.code[1] == '2':
            node = grad
            strs = g_class_strs
        elif c.code[1] == '1':
            node = upper
            strs = u_class_strs
        else:
            node = lower
            strs = l_class_strs
    else:
        node = lower
        strs = l_class_strs

    if c.internal_prereqs != []:
        if c.code not in strs:
            # print("Strs contains " + str(strs))
            strs.append(c.code)

    # Create the string the will represent this prereq
    # relationship as an edge between nodes
    for p in c.internal_prereqs:
        node_str = "  \"" + str(c.code) + "\" -> \"" + str(p) + "\";"
        # node_str += " [minlen=2]" if p[0] < c.code[0] else " [constrain=false]"
        node.append(node_str)
        node_str = ""

l_class_strs_set = set(l_class_strs)
u_class_strs_set = set(u_class_strs)
g_class_strs_set = set(g_class_strs)

l_rank_equalizer = "{ rank=same; "
for l in l_class_strs_set:
    l_rank_equalizer += "\"" + l + "\"; "
l_rank_equalizer += "}\n"

u_rank_equalizer = "{ rank=same; "
for u in u_class_strs_set:
    u_rank_equalizer += "\"" + u + "\"; "
u_rank_equalizer += "}\n"

g_rank_equalizer = "{ rank=same; "
for g in g_class_strs_set:
    g_rank_equalizer += "\"" + g + "\"; "
g_rank_equalizer += "}\n"

# Create subgraphs corresponding to each division of classes
# Then, build the appropriate substring
"""lower_cluster = "\nsubgraph cluster_0 {\n" \
    + "label=\"Lower Division\"\n" \
    + "style=filled;\n" \
    + "node[style=filled];\n" \
    + "\n".join(lower) + "}\n"

upper_cluster = "\nsubgraph cluster_1 {\n" \
    + "label=\"Upper Division\"\n" \
    + "style=filled;\n" \
    + "node[style=filled];\n" \
    + "\n".join(upper) + "}\n"

grad_cluster = "\nsubgraph cluster_2 {\n" \
    + "label=\"Graduate\"\n" \
    + "style=filled;\n" \
    + "node[style=filled];\n" \
    + "\n".join(grad) + "}\n"
"""
lower_cluster = "\n".join(lower) + "\n"
upper_cluster = "\n".join(upper) + "\n"
grad_cluster = "\n".join(grad) + "\n"
postfix = "\n}"

# Cat all the substrings into the final dot file representation
final = prefix + \
    l_rank_equalizer + lower_cluster + \
    u_rank_equalizer + upper_cluster + \
    g_rank_equalizer + grad_cluster + \
    postfix

# Send the string to stdout for piping
print(final)

computerScienceDept = Department("Computer Science", class_codes)
computerScienceDept.set_dotfile(final)
# computerScienceDept.write_dotfile()

"""
from cStringIO import StringIO
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pydot


def send_image(graph):
    png_str = graph.create_png(prog='dot')
    sio = StringIO()
    sio.write(png_str)
    sio.seek(0)
    img = mpimg.imread(sio)
    imgplot = plt.imshow(img, aspect='equal')
    plt.show(block=False)

g = pydot.graph_from_dot_file('./out.dot')
g.set_node_defaults(shape='circle', fixedsize='true', height=.85, fontsize=24)
# send_image(g)
g.write_png('output_graph.png_strg', prog='dot')
"""
