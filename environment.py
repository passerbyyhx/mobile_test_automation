import subprocess


def after_all(context):
    try:
        subprocess.Popen("taskkill -f -im qemu-system-x86_64.exe", shell=True, stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    except:
        pass
