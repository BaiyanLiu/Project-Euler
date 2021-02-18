from subprocess import getoutput


def test_0001():
    problem = 'problem_0001.py'
    assert getoutput(f'{problem} 3 5 10') == '23'
    assert getoutput(f'{problem} 3 5 1000') == '233168'


def test_0002():
    problem = 'problem_0002.py'
    assert getoutput(f'{problem} 100') == '44'
    assert getoutput(f'{problem} 4000000') == '4613732'


def test_0003():
    problem = 'problem_0003.py'
    assert getoutput(f'{problem} 13195') == '29'
    assert getoutput(f'{problem} 600851475143') == '6857'


def test_0004():
    problem = 'problem_0004.py'
    assert getoutput(f'{problem} 2') == '9009'
    assert getoutput(f'{problem} 3') == '906609'


def test_0005():
    problem = 'problem_0005.py'
    assert getoutput(f'{problem} 10') == '2520'
    assert getoutput(f'{problem} 20') == '232792560'


def test_0006():
    problem = 'problem_0006.py'
    assert getoutput(f'{problem} 10') == '2640'
    assert getoutput(f'{problem} 100') == '25164150'


def test_0007():
    problem = 'problem_0007.py'
    assert getoutput(f'{problem} 6') == '13'
    assert getoutput(f'{problem} 10001') == '104743'


def test_0008():
    problem = 'problem_0008.py'
    assert getoutput(f'{problem} 4') == '5832'
    assert getoutput(f'{problem} 13') == '23514624000'


def test_0009():
    problem = 'problem_0009.py'
    assert getoutput(f'{problem} 12') == '60'
    assert getoutput(f'{problem} 1000') == '31875000'


def test_0010():
    problem = 'problem_0010.py'
    assert getoutput(f'{problem} 10') == '17'
    assert getoutput(f'{problem} 2000000') == '142913828922'


def test_0011():
    problem = 'problem_0011.py'
    assert getoutput(f'{problem}') == '70600674'


def test_0012():
    problem = 'problem_0012.py'
    assert getoutput(f'{problem} 5') == '28'
    assert getoutput(f'{problem} 500') == '76576500'


def test_0013():
    problem = 'problem_0013.py'
    assert getoutput(f'{problem}') == '5537376230'


def test_0014():
    problem = 'problem_0014.py'
    assert getoutput(f'{problem} 1000000') == '837799'


def test_0015():
    problem = 'problem_0015.py'
    assert getoutput(f'{problem} 2') == '6'
    assert getoutput(f'{problem} 20') == '137846528820'


def test_0016():
    problem = 'problem_0016.py'
    assert getoutput(f'{problem} 32768') == '26'
    assert getoutput(f'{problem} {2 ** 1000}') == '1366'


def test_0017():
    problem = 'problem_0017.py'
    assert getoutput(f'{problem} 5') == '19'
    assert getoutput(f'{problem} 1000') == '21124'


def test_0018():
    problem = 'problem_0018.py'
    assert getoutput(f'{problem}') == '1074'


def test_0019():
    problem = 'problem_0019.py'
    assert getoutput(f'{problem} 2000') == '171'


def test_0020():
    problem = 'problem_0020.py'
    assert getoutput(f'{problem} 10') == '27'
    assert getoutput(f'{problem} 100') == '648'


def test_0021():
    problem = 'problem_0021.py'
    assert getoutput(f'{problem} 10000') == '31626'


def test_0022():
    problem = 'problem_0022.py'
    assert getoutput(f'{problem}') == '871198282'


def test_0023():
    problem = 'problem_0023.py'
    assert getoutput(f'{problem}') == '4179871'


def test_0024():
    problem = 'problem_0024.py'
    assert getoutput(f'{problem} 1 2') == '012'
    assert getoutput(f'{problem} 6 2') == '210'
    assert getoutput(f'{problem} 1000000 9') == '2783915460'


def test_0025():
    problem = 'problem_0025.py'
    assert getoutput(f'{problem} 3') == '12'
    assert getoutput(f'{problem} 1000') == '4782'


def test_0026():
    problem = 'problem_0026.py'
    assert getoutput(f'{problem} 11') == '7'
    assert getoutput(f'{problem} 1000') == '983'


def test_0027():
    problem = 'problem_0027.py'
    assert getoutput(f'{problem}') == '-59231'


def test_0028():
    problem = 'problem_0028.py'
    assert getoutput(f'{problem} 5') == '101'
    assert getoutput(f'{problem} 1001') == '669171001'


def test_0029():
    problem = 'problem_0029.py'
    assert getoutput(f'{problem} 5') == '15'
    assert getoutput(f'{problem} 100') == '9183'


def test_0030():
    problem = 'problem_0030.py'
    assert getoutput(f'{problem} 4') == '19316'
    assert getoutput(f'{problem} 5') == '443839'


def test_0031():
    problem = 'problem_0031.py'
    assert getoutput(f'{problem} 2') == '73682'


def test_0032():
    problem = 'problem_0032.py'
    assert getoutput(f'{problem}') == '45228'


def test_0033():
    problem = 'problem_0033.py'
    assert getoutput(f'{problem}') == '100'


def test_0034():
    problem = 'problem_0034.py'
    assert getoutput(f'{problem}') == '40730'


def test_0035():
    problem = 'problem_0035.py'
    assert getoutput(f'{problem} 100') == '13'
    assert getoutput(f'{problem} 1000000') == '55'


def test_0036():
    problem = 'problem_0036.py'
    assert getoutput(f'{problem}') == '872187'


def test_0037():
    problem = 'problem_0037.py'
    assert getoutput(f'{problem}') == '748317'


def test_0038():
    problem = 'problem_0038.py'
    assert getoutput(f'{problem}') == '932718654'


def test_0039():
    problem = 'problem_0039.py'
    assert getoutput(f'{problem}') == '840'


def test_0040():
    problem = 'problem_0040.py'
    assert getoutput(f'{problem}') == '210'


def test_0041():
    problem = 'problem_0041.py'
    assert getoutput(f'{problem}') == '7652413'


def test_0042():
    problem = 'problem_0042.py'
    assert getoutput(f'{problem}') == '162'


def test_0043():
    problem = 'problem_0043.py'
    assert getoutput(f'{problem}') == '16695334890'


def test_0044():
    problem = 'problem_0044.py'
    assert getoutput(f'{problem}') == '5482660'
