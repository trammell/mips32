#!/usr/bin/python


"""

>>> inst = Instr('add $t0, $s1, $s2')

>>> inst = Instr('lw $t0, 32($s3)')


"""



if __name__ == "__main__":
    import doctest
    doctest.testmod()
