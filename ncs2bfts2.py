"""
    Author: Placid Unegbu
    Version: 2
"""


from collections import OrderedDict
import os
import neuralynx_io
import numpy
import pandas as pd

def ncs2bfts(startDateTime, dirName, fileNum, bfFile):
    
    
    """
        This codes loads a Neuralynx .ncs file and returns a Blackfynn .bfts file.

        Inputs:
        
        startDateTime (float): in epoch microseconds
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
        rawDataNew = rawData[0:len(rawData):10] # downsample to 3kHz
        chls.update({'channel_'+str(i):rawDataNew})

    totalSamples = len(rawDataNew)
    timeStamp = ncs['timestamp'] + startDateTime
    timeVec = numpy.linspace(timeStamp[0],timeStamp[-1],totalSamples) # make a time vector equal to size of the raw data
    
    toBF = OrderedDict()
    toBF['timeStamp'] = numpy.int64(timeVec)
    toBF.update(chls)

    df = pd.DataFrame(toBF)
    df.to_csv(bfFile,index=False)
