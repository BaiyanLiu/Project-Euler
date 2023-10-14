from subprocess import getoutput


def test_0001():
    assert_problem(1, '23', 3, 5, 10)
    assert_problem(1, '233168', 3, 5, 1000)


def test_0002():
    assert_problem(2, '44', 100)
    assert_problem(2, '4613732', 4000000)


def test_0003():
    assert_problem(3, '29', 13195)
    assert_problem(3, '6857', 600851475143)


def test_0004():
    assert_problem(4, '9009', 2)
    assert_problem(4, '906609', 3)


def test_0005():
    assert_problem(5, '2520', 10)
    assert_problem(5, '232792560', 20)


def test_0006():
    assert_problem(6, '2640', 10)
    assert_problem(6, '25164150', 100)


def test_0007():
    assert_problem(7, '13', 6)
    assert_problem(7, '104743', 10001)


def test_0008():
    assert_problem(8, '5832', 4)
    assert_problem(8, '23514624000', 13)


def test_0009():
    assert_problem(9, '60', 12)
    assert_problem(9, '31875000', 1000)


def test_0010():
    assert_problem(10, '17', 10)
    assert_problem(10, '142913828922', 2000000)


def test_0011():
    assert_problem(11, '70600674')


def test_0012():
    assert_problem(12, '28', 5)
    assert_problem(12, '76576500', 500)


def test_0013():
    assert_problem(13, '5537376230')


def test_0014():
    assert_problem(14, '837799', 1000000)


def test_0015():
    assert_problem(15, '6', 2)
    assert_problem(15, '137846528820', 20)


def test_0016():
    assert_problem(16, '26', 32768)
    assert_problem(16, '1366', 2 ** 1000)


def test_0017():
    assert_problem(17, '19', 5)
    assert_problem(17, '21124', 1000)


def test_0018():
    assert_problem(18, '1074')


def test_0019():
    assert_problem(19, '171', 2000)


def test_0020():
    assert_problem(20, '27', 10)
    assert_problem(20, '648', 100)


def test_0021():
    assert_problem(21, '31626', 10000)


def test_0022():
    assert_problem(22, '871198282')


def test_0023():
    assert_problem(23, '4179871')


def test_0024():
    assert_problem(24, '012', 1, 2)
    assert_problem(24, '210', 6, 2)
    assert_problem(24, '2783915460', 1000000, 9)


def test_0025():
    assert_problem(25, '12', 3)
    assert_problem(25, '4782', 1000)


def test_0026():
    assert_problem(26, '7', 11)
    assert_problem(26, '983', 1000)


def test_0027():
    assert_problem(27, '-59231')


def test_0028():
    assert_problem(28, '101', 5)
    assert_problem(28, '669171001', 1001)


def test_0029():
    assert_problem(29, '15', 5)
    assert_problem(29, '9183', 100)


def test_0030():
    assert_problem(30, '19316', 4)
    assert_problem(30, '443839', 5)


def test_0031():
    assert_problem(31, '73682', 2)


def test_0032():
    assert_problem(32, '45228')


def test_0033():
    assert_problem(33, '100')


def test_0034():
    assert_problem(34, '40730')


def test_0035():
    assert_problem(35, '13', 100)
    assert_problem(35, '55', 1000000)


def test_0036():
    assert_problem(36, '872187')


def test_0037():
    assert_problem(37, '748317')


def test_0038():
    assert_problem(38, '932718654')


def test_0039():
    assert_problem(39, '840')


def test_0040():
    assert_problem(40, '210')


def test_0041():
    assert_problem(41, '7652413')


def test_0042():
    assert_problem(42, '162')


def test_0043():
    assert_problem(43, '16695334890')


def test_0044():
    assert_problem(44, '5482660')


def test_0045():
    assert_problem(45, '1533776805')


def test_0046():
    assert_problem(46, '5777')


def test_0047():
    assert_problem(47, '134043')


def test_0048():
    assert_problem(48, '0405071317', 10)
    assert_problem(48, '9110846700', 1000)


def test_0049():
    assert_problem(49, '296962999629')


def test_0050():
    assert_problem(50, '41', 100)
    assert_problem(50, '953', 1000)
    assert_problem(50, '997651', 1000000)


def test_0051():
    assert_problem(51, '13', 6)
    assert_problem(51, '56003', 7)
    assert_problem(51, '121313', 8)


def test_0052():
    assert_problem(52, '142857')


def test_0053():
    assert_problem(53, '4075')


def test_0054():
    assert_problem(54, '376')


def test_0055():
    assert_problem(55, '249')


def test_0056():
    assert_problem(56, '972')


def test_0057():
    assert_problem(57, '153')


def test_0058():
    assert_problem(58, '26241')


def test_0059():
    assert_problem(59, '129448')


def test_0060():
    assert_problem(60, '792', 4)
    assert_problem(60, '26033', 5)


def test_0061():
    assert_problem(61, '28684')


def test_0062():
    assert_problem(62, '41063625', 3)
    assert_problem(62, '127035954683', 5)


def test_0063():
    assert_problem(63, '49')


def test_0064():
    assert_problem(64, '4', 13)
    assert_problem(64, '1322', 10000)


def test_0065():
    assert_problem(65, '17', 10)
    assert_problem(65, '272', 100)


def test_0066():
    assert_problem(66, '5', 7)
    assert_problem(66, '661', 1000)


def test_0067():
    assert_problem(67, '7273')


def test_0068():
    assert_problem(68, '432621513', 9, 3)
    assert_problem(68, '6531031914842725', 16, 5)


def test_0069():
    assert_problem(69, '6', 10)
    assert_problem(69, '510510', 1000000)


def test_0070():
    assert_problem(70, '8319823')


def test_0071():
    assert_problem(71, '2', 8)
    assert_problem(71, '428570', 1000000)


def test_0072():
    assert_problem(72, '21', 8)
    assert_problem(72, '303963552391', 1000000)


def test_0073():
    assert_problem(73, '3', 8)
    assert_problem(73, '7295372', 12000)


def test_0074():
    assert_problem(74, '402')


def test_0075():
    assert_problem(75, '6', 48)
    assert_problem(75, '161667', 1500000)


def test_0076():
    assert_problem(76, '6', 5)
    assert_problem(76, '190569291', 100)


def test_0077():
    assert_problem(77, '71')


def test_0078():
    assert_problem(78, '55374')


def test_0079():
    assert_problem(79, '73162890')


def test_0080():
    assert_problem(80, '40886')


def test_0081():
    assert_problem(81, '427337')


def test_0082():
    assert_problem(82, '260324')


def test_0083():
    assert_problem(83, '425185')


def test_0084():
    assert_problem(84, '102400', 6)
    assert_problem(84, '101524', 4)


def test_0085():
    assert_problem(85, '2772')


def test_0086():
    assert_problem(86, '100', 2000)
    assert_problem(86, '1818', 1000000)


def test_0087():
    assert_problem(87, '4', 50)
    assert_problem(87, '1097343', 50000000)


def test_0088():
    assert_problem(88, '30', 6)
    assert_problem(88, '61', 12)
    assert_problem(88, '7587457', 12000)


def test_0089():
    assert_problem(89, '743')


def test_0090():
    assert_problem(90, '1217')


def assert_problem(problem: int, expected: str, *args):
    args_str = ' '.join(str(arg) for arg in args)
    assert getoutput(f'python problem_{problem:04}.py {args_str}') == expected
