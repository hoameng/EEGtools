from blackfynn import Blackfynn
from ncs2bfts2 import ncs2bfts
import datetime
bf = Blackfynn()

fileNum = [57,59,61,62,63] # number of the channel being recorded on
dirName = 'C:\Users\Placid\Dropbox\PTE_Data_Litt_Blackfinn\JAW_53_17_110217_2006_001' # directory of where data is stored
bfFile = 'datacheck.bfts'
startDateTime = ((datetime.datetime(2017,11,6,14,38,15) - datetime.datetime(1970,1,1)).total_seconds())*(1e6) # microseconds
ncs2bfts(startDateTime, dirName, fileNum, bfFile)

ds = bf.create_dataset('John Wolf Data')
ds.upload(bfFile)