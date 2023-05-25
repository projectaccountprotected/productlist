import subprocess


batch_file = r'C:\Users\gusta\WebExtract\Final Json for Bit Hub\commands.bat'

subprocess.call(['start', 'cmd', '/k', batch_file], shell=True)