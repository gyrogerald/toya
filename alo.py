import sys, os

procs = {}
with open('Procfile') as f:
    for line in f:
        name, cmd = line.split(':', 1)
        procs[name.strip()] = cmd.strip()

env = dict(os.environ)
with open('.env') as f:
    for line in f:
        name, value = line.split('=', 1)
        env[name.strip()] = value.strip()


def exec_shell(shell_args):
    cmd = ['/bin/bash', '-c', ' '.join(shell_args)]
    os.execve(cmd[0], cmd, env)


def main():
    if len(sys.argv) == 2:
        proc_name = sys.argv[1].strip()
        if proc_name in procs:
            proc_cmd = procs[proc_name]
            exec_shell([proc_cmd])

    exec_shell(sys.argv[1:])


if __name__ == '__main__':
    main()
