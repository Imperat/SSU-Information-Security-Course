import pda
import unittest
import copy
import string_perserver as s_p

from pda_exceptions import PDACrashException

input_alphabet = set("0123456789.+-e")

states = {'s1', 's15', 's2', 's3', 's4', 's5', 's6'}

rules = {
    's1': {'+': 's15',
           '-': 's15',
           '0': 's2',
           '1': 's2',
           '2': 's2',
           '3': 's2',
           '4': 's2',
           '5': 's2',
           '6': 's2',
           '7': 's2',
           '8': 's2',
           '9': 's2',
           '.': 's32'
           },
    's2': {
           '0': 's2',
           '1': 's2',
           '2': 's2',
           '3': 's2',
           '4': 's2',
           '5': 's2',
           '6': 's2',
           '7': 's2',
           '8': 's2',
           '9': 's2',
           '.': 's3',
           'e': 's4',
           },
    's15': {
           '0': 's2',
           '1': 's2',
           '2': 's2',
           '3': 's2',
           '4': 's2',
           '5': 's2',
           '6': 's2',
           '7': 's2',
           '8': 's2',
           '9': 's2',
           '.': 's31',
           },
    's31':{
           '0': 's3',
           '1': 's3',
           '2': 's3',
           '3': 's3',
           '4': 's3',
           '5': 's3',
           '6': 's3',
           '7': 's3',
           '8': 's3',
           '9': 's3',
           'e': 's4'
           },
    's3': {
           '0': 's3',
           '1': 's3',
           '2': 's3',
           '3': 's3',
           '4': 's3',
           '5': 's3',
           '6': 's3',
           '7': 's3',
           '8': 's3',
           '9': 's3',
           'e': 's4'
           },
    's32': {
           '0': 's3',
           '1': 's3',
           '2': 's3',
           '3': 's3',
           '4': 's3',
           '5': 's3',
           '6': 's3',
           '7': 's3',
           '8': 's3',
           '9': 's3',
           'e': 's4'
           },
    's4': {
           '0': 's5',
           '1': 's5',
           '2': 's5',
           '3': 's5',
           '4': 's5',
           '5': 's5',
           '6': 's5',
           '7': 's5',
           '8': 's5',
           '9': 's5',
           '+': 's6',
           '-': 's6'
           },
    's6': {
           '0': 's5',
           '1': 's5',
           '2': 's5',
           '3': 's5',
           '4': 's5',
           '5': 's5',
           '6': 's5',
           '7': 's5',
           '8': 's5',
           '9': 's5',
           },
    's5': {
           '0': 's5',
           '1': 's5',
           '2': 's5',
           '3': 's5',
           '4': 's5',
           '5': 's5',
           '6': 's5',
           '7': 's5',
           '8': 's5',
           '9': 's5',
           },
}

initial_state = 's1'
terminate_state = {'s5', 's2', 's3', 's5'}


