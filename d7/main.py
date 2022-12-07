import copy
import re

command_ex = re.compile(r'\$\s(\w+)( (.+))?')
file_ex = re.compile(r'(\d+) (\S+)')

def get_command(input):
    if input[0] != '$':
        return None
    matches = command_ex.match(input)
    command = matches.group(1)
    if arg := matches.group(3):
        return (command, arg.strip())
    return (command, None)

def make_list(input):
    node_template = {'size': 0, 'path': [], 'is_dir': True}
    root = copy.deepcopy(node_template)
    path_list = {'/': root}
    current_node = root

    def cd_command(param):
        nonlocal current_node
        match param:
            case '/':
                current_node = path_list['/']
            case '..':
                current_node = path_list['/' + '/'.join(current_node['path'][:-1])]
            case _:
                path = current_node['path'] + [param]
                path_line = ''.join(path)
                if path_line in path_list.keys():
                    current_node = path_list[path_line]
                else:
                    new_node = copy.deepcopy(node_template)
                    new_node['path'] = current_node['path'] + [param]
                    path_list['/' + '/'.join(new_node['path'])] = new_node
                    current_node = new_node

    def ls_command(output):
        nonlocal current_node
        for line in output:
            node = copy.deepcopy(node_template)
            if line[:3] == 'dir':
                fn = line[4:].strip()
            else:
                matches = file_ex.match(line)
                node['size'] = int(matches.group(1))
                node['is_dir'] = False
                fn = matches.group(2)

            node['path'] = current_node['path'] + [fn]
            path_line = '/' + '/'.join(node['path'])
            if not path_list.get(path_line, None):
                path_list[path_line] = node

    def do_command(command, param, output):
        match command:
            case 'cd':
                cd_command(param)
            case 'ls':
                ls_command(output)

    def calc_sizes():
        for file, meta in path_list.items():
            if not meta['is_dir']:
                tmp_path = ''
                path_list['/']['size'] += meta['size']
                for el in meta['path'][:-1]:
                    tmp_path += '/' + el
                    path_list[tmp_path]['size'] += meta['size']

    last_command = None
    output_buffer = []
    for line in input:
        if command := get_command(line):
            if last_command != None:
                do_command(*last_command, output_buffer)
            output_buffer = []
            last_command = command
        else:
            output_buffer.append(line)
    do_command(*last_command, output_buffer)

    calc_sizes()

    return path_list

def find_total_size_limit(path_list, limit=100000):
    total_size = 0
    for dir, meta in path_list.items():
        if meta['is_dir'] and meta['size'] <= limit:
            total_size += meta['size']
    return total_size

def find_closest(path_list, to_clean):
    closest = None
    for dir, meta in path_list.items():
        if meta['is_dir'] and meta['size'] >= to_clean:
            if not closest or (closest and meta['size'] < closest):
                closest = meta['size']
    return closest

with open('input') as input:
    path_list = make_list(input)

# Part 1
print(find_total_size_limit(path_list))

# Part 2
need_to_update = 30000000
total_memory = 70000000
to_clean = need_to_update - (total_memory - path_list['/']['size'])

print(find_closest(path_list, to_clean))
