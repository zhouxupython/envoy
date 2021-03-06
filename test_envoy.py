import unittest
import envoy
import time


# class SimpleTest(unittest.TestCase):

    # def test_input(self):
        # r = envoy.run("sed s/i/I/g", "Hi")
        # self.assertEqual(r.std_out.rstrip(), "HI")
        # self.assertEqual(r.status_code, 0)

    # def test_pipe(self):
        # r = envoy.run("echo -n 'hi'| tr [:lower:] [:upper:]")
        # self.assertEqual(r.std_out, "HI")
        # self.assertEqual(r.status_code, 0)

    # def test_timeout(self):
        # r = envoy.run('yes | head', timeout=1)
        # self.assertEqual(r.std_out, 'y\ny\ny\ny\ny\ny\ny\ny\ny\ny\n')
        # self.assertEqual(r.status_code, 0)

    # # THIS TEST FAILS BECAUSE expand_args DOESN'T HANDLE QUOTES PROPERLY
    # def test_quoted_args(self):
        # sentinel = 'quoted_args' * 3
        # r = envoy.run("python -c 'print \"%s\"'" % sentinel)
        # self.assertEqual(r.std_out.rstrip(), sentinel)
        # self.assertEqual(r.status_code, 0)

    # def test_non_existing_command(self):
        # r = envoy.run("blah")
        # self.assertEqual(r.status_code, 127)


class ConnectedCommandTests(unittest.TestCase):

    # def test_status_code_none(self):
        # c = envoy.connect("sleep 5")
        # #print 'c over, c.status_code: ', c.status_code
        # self.assertEqual(c.status_code, None)

    # def test_status_code_success(self):
        # c = envoy.connect("sleep 1")
        # time.sleep(2)
        # c.block()
        # self.assertEqual(c.status_code, 0)



    # def test_input(self):
        # test_string = 'asdfQWER'
        # r = envoy.connect("cat | tr [:lower:] [:upper:]")
        # r.send(test_string)
        # print 'r.std_out.rstrip()', r.std_out.rstrip()
        # self.assertEqual(r.std_out.rstrip(), test_string.upper())
        # self.assertEqual(r.status_code, 0)
		
    def test_status_code_failure(self):
        c = envoy.connect("blah")
        c.block()
        self.assertEqual(c.status_code, 127)

if __name__ == "__main__":
    unittest.main()
