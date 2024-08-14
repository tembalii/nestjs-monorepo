import os
import shlex
import subprocess
import sys

import commands
import popen2
from fastapi import FastAPI

app = FastAPI()


@app.get("/direct/{input}")
def direct_response(input: str):

    tainted = input
    rand = os.urandom()

    # ok: tainted-os-command-stdlib-fastapi
    os.putenv("var", tainted)

    # deepruleid: tainted-os-command-stdlib-fastapi
    os.startfile(r"root/path/" + tainted)

    # deepruleid: tainted-os-command-stdlib-fastapi
    os.startfile(tainted, "print")

    # deepruleid: tainted-os-command-stdlib-fastapi
    os.startfile(tainted, "compile")

    # ok: tainted-os-command-stdlib-fastapi
    os.startfile("filename", "compile", tainted)  # <- args can be tainted as well

    # deepruleid: tainted-os-command-stdlib-fastapi
    os.system(tainted)

    if rand == 1:
        # ok: tainted-os-command-stdlib-fastapi
        os.execl(
            sys.executable,
            sys.executable,
            "-m",
            "promptflow._cli._pf.entry",
            *sys.argv[1:]
        )

    if rand == 1:
        # deepruleid: tainted-os-command-stdlib-fastapi
        os.execl(tainted, tainted, "-m", "promptflow._cli._pf.entry", *sys.argv[1:])

    if rand == 1:
        # ok: tainted-os-command-stdlib-fastapi
        os.execl(
            sys.executable, sys.executable, "-m", "promptflow._cli._pf.entry", tainted
        )

    if rand == 1:
        # deepruleid: tainted-os-command-stdlib-fastapi
        os.execv(tainted, ["arg1", "arg2"])

    if rand == 1:
        # deepruleid: tainted-os-command-stdlib-fastapi
        os.execve(tainted, ["arg1", "arg2"], sys.env)

    # deepok: tainted-os-command-stdlib-fastapi
    os.popen(tainted)

    # deepok: tainted-os-command-stdlib-fastapi
    popen2.popen2(tainted)
    # deepok: tainted-os-command-stdlib-fastapi
    popen2.popen3(tainted)
    # deepok: tainted-os-command-stdlib-fastapi
    popen2.Popen3(tainted)

    # deepruleid: tainted-os-command-stdlib-fastapi
    os.posix_spawn(tainted, ["arg1", "arg2"], sys.env, setsid=False)
    # ok: tainted-os-command-stdlib-fastapi
    os.posix_spawn("cmd", [tainted, "arg2"], sys.env, setsid=False)
    # ok: tainted-os-command-stdlib-fastapi
    os.posix_spawn("cmd", ["arg1", "arg2"], tainted, setsid=False)

    # deepruleid: tainted-os-command-stdlib-fastapi
    os.spawnle(os.P_NOWAITO, tainted, *sys.args, sys.env)
    # ok: tainted-os-command-stdlib-fastapi
    os.spawnle(os.P_NOWAITO, shlex.quote(tainted), *sys.args, sys.env)
    # ok: tainted-os-command-stdlib-fastapi
    os.spawnle(os.P_NOWAITO, "myfile.py", *sys.args, tainted)
    # ok: tainted-os-command-stdlib-fastapi
    os.spawnle(os.P_NOWAITO, "myfile.py", [tainted, "arg2"], sys.env)
    # deepruleid: tainted-os-command-stdlib-fastapi
    os.spawnl(os.P_NOWAIT, tainted)
    # ok: tainted-os-command-stdlib-fastapi
    os.spawnl(os.P_NOWAIT, "setup.exe")

    # ok: tainted-os-command-stdlib-fastapi
    subprocess.run(tainted, shell=True)
    # ok: tainted-os-command-stdlib-fastapi
    subprocess.run(["cmd", tainted], shell=False)
    # deepruleid: tainted-os-command-stdlib-fastapi
    subprocess.run([tainted, "arg1"], shell=False)
    # deepruleid: tainted-os-command-stdlib-fastapi
    subprocess.run("mycommand", shell=False, env=tainted)

    # deepok: tainted-os-command-stdlib-fastapi
    subprocess.Popen("mycommand", shell=False, executable=tainted)

    # ok: tainted-os-command-stdlib-fastapi
    subprocess.Popen(
        "cc" + ["-E", "-P", "-x", "-"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    subprocess.Popen(
        "cc" + ["-E", "-P", "-x", "-"],
        stdin=subprocess.PIPE,
        # deepok: tainted-os-command-stdlib-fastapi
        env=tainted,
        stdout=subprocess.PIPE,
    )

    # deepruleid: tainted-os-command-stdlib-fastapi
    commands.getoutput(tainted)
    # deepruleid: tainted-os-command-stdlib-fastapi
    commands.getstatusoutput(tainted)