class TestFloat(unittest.TestCase):

    def test1(self):
        strs = '-12.e-1'
        my_pda = pda.PDA(rules, input_alphabet, states,
                 initial_state, terminate_state)
        res = s_p.perserve_string(strs, copy.deepcopy(my_pda), 0)
        self.assertEqual(res, (True, len(strs)-1))

    def test2(self):
        strs = '-1'
        my_pda = pda.PDA(rules, input_alphabet, states,
                 initial_state, terminate_state)
        res = s_p.perserve_string(strs, copy.deepcopy(my_pda), 0)
        self.assertEqual(res, (True, len(strs)-1))

    def test3(self):
        strs = '0'
        my_pda = pda.PDA(rules, input_alphabet, states,
                 initial_state, terminate_state)
        res = s_p.perserve_string(strs, copy.deepcopy(my_pda), 0)
        self.assertEqual(res, (True, len(strs)-1))

    def test4(self):
        strs = '000'
        my_pda = pda.PDA(rules, input_alphabet, states,
                 initial_state, terminate_state)
        res = s_p.perserve_string(strs, copy.deepcopy(my_pda), 0)
        self.assertEqual(res, (True, len(strs)-1))

    def test5(self):
        strs = '+123'
        my_pda = pda.PDA(rules, input_alphabet, states,
                 initial_state, terminate_state)
        res = s_p.perserve_string(strs, copy.deepcopy(my_pda), 0)
        self.assertEqual(res, (True, len(strs)-1))

    def test6(self):
        strs = '1.1'
        my_pda = pda.PDA(rules, input_alphabet, states,
                 initial_state, terminate_state)
        res = s_p.perserve_string(strs, copy.deepcopy(my_pda), 0)
        self.assertEqual(res, (True, len(strs)-1))

    def test7(self):
        strs = '-2.3'
        my_pda = pda.PDA(rules, input_alphabet, states,
                 initial_state, terminate_state)
        res = s_p.perserve_string(strs, copy.deepcopy(my_pda), 0)
        self.assertEqual(res, (True, len(strs)-1))

    def test8(self):
        strs = '2e13'
        my_pda = pda.PDA(rules, input_alphabet, states,
                 initial_state, terminate_state)
        res = s_p.perserve_string(strs, copy.deepcopy(my_pda), 0)
        self.assertEqual(res, (True, len(strs)-1))

    def test9(self):
        strs = '10.1e+10'
        my_pda = pda.PDA(rules, input_alphabet, states,
                 initial_state, terminate_state)
        res = s_p.perserve_string(strs, copy.deepcopy(my_pda), 0)
        self.assertEqual(res, (True, len(strs)-1))

    def test10(self):
        strs = '10.1e-10'
        my_pda = pda.PDA(rules, input_alphabet, states,
                 initial_state, terminate_state)
        res = s_p.perserve_string(strs, copy.deepcopy(my_pda), 0)
        self.assertEqual(res, (True, len(strs)-1))

    def test11(self):
        strs = '+123.e2'
        my_pda = pda.PDA(rules, input_alphabet, states,
                 initial_state, terminate_state)
        res = s_p.perserve_string(strs, copy.deepcopy(my_pda), 0)
        self.assertEqual(res, (True, len(strs)-1))

    def test12(self):
        strs = '.1'
        my_pda = pda.PDA(rules, input_alphabet, states,
                 initial_state, terminate_state)
        res = s_p.perserve_string(strs, copy.deepcopy(my_pda), 0)
        self.assertEqual(res, (True, len(strs)-1))

    def test13(self):
        strs = '0912.'
        my_pda = pda.PDA(rules, input_alphabet, states,
                 initial_state, terminate_state)
        res = s_p.perserve_string(strs, copy.deepcopy(my_pda), 0)
        self.assertEqual(res, (True, len(strs)-1))

    def test14(self):
        strs = '.1e01'
        my_pda = pda.PDA(rules, input_alphabet, states,
                 initial_state, terminate_state)
        res = s_p.perserve_string(strs, copy.deepcopy(my_pda), 0)
        self.assertEqual(res, (True, len(strs)-1))

    def test15(self):
        strs = '+1.2e-2'
        my_pda = pda.PDA(rules, input_alphabet, states,
                 initial_state, terminate_state)
        res = s_p.perserve_string(strs, copy.deepcopy(my_pda), 0)
        self.assertEqual(res, (True, len(strs)-1))

    def test16(self):
        strs = '+.1e10'
        my_pda = pda.PDA(rules, input_alphabet, states,
                 initial_state, terminate_state)
        res = s_p.perserve_string(strs, copy.deepcopy(my_pda), 0)
        self.assertEqual(res, (True, len(strs)-1))

    def test17(self):
        strs = '-23.e2'
        my_pda = pda.PDA(rules, input_alphabet, states,
                 initial_state, terminate_state)
        res = s_p.perserve_string(strs, copy.deepcopy(my_pda), 0)
        self.assertEqual(res, (True, len(strs)-1))

    # negate tests
    
    def test18(self):
        strs = '.'
        try:
            my_pda = pda.PDA(rules, input_alphabet, states,
                       initial_state, terminate_state)
            res = s_p.perserve_string(strs, copy.deepcopy(my_pda), 0)
        except PDACrashException:
          return
        self.assertEqual(res[0], False)

    def test19(self):
        strs = 'e'
        try:
            my_pda = pda.PDA(rules, input_alphabet, states,
                       initial_state, terminate_state)
            res = s_p.perserve_string(strs, copy.deepcopy(my_pda), 0)
        except PDACrashException:
          return
        self.assertEqual(res[0], False)


    def test20(self):
        strs = '-e10'
        try:
            my_pda = pda.PDA(rules, input_alphabet, states,
                       initial_state, terminate_state)
            res = s_p.perserve_string(strs, copy.deepcopy(my_pda), 0)
        except PDACrashException:
          return
        self.assertEqual(res[0], False)


if __name__ == '__main__':
    unittest.main()