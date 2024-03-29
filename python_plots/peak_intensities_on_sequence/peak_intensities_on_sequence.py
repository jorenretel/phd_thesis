
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import math
import random
import matplotlib.gridspec as gridspec

#sns.set(style="white")
#sns.set_style("ticks")
sns.set(font='sans-serif')

#from matplotlib.font_manager import findfont, FontProperties

#print FontProperties()
#print findfont(FontProperties(family=['serif']))

def make_intensity_histogram(argServer):
    project = argServer.getProject()
    nmrProject = project.findFirstNmrProject()

    residues = project.findFirstMolSystem(name='MS1').findFirstChain().sortedResidues()


    #nmrConstraintStore = project.newNmrConstraintStore(nmrProject=nmrProject)

    #f, (ax1) = plt.subplots(1, 1, figsize=(8, 6), sharex=True)


    f, axes = plt.subplots(8, 1,figsize=(10, 12))#, sharey=True)

    #axese = [item for sublist in axes for item in sublist]

    gs = gridspec.GridSpec(7, 2,
                           width_ratios=[1,1],
                           height_ratios=[4,4,4,4,7,4,4])

    axese = []

    axese.append(plt.subplot(gs[0, 0]))
    axese.append(plt.subplot(gs[1, :]))
    axese.append(plt.subplot(gs[2, :]))
    axese.append(plt.subplot(gs[3, :]))
    axese.append(plt.subplot(gs[4, :]))
    axese.append(plt.subplot(gs[5, :]))
    axese.append(plt.subplot(gs[6, :]))
    axese.append(plt.subplot(gs[0, 1]))

    #axese.append(plt.subplot2grid((7,2), (0,0), colspan=1))
    #axese.append(plt.subplot2grid((7,2), (1,0), colspan=2))
    #axese.append(plt.subplot2grid((7,2), (2,0), colspan=2))
    #axese.append(plt.subplot2grid((7,2), (3,0), colspan=2))
    #axese.append(plt.subplot2grid((7,2), (4,0), colspan=2))
    #axese.append(plt.subplot2grid((7,2), (5,0), colspan=2))
    #axese.append(plt.subplot2grid((7,2), (6,0), colspan=2))
    #axese.append(plt.subplot2grid((7,2), (0,1), colspan=1))



    res_ranges = [range(1, 24)]
    res_ranges.append(range(24, 60))
    res_ranges.append(range(60, 102))
    res_ranges.append(range(102, 143))
    res_ranges.append(range(143, 183))
    res_ranges.append(range(183, 224))
    res_ranges.append(range(224, 264))
    res_ranges.append(range(264, 282))

    expNames = ['240_CANH2014', '245_CAcoNH2014', '307_CBcaNH', '316_CBcacoNH']
    colors = ['#4daf4a', '#984ea3', '#377eb8', '#e41a1c']
    normalization = [1, 1, 1, 1]
    peakListSerial = 1

    intensities = []

    for expName, color, norm in zip(expNames, colors, normalization):
        print expName
        xys = get_values_for_experiment(nmrProject=nmrProject,
                                        expName=expName,
                                        peakListSerial=peakListSerial,
                                        measurement='height')
        intensities.append(xys)
        # for axe, res_range in zip(axese, res_ranges):

        #     xs = []
        #     ys = []
        #     for i in res_range:
        #         if i in xys:
        #             ys.append(xys[i] * norm)
        #             xs.append(i)
        #         else:
        #           ys.append(None)
        #           xs.append(i)

        #     axe.scatter(xs, ys, color=color)
        #     #axe.plot(xs, ys, color=color)
        #     axe.set_xlim([res_range[0],res_range[-1]])



    for axe, res_range in zip(axese, res_ranges):

        xs = []
        ys = []

        for i in res_range:

            av = sum([res_dict.get(i, 0) for res_dict in intensities])
            ccpCode = residues[i-1].ccpCode
            ccpCode_next = None
            if i < len(residues):
                ccpCode_next = residues[i].ccpCode
            if i == len(residues) or ccpCode == 'Pro' or ccpCode == 'Gly' or ccpCode_next == 'Pro':
                av = av/2.0
            else:
                av = av/4.0

            if av != 0.0:
                ys.append(av)
                xs.append(i)
            else:
                ys.append(None)
                xs.append(i)

        axe.plot(xs, ys, color='grey', zorder=1)
        #axe.plot([res_range[0], res_range[-1]], [4,4], color='black')
        axe.set_xticks([i for i in res_range if i%2==0])
        axe.set_xlabel('residues')
        axe.set_ylabel('S/N')

        max_point = 30

        for res_dict, color in zip(intensities, colors):

            xs = []
            ys = []
            for i in res_range:
                if i in res_dict:
                    ys.append(res_dict[i])
                    xs.append(i)
                else:
                  ys.append(None)
                  xs.append(i)

            max_point = max(ys + [max_point])

            axe.scatter(xs, ys, color=color, zorder=2)
            #axe.plot(xs, ys, color=color)
        axe.set_xlim([res_range[0],res_range[-1]])

        #current = axe.get_ylim()[1]
        #print current
        #axe.set_ylim(0, max([current, 40]))

        print max_point

        max_point = (int(max_point+1)/10)*10 +10

        axe.set_ylim(0, max_point)
        axe.yaxis.set_ticks(range(0, max_point+1, 10))

    plt.tight_layout()
    axese[4].set_ylim()
    axese[4].yaxis.set_ticks(range(0, 71, 10))
    plt.savefig('/home/joren/peak_intensities_on_sequence.svg')


