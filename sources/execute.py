import subprocess


def adapt_cmd(cmd: list[str], os: str) -> list[str]:
    '''
    Адаптация вида команды для корректной работы на разных ОС.
    '''

    win_exe_format = "C:\\Program Files\\OpenSC Project\\OpenSC\\tools\\"
    rt_lib_name = "rtpkcs11ecp"

    # Определение позиции названия модуля в команде
    module_index = 0
    if ("pkcs11-tool" == cmd[0]):
        for i in range(len(cmd)):
            if (rt_lib_name in cmd[i]):
                module_index = i
        
    if (os == "win32"):
        if ("pkcs" in cmd[0]): cmd[0] = win_exe_format + cmd[0] + ".exe"
        if ("pkcs15" in cmd[0]): cmd.append("-r3")
        cmd[module_index] = cmd[module_index].replace(".so", "")
        if ((module_index) and not (".dll" in cmd[module_index])): cmd[module_index] += ".dll"

    elif (os == "linux"):
        cmd[module_index] = cmd[module_index].replace(".dll", "")
        if ((module_index) and not (".so" in cmd[module_index])): cmd[module_index] += ".so"
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
