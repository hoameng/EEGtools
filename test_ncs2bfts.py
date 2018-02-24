from blackfynn import Blackfynn
from ncs2bfts import ncs2bfts
bf = Blackfynn()

fileNum = [57,59,61,62,63] # number of the channel being recorded on
dirName = 'C:\Users\Placid\Dropbox\PTE_Data_Litt_Blackfinn\JAW_53_17_110217_2006_001' # directory of where data is stored
dataFile = 'datacheck.bfts'
ncs2bfts(dirName, fileNum,dataFile)

ds = bf.create_dataset('John Wolf Data')
ds.upload(dataFile)