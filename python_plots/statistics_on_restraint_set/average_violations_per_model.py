'''
Used this script to get out the number of
dihedral angle violations over resp. 1, 3 and 5
degrees. First splitted the structure in ccpn in
15 different models (structures 53-67).

'''


from ccpnmr.analysis.core import ConstraintBasic
import numpy as np


def average_violations_per_model(argServer):

    project = argServer.getProject()
    nmrProject = project.findFirstNmrProject()
    store_serial = 65   #Dihedral angles
    nmrConstraintStore = nmrProject.findFirstNmrConstraintStore(serial=store_serial)
    allConstraintLists = nmrConstraintStore.constraintLists

    molSystem = project.findFirstMolSystem(code='MS1')
    print molSystem

    print molSystem.structureEnsembles

    structures = []
    for key in range(53, 68): #Splitted models
        structures.append(molSystem.findFirstStructureEnsemble(ensembleId=key))
    print structures

    bigger1_counts = []
    bigger3_counts = []
    bigger5_counts = []

    for structure in structures:

        bigger1 = 0
        bigger3 = 0
        bigger5 = 0

        for constraintList in allConstraintLists: #Only have one list in this case
            print constraintList

            violationList = ConstraintBasic.getStructureViolations(constraintList, structure)
            for violation in violationList.violations:
                if violation.violation > 1:
                    bigger1 +=1
                if violation.violation > 3:
                    bigger3 += 1
                if violation.violation > 5:
                    bigger5 +=1

        bigger1_counts.append(bigger1)
        bigger3_counts.append(bigger3)
        bigger5_counts.append(bigger5)

    print bigger1_counts
    print bigger3_counts
    print bigger5_counts
    print '----'
    for counts in [bigger1_counts, bigger3_counts, bigger5_counts]:
        print '---'
        print np.mean(counts)
        print np.std(counts)

