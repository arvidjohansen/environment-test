#! /Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# Code test for working with environment-
# variables with the os module on different
# systems

import os

fruit = os.getenv('fruit')
print(fruit)
sep = str('-'*5)
print(sep)
print(sep.join('\n'))



cmds = [
    'getcwd',
 'getcwdb',
 'getegid',
 'getenv',
 'getenvb',
 'geteuid',
 'getgid',
 'getgrouplist',
 'getgroups',
 'getloadavg',
 'getlogin',
 'getpgid',
 'getpgrp',
 'getpid',
 'getppid',
 'getpriority',
 'getsid',
 'getuid',
]

errors = [] # all func names that cause errors


for c in cmds:

    print('\n\n')
    print('Running command : '+c)
    print('\n\n')
    full_command = getattr(os,c)
    try:
        print(full_command())
    except TypeError:
        # func required args
        errors.append(c)

    


print('Finished')
print(f'Functions with errors: ')

print(errors)

