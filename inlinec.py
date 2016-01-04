import hashlib
import subprocess
import ctypes
import pathlib


class CSyntaxError(SyntaxError):
    pass


def gcc(c_code: str):
    hash_ = hashlib.sha256(c_code.encode()).hexdigest()
    c_path = "/tmp/" + hash_ + ".c"
    so_path = "/tmp/" + hash_ + ".so"

    if not pathlib.Path(so_path).is_file():
        with open(c_path, "w") as f:
            f.write(c_code)

        try:
            subprocess.run(["gcc", "-shared", "-std=c99", "-o", so_path, c_path],
                            check=True)
        except subprocess.CalledProcessError as e:
            raise CSyntaxError(e.output)

    return ctypes.cdll.LoadLibrary(so_path).f
