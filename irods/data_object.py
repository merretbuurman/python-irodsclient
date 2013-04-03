from models import DataObject
SEEK_SET = 0
SEEK_CUR = 1
SEEK_END = 2

class iRODSDataObject(object):
    def __init__(self, sess, parent=None, result=None):
        self.sess = sess
        if parent:
            self.collection = parent
        if result:
            self.id = result[DataObject.id]
            self.name = result[DataObject.name]
            self.full_path = self.collection.name + '/' + self.name

    def __repr__(self):
        return "<iRODSDataObject %d %s>" % (self.id, self.name)

    def open(self, mode):
        desc = self.sess.open_file(self.full_path, mode)
        return iRODSDataObjectFile(self.sess, desc)

class iRODSDataObjectFile(object):
    def __init__(self, session, descriptor):
        self.sess = session
        self.desc = descriptor
        self.position = None

    def tell(self):
        return self.position

    def close(self):
        pass

    def read(self, size=None):
        return self.sess.read_file(self.desc, 1024)

    def write(self, string):
        pass

    def seek(self, offset, whence):
        pass

    def readline(self):
        pass

    def readlines(self):
        pass
