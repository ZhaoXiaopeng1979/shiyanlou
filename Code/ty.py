#from thrift import Thrift
#from thrift.transport import TSocket, TTransport
#from thrift.protocol import TBinaryProtocol
#from hbase import Hbase
from collections import OrderedDict

# 读取本地文件，并为Hbase存储做准备
try:
    with open('/home/shiyanlou/tongjl/ismgenerator/data/txt/ismfactors.20180313') as f:
        contents = f.readlines()
        index_ism = OrderedDict()
        for content in contents[1:]:
            ismcode = content.split('|')[0][2:]
            ism = content[2:-3] 
            index_ism[ismcode] = ism
        #print(index_ism)
        print(len(index_ism))
    with open('./data','w') as fw:
        for i in index_ism:
            fw.write(i+':'+index_ism[i]+'\n')
except FileNotFoundError:
    print("File not found")

finally:
    f.close()

'''
# 连接Hbase,并写入数据
try:
    
    transport = TSocket.TSocket('zpy11409.zpy.corp', 9090)
    
    transport.setTimeout(5000)
    
    trans = TTransport.TBufferedTransport(transport)
    
    protocol = TBinaryProtocol.TBinaryProtocol(trans)
    
    client = Hbase.Client(protocol)
    
    transport.open()
    
    table='ismfactor'
    
    from hbase.ttypes import Mutation
    
    mutations = [Mutation(column="ismfactor:ismfactor", value="99999999999999999999991")]
    
    client.mutateRow(table, '180313000000002',mutations)

except Exception, e:
    print('youcuo')
'''