def get_values_for_experiment(nmrProject, expName, peakListSerial, measurement='height'):
    experiment = nmrProject.findFirstExperiment(name=expName)
    spectrum = experiment.findFirstDataSource()
    peakList = spectrum.findFirstPeakList(serial=peakListSerial)
    noise_level = getNoiseEstimate(spectrum)
    print noise_level

    xys = {}

    for peak in peakList.peaks:
        peakdims = peak.sortedPeakDims()

        for dim in peakdims:

            contribs = dim.sortedPeakDimContribs()

            #if len(contribs) == 1 and contribs[0].resonance.isotopeCode == '13C':
            for contrib in contribs:
                #resonance = contribs[0].resonance
                resonance = contrib.resonance
                #print resonance.isotopeCode
                if resonance.resonanceGroup and resonance.isotopeCode == '13C':
                    if resonance.resonanceGroup.residue:

                        seqCode = resonance.resonanceGroup.residue.seqCode
                        if measurement == 'height':
                            height = peak.findFirstPeakIntensity(intensityType='height').value
                            xys[seqCode] = (height / noise_level) / len(contribs)
                        elif measurement ==  'linewidth':
                            xys[seqCode] = dim.lineWidth

    return xys






def getNoiseEstimate(dataSource, nsamples=1000, nsubsets=10, fraction=0.1):
  """
  Estimate the noise level for a spectrum by choosing a random nsamples points
  and finding subsets with the lowest standars devation/

  .. describe:: Input

  Nmr.DataSource, Int, Int, Float

  .. describe:: Output

  Float
  """

  sqrt = math.sqrt
  data = get_sample_intensities_from_data_source(dataSource, nsamples)

  if not data:
    return 1.0

  elif len(data) < 10:
    maxvalue = max([abs(x) for x in data])
    if maxvalue > 0:
      return 0.1 * maxvalue
    return 1.0

  minStd = None
  for i in range(nsubsets):
    subset = getRandomSubset(data, fraction)

    avg = float(sum(subset)) / len(subset)
    std = sqrt(sum([(amp-avg)**2 for amp in subset])/float(len(subset)))

    if (minStd is None) or std < minStd:
      minStd = std

  # multiplier a guess
  #minStd = 1.3 * minStd

  minStd *= dataSource.scale

  return abs(minStd)


def get_noise_sparky(dataSource, nsamples=10000):
  '''This is the method used by sparky to determine
     the level of the noise and given slightly
     different values for the noise.
     It just picks a number of points and returns
     the median intensity.

  '''
  noise = 1.0
  data = get_sample_intensities_from_data_source(dataSource, nsamples)
  if data:
    data = [abs(point) for point in data]
    data.sort()
    noise = data[int(len(data)/2.0)]
  return noise


def getRandomSubset(data, fraction):
  """
  Function used by getNoiseEstimate()

  .. describe:: Input
  .. describe:: Output

  """

  return random.sample(data, int(len(data)*fraction))


def get_sample_intensities_from_data_source(dataSource, nsamples):
  '''Returns a list of nsamples with intensities at randomly
     choosen points in the spectrum.

  '''

  data = []

  if not hasattr(dataSource, 'block_file') or not dataSource.block_file:
    return data

  block_file = dataSource.block_file
  npts = [dataDim.numPoints for dataDim in dataSource.sortedDataDims()]

  fails = 0
  for i in range(nsamples):
    pt_index = [random.randint(0, n-1) for n in npts]

    try:
      data.append(float(block_file.getPointValue(pt_index)))
    except(ApiError, ValueError):
      fails += 1

  if fails:
    msg = "Attempt to access %d non-existent data points in spectrum %s:%s"
    print msg % (fails, dataSource.experiment.name, dataSource.name)

  return data