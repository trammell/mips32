usage:
	@echo "usage: make [test]"

.PHONY: test

test:
	python mips32/Instruction.py -v

