"""
    Author: Placid Unegbu
    Version: 1
"""


import neuralynx_io
import numpy
from matplotlib import pyplot as plt
from scipy.signal import decimate
import pandas as pd
import os
from collections import OrderedDict



def ncs2bfts(dirName, fileNum, bfFile):
    
    
    """
        This codes loads a Neuralynx .ncs file and returns a Blackfynn .bfts file.

        Inputs
        dirName (string): directory of where .ncs files are stored
            example, dirName = 'C:\user\username\ncsdirectory'
        fileNum (vector): channels numbers
            example, if .ncs files are saved as CSC57.ncs, CSC59.ncs
            fileNum = [57, 59];
        bfFile (string): name of generated .bfts file

    """

    chls = OrderedDict() # dictionary to store channel values
    for i in fileNum:
        fileSelect = 'CSC'+str(i)+'.ncs'
        fileName = os.path.join(dirName, fileSelect) # create a full filepath pointing to the neuralynx .ncs datafile

        ncs = neuralynx_io.load_ncs(fileName) # import neuralynx data. NOTE: import stores information as a dictionary

        sampleRate = ncs['sampling_rate'] 
        rawData = ncs['data']
        rawDataNew = decimate(rawData,10,n=10,ftype='fir',zero_phase=True) # downsample to 3kHz
        chls.update({'channel_'+str(i):rawDataNew})

    totalSamples = len(rawData)
    timeStamp = ncs['timestamp']
    maxTime = timeStamp[-1]
    timeVec = numpy.linspace(0,maxTime,totalSamples) # make a time vector equal to size of the raw data
    timeVecNew = decimate(timeVec,10,n=10,ftype='fir',zero_phase=True)

    toBF = OrderedDict()
    toBF['timeStamp'] = timeVecNew
    toBF.update(chls)

    df = pd.DataFrame(toBF)
    df.to_csv(bfFile)
