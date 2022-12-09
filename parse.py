import re

def gen_tree(file):
    f = open(file, 'r')
    tree = {}
    lines = f.readlines()
    lines.append("")
    now = -1
    while now < len(lines) - 1:
        now += 1
        line = lines[now]
        if line.startswith('struct'):
            name = line.split(' ')[1]
            parts = name.split('::')
            state = parts[-1]
            if parts[0] == 'tokio':
                continue
            if re.match('Suspend[0-9]*', state):
                awaitee = None
                while 1:
                    now += 1
                    line = lines[now]
                    if line.startswith('struct'):
                        now -= 1
                        break
                    parts = line.split()
                    if len(parts) > 3 and parts[1] == '__awaitee:':
                        awaitee = ' '.join(parts[3:])
                    if awaitee:
                        # remove '::Suspendx' from name
                        root_name = '::'.join(name.split('::')[:-1])
                        # remove Genfuture for child futures
                        if awaitee.startswith('core::future::from_generator::GenFuture<'):
                            awaitee = awaitee.split('<')[1].split('>')[0]
                        if tree.get(root_name) == None:
                            tree[root_name] = []
                        if tree[root_name].count(awaitee) == 0:
                            tree[root_name].append(awaitee)
    return tree