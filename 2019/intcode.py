import pytest


def int_code_v2(program):
    opcodes = {
        1: lambda x, y: x + y,
        2: lambda x, y: x * y,
    }

    idx = 0
    done = False
    while not done:
        parameters = program[idx:idx + 4]
        done = parameters[0] == 99
        if done:
            break

        opcode, input1, input2, output = parameters
        operation = opcodes.get(opcode)
        if not operation:
            raise Exception(f'Something went wrong, unknown opcode {opcode}')

        program[output] = opcodes[opcode](program[input1], program[input2])
        idx += 4

    return program


@pytest.mark.parametrize('input, output', [
    ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
    ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
    ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
    ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
    ([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]),
])
def test_int_code_machine(input, output):
    assert int_code_v2(input) == output

# ------


ADD = 1
MULTIPLY = 2
INPUT = 3
OUTPUT = 4
JUMP_TRUE = 5
JUMP_FALSE = 6
LESS_THAN = 7
EQUALS = 8
EXIT = 99
OPERATIONS = [ADD, MULTIPLY, INPUT, OUTPUT, JUMP_TRUE, JUMP_FALSE, LESS_THAN, EQUALS, EXIT]
POSITION = '0'
IMMEDIATE = '1'
d = dict(zip(OPERATIONS, ['add', 'multiply', 'input', 'output', 'jump-true', 'jump-false', 'less-than', 'equals']))


def read_arguments(memory, instruction_pointer, modes, num_params, relative_base):
    start = instruction_pointer + 1
    end = start + num_params

    arg_data = memory[start:end]

    output = param2 = None
    if len(arg_data) == 3:
        param1, param2, output = arg_data

    elif len(arg_data) == 2:
        param1, param2 = arg_data

    elif len(arg_data) == 1:
        param1 = memory[start]
        return end, [param1], None

    arg_one_mode, arg_two_mode, output_mode = modes

    arguments = [memory[param1] if arg_one_mode == POSITION else param1]
    if param2 is not None:
        arguments.append(
            memory[param2] if arg_two_mode == POSITION else param2
        )

    return end, arguments, output


def read_next_operation(memory, instruction_pointer, relative_base):
    current_instruction = memory[instruction_pointer]
    oc = str(current_instruction)
    oc = oc.zfill(5)

    op_code = int(oc[-2:])
    # reverse and zero fill the modes
    modes = oc[:-2].zfill(3)[::-1]

    if op_code not in OPERATIONS:
        raise Exception(f'Something went wrong, unknown operation {op_code} ({d[op_code]})')

    if op_code in (ADD, MULTIPLY, LESS_THAN, EQUALS):
        num_params = 3
    elif op_code in (JUMP_TRUE, JUMP_FALSE):
        num_params = 2
    elif op_code in (INPUT, OUTPUT):
        num_params = 1
    elif op_code == EXIT:
        return None, None, None, None

    # print(memory[instruction_pointer:end])
    # print(d[op_code], args)
    end, args, output = read_arguments(memory, instruction_pointer, modes, num_params, relative_base)
    return op_code, end, args, output


def int_code_v5(memory, inputs=None):
    # print(memory)
    input_ptr = 0
    outputs = []
    instruction_pointer = 0
    relative_base = 0
    done = False

    while not done:
        op_code, end, args, output = read_next_operation(memory, instruction_pointer, relative_base)

        if not op_code:
            done = True
            continue

        if op_code not in OPERATIONS:
            raise Exception(f'Something went wrong, unknown operation {op_code} ({d[op_code]})')

        if op_code in (ADD, MULTIPLY, LESS_THAN, EQUALS, INPUT, OUTPUT):
            if op_code == ADD:
                memory[output] = args[0] + args[1]
            elif op_code == MULTIPLY:
                memory[output] = args[0] * args[1]
            elif op_code == EQUALS:
                memory[output] = 1 if args[0] == args[1] else 0
            elif op_code == LESS_THAN:
                memory[output] = 1 if args[0] < args[1] else 0
            if op_code == INPUT:
                memory[args[0]] = inputs[input_ptr]
                input_ptr += 1
            elif op_code == OUTPUT:
                outputs.append(memory[args[0]])

            instruction_pointer = end

        elif op_code in (JUMP_TRUE, JUMP_FALSE):
            if op_code == JUMP_TRUE:
                instruction_pointer = args[1] if args[0] != 0 else end
            elif op_code == JUMP_FALSE:
                instruction_pointer = args[1] if args[0] == 0 else end

        if instruction_pointer >= len(memory):
            done = True

    return memory, outputs


def thermal_environment_supervision_terminal(program, inputs=[1]):
    _memory, output = int_code_v5(program, inputs)
    return output[-1]


@pytest.mark.parametrize('program, expected_output', [
    ([3, 0, 4, 0, 99], 1),
    ([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 0),
    ([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 1),
    ([3, 3, 1108, -1, 8, 3, 4, 3, 99],  0),
    ([3, 3, 1107, -1, 8, 3, 4, 3, 99],  1),
    ([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], 1),
    ([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], 1),
])
def test_test(program, expected_output):
    assert thermal_environment_supervision_terminal(program) == expected_output
