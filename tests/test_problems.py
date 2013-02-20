from nose.tools import *
from problems import *

TIMELIMIT = 60 # seconds allowed before test fails

@timed(TIMELIMIT)
def test_problem1():
	eq_(problem1(), 233168)

@timed(TIMELIMIT)
def test_problem2():
	eq_(problem2(), 4613732)

@timed(TIMELIMIT)
def test_problem3():
	eq_(problem3(), 6857)

@timed(TIMELIMIT)
def test_problem4():
	eq_(problem4(), 906609)

@timed(TIMELIMIT)
def test_problem5():
	eq_(problem5(), 232792560)

@timed(TIMELIMIT)
def test_problem6():
	eq_(problem6(), 25164150)

@timed(TIMELIMIT)
def test_problem7():
	eq_(problem7(), 104743)

@timed(TIMELIMIT)
def test_problem8():
		eq_(problem8(), 40824)

@timed(TIMELIMIT)
def test_problem9():
	eq_(problem9(), 31875000)

@timed(TIMELIMIT)
def test_problem10():
	eq_(problem10(), 142913828922)

@timed(TIMELIMIT)
def test_problem12():
	eq_(problem12(), 76576500)

@timed(TIMELIMIT)
def test_problem13():
	eq_(problem13(), 5537376230)

@timed(TIMELIMIT)
def test_problem16():
	eq_(problem16(), 1366)

@timed(TIMELIMIT)
def test_problem17():
	eq_(problem17(), 21124)

@timed(TIMELIMIT)
def test_problem20():
	eq_(problem20(), 648)

@timed(TIMELIMIT)
def test_problem22():
	eq_(problem22(), 871198282)

@timed(TIMELIMIT)
def test_problem24():
	eq_(problem24(), 2783915460)

@timed(TIMELIMIT)
def test_problem25():
	eq_(problem25(), 4782)

@timed(TIMELIMIT)
def test_problem30():
	eq_(problem30(), 443839)

