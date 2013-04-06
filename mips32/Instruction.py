#!/usr/bin/python



# >>> # inst = Instruction('lw $t0, 32($s3)')

class Instruction():

    """
    >>> inst = Instruction('add $t0, $s1, $s2')
    >>> inst.asm
    'add $t0, $s1, $s2'
    """

    def __init__(self, asm):
        self.asm = asm


def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
