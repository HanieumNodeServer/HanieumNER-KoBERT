from gen_data_dasom import *
from gen_data_suhyeon import *

random.seed(1)

dasom_data = dasom()
suhyeon_data =  suhyeon()

bus_list = dasom_data + suhyeon_data

filePATH = 'data/gen_data/data'
with open(filePATH+'/data.txt', 'w', encoding = 'utf-8') as f:
    for b in bus_list:
        f.write(b+'\n')