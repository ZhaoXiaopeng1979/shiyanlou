#from thrift import Thrift
#from thrift.transport import TSocket, TTransport
#from thrift.protocol import TBinaryProtocol
#from hbase import Hbase
#from hbase.ttypes import Mutation
from collections import OrderedDict
import sys
import json

filename = sys.argv[1]
print('From {} get the file'.format(filename))

# '/home/tongjl/ismgenerator/data/txt/ismfactors.20180316'
try:
    with open(filename) as f:
        contents = f.readlines()
        index_ism = OrderedDict()
        ism = OrderedDict()
        column = contents[0].split('|')
        column[0] = column[0][2:]
        column[-1] = column[-1][:-3]
        print(column)
        for content in contents[1:]:           
            ismcode = content.split('|')[0][2:]
            ism_data = content.split('|')
            ism_data[0] = ism_data[0][2:]
            ism_data[-1] = ism_data[-1][:-3]
            ism = dict(zip(column,ism_data))

            index_ism[ismcode] = ism
 
except FileNotFoundError:
    print("File not found")


try:
    data = json.dumps(index_ism)
    with open('./data','w') as wf:
        wf.write(data)

except FileNotFoundError:
    print("Write File failure")

'''
try:
    
    transport = TSocket.TSocket('zpy11409.zpy.corp', 9090)
    
    transport.setTimeout(5000)
    
    trans = TTransport.TBufferedTransport(transport)
    
    protocol = TBinaryProtocol.TBinaryProtocol(trans)
    
    client = Hbase.Client(protocol)
    
    transport.open()
    
    table='ismfactor'
    
    for i in index_ism:
    
        mutations = [Mutation(column="ismfactor:ismfactor", value=index_ism[i])]
    
        client.mutateRow(table, i,mutations)

except Exception, e:
    print('youcuo')

print('Finish put data to Hbase')

'''

