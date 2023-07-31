import subprocess


def execute(cmd: list[str], stdin: subprocess._FILE = None, stdout: subprocess._FILE = None) -> subprocess.CompletedProcess:
    '''
    Исполнение команд с последуещей проверкой кода выхода.
    Обёртка над subprocess.run().
    '''
    
    process = subprocess.run(cmd, stdin=stdin, stdout=stdout, stderr=subprocess.PIPE)
    if (process.returncode != 0): raise Exception(process.stderr)

    return process
