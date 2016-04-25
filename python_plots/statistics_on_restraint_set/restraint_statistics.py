

def print_stats(argServer):

    project = argServer.getProject()
    nmrProject = project.findFirstNmrProject()
    store_serial = 64
    nmrConstraintStore = nmrProject.findFirstNmrConstraintStore(serial=store_serial)
    allConstraintLists = nmrConstraintStore.constraintLists

    constraintsC = []
    constraintsH = []

    for constraintList in allConstraintLists:
        if 'REJECT' in constraintList.name:
            continue
        print constraintList.findFirstExperiment().name

        if get_isotope(constraintList) == '1H':
            constraintsH.extend(constraintList.constraints)
        elif get_isotope(constraintList) == '13C':
            constraintsC.extend(constraintList.constraints)

        print_info(constraintList.constraints)

    print 'All H-detected'
    print_info(constraintsH)
    print 'All C-detected'
    print_info(constraintsC)
    print 'All'
    print_info(constraintsH+ constraintsC)




def print_info(constraints):

    print len(constraints)

    upper_limits = divide_by_upper_limit(constraints)
    for l in (3.5, 5.5, 8.0):
        print len(upper_limits.get(l, [])) or ''

    constraints_by_range = divide_constraints_in_ranges(constraints)
    for constraints_in_range in constraints_by_range:
        print len(constraints_in_range)
    unambiguous = get_unambiguous(constraints)
    unique = get_unique_constraints(constraints)
    long_range = constraints_by_range[3]


    print len(unambiguous)                                   # unambiguous
    print len(unique)                                        # unique
    #print len(unique.intersection(unambiguous))              # unique and unambiguous
    print len(unique.intersection(long_range))               # unique and long range
    print len(unique.intersection(long_range, unambiguous))  # unique and long range and unambiguous



    #print len(get_unique_items(constraintList.constraints))                    # All unique
    #print len(get_unique_items(unambiguous))                                   # Unique and unambiguous
    #print len(get_unique_items(divide_constraints_in_ranges(unambiguous)[3]))  # Unambiguous and unique and long range



def get_isotope(constraintList):

    c = constraintList.findFirstConstraint()
    item = c.findFirstItem()
    resonance = item.findFirstResonance()
    return resonance.isotopeCode


def get_unambiguous(constraints):
    unambiguous = set()
    for constraint in constraints:
        if len(constraint.items) == 1:
            unambiguous.add(constraint)
    return unambiguous


def divide_constraints_in_ranges(constraints):

    ranges = [[], [], [], []]
    for constraint in constraints:
        ranges[get_range_for_constraint(constraint)].append(constraint)
    return ranges

def get_range_for_constraint(constraint):
    ranges = []
    for item in constraint.items:
        ranges.append(get_range_for_item(item))
    return min(ranges)
    #average_distance = sum(ranges)/float(len(ranges))
    #if average_distance == 0:
    #    return 0
    #elif average_distance < 2.0:
    #    return 1
    #elif average_distance <3.0:
    #    return 2
    #else:
    #    return 3
    #return max(set(ranges), key=ranges.count)


def get_range_for_item(item):

    fixedResonance1, fixedResonance2 = item.resonances
    residue1 = fixedResonance1.resonanceSet.findFirstAtomSet().findFirstAtom().residue
    residue2 = fixedResonance2.resonanceSet.findFirstAtomSet().findFirstAtom().residue
    seqCode1 = residue1.seqCode
    seqCode2 = residue2.seqCode

    sequence_distance = abs(seqCode1-seqCode2)
    if sequence_distance == 0:
        return 0
    elif sequence_distance == 1:
        return 1
    elif sequence_distance <= 4 :
        return 2
    else:
        return 3


def get_unique_items(constraints):

    unique_items = set()

    for constraint in constraints:
        for item in constraint.items:
            resonanceA, resonanceB = item.resonances
            key = tuple(sorted([resonanceA.serial, resonanceB.serial]))
            unique_items.add(key)
    return unique_items


def get_unique_constraints(constraints):

    pairs = set()
    unique_constraints = set()
    for constraint in constraints:
        pair = get_resonance_pairs(constraint)
        if pair not in pairs:
            unique_constraints.add(constraint)
            pairs.add(pair)
    return unique_constraints



def get_resonance_pairs(constraint):
    items = []
    for item in constraint.items:
        items.append(get_resonance_pair(item))
    return tuple(sorted(items))


def get_resonance_pair(item):

    resonanceA, resonanceB = item.resonances
    return tuple(sorted([resonanceA.serial, resonanceB.serial]))


def divide_by_upper_limit(constraints):

    limits_dict = {}
    for constraint in constraints:
        limit = constraint.upperLimit
        if limit not in limits_dict:
            limits_dict[limit] = [constraint]
        else:
            limits_dict[limit].append(constraint)
    return limits_dict



