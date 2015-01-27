#!/usr/bin/env python
# (c) 2012-2013 Continuum Analytics, Inc. / http://continuum.io
# All Rights Reserved
#
# conda is distributed under the terms of the BSD 3-clause license.
# Consult LICENSE.txt or http://opensource.org/licenses/BSD-3-Clause.

from subprocess import check_output, PIPE, Popen, STDOUT
from os.path import join, dirname, abspath, isdir
from os import makedirs, pathsep
from collections import OrderedDict

from concurrent.futures import ThreadPoolExecutor

import sys
import json
import re

manpath = join(dirname(__file__), 'build', 'man')
if not isdir(manpath):
    makedirs(manpath)
rstpath = join(dirname(__file__), 'source', 'commands')
if not isdir(rstpath):
    makedirs(rstpath)

RST_HEADER = """
.. _{command}_ref:

conda {command}
=======================

.. raw:: html

"""

def str_check_output(*args, **kwargs):
    return check_output(*args, **kwargs).decode('utf-8')

def conda_help(cache=[]):
    if cache:
        return cache[0]
    cache.append(str_check_output(['conda', '--help']))
    return cache[0]

def conda_command_help(command):
    return str_check_output(['conda'] + command.split() + ['--help'])

def conda_commands():
    print("Getting list of core commands")
    help = conda_help()
    commands = []
    start = False
    for line in help.splitlines():
        # Commands start after "command" header
        if line.strip() == 'command':
            start = True
            continue
        if start:
            # The end of the commands
            if not line:
                break
            if line[4] != ' ':
                commands.append(line.split()[0])
    return commands

def external_commands():
    print("Getting list of external commands")
    help = conda_help()
    commands = []
    start = False
    for line in help.splitlines():
        # Commands start after "command" header
        if line.strip() == 'external commands:':
            start = True
            continue
        if start:
            # The end of the commands
            if not line:
                break
            if line[4] != ' ':
                commands.append(line.split()[0])

    # TODO: Parallelize this
    print("Getting list of external subcommands")
    subcommands_re = re.compile(r'\s*\{(.*)\}\s*')
    # Check for subcommands (like conda skeleton pypi)
    command_help = {}

    def get_help(command):
        command_help[command] = conda_command_help(command)
        print("Checked for subcommand help for %s" % command)

    with ThreadPoolExecutor(len(commands)) as executor:
        # list() is needed for force exceptions to be raised
        list(executor.map(get_help, commands))

    for command in command_help:
        help = command_help[command]
        start = False
        for line in help.splitlines():
            if line.strip() == "positional arguments:":
                start = True
                continue
            if start:
                m = subcommands_re.match(line)
                if m:
                    commands.extend(['%s %s' % (command, i) for i in
                        m.group(1).split(',')])
                break
    return commands

def man_replacements():
    # XXX: We should use conda-api for this, but it's currently annoying to set the
    # root prefix with.
    info = json.loads(str_check_output(['conda', 'info', '--json']))
    # We need to use an ordered dict because the root prefix should be
    # replaced last, since it is typically a substring of the default prefix
    r = OrderedDict([
        (info['default_prefix'].encode('utf-8'), b'default prefix'),
        (pathsep.join(info['envs_dirs']).encode('utf-8'), b'envs dirs'),
        # For whatever reason help2man won't italicize these on its own
        # Note these require conda > 3.7.1
        (info['user_rc_path'].encode('utf-8'), rb'\fI\,user .condarc path\/\fP'),
        (info['sys_rc_path'].encode('utf-8'), rb'\fI\,system .condarc path\/\fP'),

        (info['root_prefix'].encode('utf-8'), rb'root prefix'),
        ])

    return r

def generate_man(command):
    conda_version = check_output(['conda', '--version'], stderr=STDOUT)

    manpage = check_output([
        'help2man',
        '--name', 'conda %s' % command,
        '--section', '1',
        '--source', 'Continuum Analytics',
        '--version-string', conda_version,
        '--no-info',
        'conda %s' % command,
        ])

    replacements = man_replacements()
    for text in replacements:
        manpage = manpage.replace(text, replacements[text])
    with open(join(manpath, 'conda-%s.1' % command.replace(' ', '-')), 'wb') as f:
        f.write(manpage)

    print("Generated manpage for conda %s" % command)

def generate_html(command):
    command_file = command.replace(' ', '-')

    # Use abspath so that it always has a path separator
    man = Popen(['man', abspath(join(manpath, 'conda-%s.1' % command_file))], stdout=PIPE)
    htmlpage = check_output([
        'man2html',
        '-bare', # Don't use HTML, HEAD, or BODY tags
        'title', 'conda-%s' % command_file,
        '-topm', '0', # No top margin
        '-botm', '0', # No bottom margin
        ],
        stdin=man.stdout)

    with open(join(manpath, 'conda-%s.html' % command_file), 'wb') as f:
        f.write(htmlpage)
    print("Generated html for conda %s" % command)


def write_rst(command, sep=None):
    command_file = command.replace(' ', '-')
    with open(join(manpath, 'conda-%s.html' % command_file), 'r') as f:
        html = f.read()

    rp = rstpath
    if sep:
        rp = join(rp, sep)
    if not isdir(rp):
        makedirs(rp)
    with open(join(rp, 'conda-%s.rst' % command_file), 'w') as f:
        f.write(RST_HEADER.format(command=command))
        for line in html.splitlines():
            f.write('   ')
            f.write(line)
            f.write('\n')
    print("Generated rst for conda %s" % command)

def main():
    core_commands = conda_commands()
    build_commands = external_commands()

    commands = sys.argv[1:] or core_commands + build_commands

    def gen_command(command):
        generate_man(command)
        generate_html(command)

    with ThreadPoolExecutor(len(commands)) as executor:
        # list() is needed to force exceptions to be raised
        list(executor.map(gen_command, commands))

    for command in [c for c in core_commands if c in commands]:
        write_rst(command)
    for command in [c for c in build_commands if c in commands]:
        write_rst(command, sep='build')

if __name__ == '__main__':
    sys.exit(main())
