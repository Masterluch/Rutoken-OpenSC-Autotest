import subprocess


def adapt_cmd(cmd: list[str], os: str) -> list[str]:
    '''
    Адаптация команды для корректной работы на разных ОС.
    '''

    win_exe_format = "C:\\Program Files\\OpenSC Project\\OpenSC\\tools\\"
    dict_rt_libs = {"win32": "rtpkcs11ecp.dll", "linux": "librtpkcs11ecp.so"}

    # Определение позиции названия модуля в команде
    module_name_index = 0
    if ("pkcs11-tool" == cmd[0]):
        for i in range(len(cmd)):
            if ("--module" in cmd[i]):
                module_name_index = i+1
    # Замена названия библиотеки
    if (module_name_index):
            if (not dict_rt_libs[os] in cmd[module_name_index]):
                cmd[module_name_index] = cmd[module_name_index].replace("rtpkcs11ecp", dict_rt_libs[os])
    
    # Общие изменения в засисимости от ОС
    if (os == "win32"):
        if ("pkcs" in cmd[0]): cmd[0] = win_exe_format + cmd[0] + ".exe"
        if ("pkcs15" in cmd[0]): cmd.append("-r3")
    elif (os == "linux"): pass
    else: raise Exception("Unsupported OS")
    
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
