
class hproxy(object):
    keepalive = 10  # default keepalive timmer
    #timesinceping   # host unix time, used to detect disconects
    #topics = ()     # used to store currently subscribed topics
    #debug = False   # should output debug messages
    address='127.0.0.1'         # broker address
    port=2000            # broker port
    clientid=0        # client id sent to brocker
    #will            # stores the will of the client
    #username        # stores username
    #password        # stores password
    retain = 0
    qosLevel = 0
    requestCode = 0
    messageType = 5
    serializeType = 3
    #methodId = ""
    #serviceId = ""
    ShortMIN_VALUE = -32768
    ShortMAX_VALUE = 32767
    def __init__(self,ip,port):
        self.broker(ip,port,0)

    def broker(self,ip,port,id):
        self.ip=ip
        self.port=port

    def call(self,param):
        if type(param)!=dict:
            raise NameError("param must be dict")
        traceid='568e1e7052f851273652154480339845'
        issample='false'

    def writeFInt(self,tbuf,anInt,i):
        # -128 = short byte, -127 == 4 byte
        if  anInt > -127 and anInt <= 127:
            buf=chr(anInt)
            i+=1
        elif anInt >= self.ShortMIN_VALUE and anInt <= self.ShortMAX_VALUE:
            i += 3
            buf = chr(-128)+ chr( anInt >> 0) + chr( anInt >> 8)
        else:
            i += 5
            buf = chr(-127)+ chr((anInt >> 0) & 255)+ chr((anInt >> 8) & 255)+ chr((anInt >> 16) & 255)+chr((anInt >> 24) & 255)
        tbuf += buf
        return tbuf,i

    def __getattr__(self, key):
        return lambda:'bar'


def printStrInNum(sstr):
    buf=''
    for i in range(len(sstr)):
        buf = ''.join((buf,str(ord(sstr[i])),',') )
    print buf

if __name__ == '__main__':
    s = hproxy('127.0.0.1',3000)
    res = s.call({"data" :{ "uid" : "", "stype": 0}, "method" : "", "service":""})
    i=0
    totalbuf=''
    totalbuf,i = s.writeFInt(totalbuf,3,i)
    totalbuf,i = s.writeFInt(totalbuf,4,i)
    totalbuf,i = s.writeFInt(totalbuf,5,i)
    printStrInNum(totalbuf)
    # buf.__dict__
    # print 'st'.join((buf,'ed'))


