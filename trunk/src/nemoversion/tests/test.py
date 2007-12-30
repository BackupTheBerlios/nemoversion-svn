import unittest
import commands
from nemoversion.tests import mock
from nemoversion.repository import svncommand

class TestAddCommand(unittest.TestCase):
    def setUp(self):
        commands.getoutput("svnadmin create /tmp/nemoversion_test")
        commands.getoutput("svn co file:///tmp/nemoversion_test /tmp/testing_nemoversion/")
        commands.getoutput("touch /tmp/testing_nemoversion/foo.py")
    
    def testAddCommand(self):
        status = 0
        output = 'A         /tmp/testing_nemoversion/foo.py'
        command = svncommand.AddCommand()
        self.assertEqual({'status':status, 'output':output},
            command.execute(mock.FileInfo('/tmp/testing_nemoversion/foo.py')))

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
    
    def testAddCommand(self):
        status = 0
        output = 'D         /tmp/testing_nemoversion/foo.py'
        command = svncommand.RemoveCommand()
        self.assertEqual({'status':status, 'output':output},
            command.execute(mock.FileInfo('/tmp/testing_nemoversion/foo.py')))

    def tearDown(self):
        commands.getoutput("rm -Rf /tmp/nemoversion_test")
        commands.getoutput("rm -Rf /tmp/testing_nemoversion")
        
class TestStatusCommand(unittest.TestCase):
    def setUp(self):
        commands.getoutput("svnadmin create /tmp/nemoversion_test")
        commands.getoutput("svn co file:///tmp/nemoversion_test /tmp/testing_nemoversion/")
        commands.getoutput("touch /tmp/testing_nemoversion/foo.py")
    
    def testAddCommand(self):
        status = 0
        output = '?      /tmp/testing_nemoversion/foo.py'
        command = svncommand.StatusCommand()
        self.assertEqual({'status':status, 'output':output},
            command.execute(mock.FileInfo('/tmp/testing_nemoversion/foo.py')))

    def tearDown(self):
        commands.getoutput("rm -Rf /tmp/nemoversion_test")
        commands.getoutput("rm -Rf /tmp/testing_nemoversion")

if __name__ == '__main__':
    unittest.main()