import os
import select
import subprocess
from shlex import quote


class editor_toolbox():
    # fake module
    __slots__ = ()

    def __new__(cls, *args, **kwargs):
        raise RuntimeError(f"{cls!r}" " should not be instantiated")
        
    @staticmethod
    def vim(filename, num, col):
        """
        open file on vim at line number and column
        """
        if col is None:
            col = 0
        return (
            "gvim",
            "--remote-silent",
            "+cal cursor(" f"{num},{col}" ")",
            quote(filename),
        ), None

def cmd_exists(cmd):
    import subprocess
    return (subprocess.call(
        cmd, shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ) == 0)

def main():
    # print(cmd_exists(''))

    # cmd = editor_toolbox.vim('prctice.py', 9, None)
    
    test_file = 'toolbox.py'

    # unpack
    cmd, env = editor_toolbox.vim(test_file, 53, None)
    if env:
        os.environ.update(env)

    print(cmd)
    import subprocess
    process = subprocess.Popen(
        cmd,
    )

    process.wait()
    _, stderr = process.communicate()
    if stderr:
        print(stderr)


main()
