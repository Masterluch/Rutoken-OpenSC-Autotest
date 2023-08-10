import subprocess


def adapt_cmd(cmd: list[str], os: str) -> list[str]:
    '''
    Адаптация вида команды для корректной работы на разных ОС.
    '''

    win_exe_format = "C:\\Program Files\\OpenSC Project\\OpenSC\\tools\\"
        
    if (os == "win32"):
        if ("pkcs" in cmd[0]): cmd[0] = win_exe_format + cmd[0] + ".exe"
        if ("pkcs15" in cmd[0]): cmd.append("-r3")
    elif (os == "linux"):
        pass
    else:
        raise Exception("Unsupported OS")
    
    return cmd
    

def execute(original_cmd: list[str], os: str, stdin = None, stdout = None) -> subprocess.CompletedProcess:
    '''
    Исполнение команд с последуещей проверкой кода выхода.
    Обёртка над subprocess.run().
    '''

    cmd = adapt_cmd(original_cmd, os)
    process = subprocess.run(cmd, stdin=stdin, stdout=stdout, stderr=subprocess.PIPE)
    if (process.returncode != 0): raise Exception(process.stderr)

    return process
