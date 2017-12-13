registers = {}
high_val = 0


def get_reg(reg):
    if reg in registers:
        return registers[reg]
    else:
        return 0


def change_reg(reg, change):
    global high_val
    cur_val = get_reg(reg)
    new_val = cur_val + int(change)
    registers[reg] = new_val
    if new_val > high_val:
        high_val = new_val


def parse_reg_change(change_inst):
    if 'inc' in change_inst:
        reg, change = change_inst.split(' inc ')
    elif 'dec' in change_inst:
        reg, change = change_inst.split(' dec ')
        change = 0 - int(change)
    else:
        raise ValueError('Invalid change instruction: {}'.format(change_inst))
    change_reg(reg, change)


def parse_conditional(cond_inst):
    reg, op, val = cond_inst.split(' ')
    reg_val = get_reg(reg)
    if op in ['>', '<', '>=', '<=', '==', '!=']:
        return eval('{0} {1} {2}'.format(reg_val, op, val))
    else:
        raise ValueError('Invalid conditional instruction: {}'.format(cond_inst))


def execute_instructions(instructions):
    for inst in instructions:
        change, cond = inst.split(' if ')
        if (parse_conditional(cond)):
            parse_reg_change(change)


with open("8.txt") as f:
    instructions = [l.strip() for l in f.readlines()]
    execute_instructions(instructions)
reg_vals = set()
for r in registers:
    reg_vals.add(registers[r])
print(max(reg_vals))
print(high_val)