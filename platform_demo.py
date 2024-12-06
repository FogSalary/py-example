import platform


print("system name: ", platform.system())                   # Linux
print("system version: ", platform.version())               # #48~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Mon Oct  7 11:24:13 UTC 2
print("Processor Architecture: ", platform.architecture())  # ('64bit', 'ELF')
print(platform.node())
print(platform.processor())
print(platform.machine())
print(platform.uname())