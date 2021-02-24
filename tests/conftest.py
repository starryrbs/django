import subprocess

import sys


def pytest_cmdline_main(config):
    run_args = ['python', 'runtests.py', '--settings=test_sqlite']
    if config.args:
        item = config.args[0]
        test_label = item.replace('/', '.').replace('::', '.').replace('.py', '')
        run_args.append(test_label)
    process = subprocess.run(run_args)
    sys.exit(process.returncode)
