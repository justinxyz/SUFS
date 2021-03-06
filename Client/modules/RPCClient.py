"""
RPCClient.py
"""
import xmlrpclib


class RPCClient:

    def __init__(self, url, port):
        self.port = port
        self.url = url
        self.server = xmlrpclib.ServerProxy(self.url + ':' + str(self.port))

    def hello_world(self):
        return self.server.hello_world()

    def write1(self, filename, size):
        return self.server.write1(filename, size)

    def putfile(self, filename, size):
        return # list of blocks and datanodes it belongs to

"""
Example of us
"""
#rc = RPCClient("http://localhost", 8000)
#print rc.get_hello_world()