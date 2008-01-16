import unittest
import commands
from nemoversion.appcontroller import factory
from nemoversion.tests import mock
from nemoversion.repository import svncommand

class TestCommand(unittest.TestCase):
    def setUp(self):
        pass
    
    def testCmpSame(self):
        fileInfo = mock.FileInfo("/tmp/testing_nemoversion/foo.py")
        otherCommand = mock.Command(fileInfo)
        theCommand = svncommand.Command(fileInfo)
        self.assertEqual(theCommand, otherCommand)
        
    def testCmpDiff(self):
        fileInfo = mock.FileInfo("/tmp/testing_nemoversion/foo.py")
        otherCommand = mock.Command(fileInfo)
        theCommand = svncommand.AddCommand(fileInfo)
        self.assertNotEqual(theCommand, otherCommand)
        
class TestAddCommand(unittest.TestCase):
    def setUp(self):
        commands.getoutput("svnadmin create /tmp/nemoversion_test")
        commands.getoutput("svn co file:///tmp/nemoversion_test /tmp/testing_nemoversion/")
        commands.getoutput("touch /tmp/testing_nemoversion/foo.py")
    
    def testAddCommand(self):
        status = 0
        output = 'A         /tmp/testing_nemoversion/foo.py'
        command = svncommand.AddCommand(mock.FileInfo('/tmp/testing_nemoversion/foo.py'))
        self.assertEqual({'status':status, 'output':output},
            command.execute())

    def tearDown(self):
        commands.getoutput("rm -Rf /tmp/nemoversion_test")
        commands.getoutput("rm -Rf /tmp/testing_nemoversion")

class TestRemoveCommand(unittest.TestCase):
    def setUp(self):
        commands.getoutput("svnadmin create /tmp/nemoversion_test")
        commands.getoutput("svn co file:///tmp/nemoversion_test /tmp/testing_nemoversion/")
        commands.getoutput("touch /tmp/testing_nemoversion/foo.py")
        commands.getoutput("svn add /tmp/testing_nemoversion/foo.py")
        commands.getoutput("svn ci /tmp/testing_nemoversion/ -m 'Testing remove command'")
    
    def testRemoveCommand(self):
        status = 0
        output = 'D         /tmp/testing_nemoversion/foo.py'
        command = svncommand.RemoveCommand(mock.FileInfo('/tmp/testing_nemoversion/foo.py'))
        self.assertEqual({'status':status, 'output':output},
            command.execute())

    def tearDown(self):
        commands.getoutput("rm -Rf /tmp/nemoversion_test")
        commands.getoutput("rm -Rf /tmp/testing_nemoversion")
        
class TestStatusCommand(unittest.TestCase):
    def setUp(self):
        commands.getoutput("svnadmin create /tmp/nemoversion_test")
        commands.getoutput("svn co file:///tmp/nemoversion_test /tmp/testing_nemoversion/")
        commands.getoutput("touch /tmp/testing_nemoversion/foo.py")
    
    def testStatusCommand(self):
        status = 0
        output = '?      /tmp/testing_nemoversion/foo.py'
        fInfo = mock.FileInfo('/tmp/testing_nemoversion/foo.py')
        command = svncommand.StatusCommand(fInfo)
        self.assertEqual({'status':status, 'output':output},
            command.execute())

    def tearDown(self):
        commands.getoutput("rm -Rf /tmp/nemoversion_test")
        commands.getoutput("rm -Rf /tmp/testing_nemoversion")

class TestActionFactory(unittest.TestCase):
    def setUp(self):
        self.finfo = mock.FileInfo('/tmp/testing_nemoversion/foo.py')
        
    def testReturnStatusCommand(self):
        actionFac = factory.ActionFactory()
        self.assertEqual(actionFac.createAction(self.finfo, "StatusCommand"),
            svncommand.StatusCommand(self.finfo))
        
if __name__ == '__main__':
    unittest.main()