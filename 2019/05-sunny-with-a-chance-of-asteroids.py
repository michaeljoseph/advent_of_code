# ⏱ 2019-11-05 19:20
## TODO: 2.b terminology that i skipped
# hacksolution 19:23
# 19:36 actually, naming helped, now assert it's still good

ADD = 1
MULTIPLY = 2
INPUT = 3
OUTPUT = 4
EXIT = 99

OPERATIONS = [ADD, MULTIPLY, INPUT, OUTPUT, EXIT]
POSITION = '0'
IMMEDIATE = '1'

d = {
    ADD: 'add',
    MULTIPLY: 'multiply',
    INPUT: 'input',
    OUTPUT: 'output',
}


def run_program(memory, i=None):
    outputs = []
    instruction_pointer = 0
    done = False
    # print(list(enumerate(memory[:20])))
    # print(memory[:20])
    while not done:
        # print('IPPPPPP', instruction_pointer)
        current_instruction = memory[instruction_pointer]

        if current_instruction == EXIT:
            done = True
            continue

        oc = str(current_instruction)
        oc = oc.zfill(5 if len(oc) == 4 else 3)

        op_code = int(oc[-2:])
        # reverse and zero fill the modes
        modes = oc[:-2].zfill(3)[::-1]
        # modes = oc[:-2][::-1]
        # print(f'OC: {oc}; op_code: {op_code}; modes: {modes}')

        if op_code in (ADD, MULTIPLY):
            start = instruction_pointer + 1
            end = instruction_pointer + 4
            # print(f'ip:{instruction_pointer}; start={start}; end={end}')
            # print(memory[instruction_pointer], memory[start], memory[end])
            # print(memory[start:end] )
            param1, param2, output = memory[start:end]

            # print(f'modes={modes}')
            arg_one_mode, arg_two_mode, output_mode = modes
            assert output_mode == '0'

            arg_one = memory[param1] if arg_one_mode == POSITION else param1
            arg_two = memory[param2] if arg_two_mode == POSITION else param2

            if op_code == ADD:
                memory[output] = arg_one + arg_two
            elif op_code == MULTIPLY:
                memory[output] = arg_one * arg_two

            # print(d[op_code], param1, param2, output)
            # print(instruction_pointer, '=>', end)
            instruction_pointer = end

        elif op_code in (INPUT, OUTPUT):
            param1 = memory[instruction_pointer+1]
            # print(f'I/O: {param1}')

            if current_instruction == INPUT:
                memory[param1] = i()
            elif current_instruction == OUTPUT:
                outputs.append(memory[param1])

            # print(d[op_code], param1, outputs)
            instruction_pointer += 2

        else:
            raise Exception(f'Something went wrong, unknown operation {current_instruction}')

        if instruction_pointer >= len(memory):
            done = True

    return memory, outputs


def compute(program, noun, verb):
    return run_program([program[0], noun, verb] + program[3:])[0]


# [x] write TEST wrapper and handle i/o
def thermal_environment_supervision_terminal(program):
    _memory, output = run_program(program, i=lambda: 1)
    return output[-1]


def test_intcode_still_codes():
    memory = [1, 0, 0, 0, 99]
    expected_memory = [2, 0, 0, 0, 99]
    assert run_program(memory) == (expected_memory, [])
    # ✅ 19:40


# ok, now adding new instructions
def test_new_instructions():
    assert run_program([1002, 4, 3, 4, 33]) == ([1002, 4, 3, 4, 99], [])
    # ✅ 20:06
    assert run_program([1101, 100, -1, 4, 0]) == ([1101, 100, -1, 4, 99], [])
    assert run_program([3, 0, 4, 0, 99], i=lambda: 1) == ([1, 0, 4, 0, 99], [1])
    assert thermal_environment_supervision_terminal([3, 0, 4, 0, 99]) == [1]
    # [x] test program with new instructions to challenge fixed instruction size
    # 20:27
    # done @ 23:10


# 23:21 solve the puzzle
from common import get_puzzle
if __name__ == '__main__':
    diagnostic_program = [int(x) for x in get_puzzle(5).split(',')]
    print('🙆‍♂️', thermal_environment_supervision_terminal(diagnostic_program))
# 00:13 because opcode and current instruction gah

