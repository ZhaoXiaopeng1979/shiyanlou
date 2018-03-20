#from thrift import Thrift
#from thrift.transport import TSocket, TTransport
#from thrift.protocol import TBinaryProtocol
#from hbase import Hbase
#from hbase.ttypes import Mutation
from collections import OrderedDict
import datetime

a = 
'''

try:
    with open('/home/tongjl/ismgenerator/data/txt/ismfactors.20180316') as f:
        contents = f.readlines()
        index_ism = OrderedDict()
        for content in contents[1:]:
            ismcode = content.split('|')[0][2:]
            ism = content[2:-3] 
            index_ism[ismcode] = ism
 
except FileNotFoundError:
    print("File not found")

'''
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

'''
