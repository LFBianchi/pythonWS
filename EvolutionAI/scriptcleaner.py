file = open('files/script-list.txt', 'r')
writef = open('files/clean-scripts.txt', 'w')

for line in file:
    if not line.startswith('Written'):
        if not line.startswith('\n'):
            clean_line = line[:line.find('(') - 1]
            script_endpoint = '-'.join(clean_line.split(' '))
            writef.write(script_endpoint.rstrip() +'\n')
    