import shlex
from pathlib import Path

from invoke.tasks import task # type: ignore reportUnknownVariableType
from invoke.context import Context

from functools import wraps
from typing import Callable
import inspect
from pathlib import Path


__all__ = [
    "pytest",
    "exp",
    "rufff",
    "mk_task",
    "up",
    "down",
    "build",
]



def find_task_dir(ctx: Context):
    cwd = Path(ctx.cwd).absolute()
    while cwd.parent != cwd:
        tasks = cwd / 'tasks.py'
        if tasks.exists():
            return cwd
        else:
            cwd = cwd.parent


def run(ctx: Context, cmd: list[str]):
    task_dir = find_task_dir(ctx)
    with ctx.cd(task_dir):
        cmd_str = shlex.join(cmd)

        return ctx.run(cmd_str, echo=True, pty=True)


def mk_task(fn: Callable):
    """
    Decorator for a function that returns a shell command as a list of strings and runs them in the invoke context.
    """
    @task
    @wraps(fn)
    def wrapper(ctx: Context, *args, **kwargs):
        cmd = fn(ctx, *args, **kwargs)
        return run(ctx, cmd)
    return wrapper

@task
def down(ctx: Context):
    cmd = [
        "docker",
        "compose",
        "down",
    ]
    return run(ctx, cmd)

@task(down)
def build(ctx: Context):
    cmd = [
        "docker",
        "buildx",
        "bake",
    ]
    return run(ctx, cmd)


@task(build)
def up(ctx: Context):
    cmd = [
        "docker",
        "compose",
        "up",
        # "-d",
    ]
    return run(ctx, cmd)


@mk_task
def pytest(ctx: Context):
    return [
        'poetry',
        'run',
        'python',
        '-m',
        'pytest',
        '-x',
        '-rs'
    ]


@mk_task
def rufff(ctx: Context):
    return [
        'poetry',
        'run',
        'ruff',
        'check',
        str(find_task_dir(ctx)),
        '--fix',
    ]


@mk_task
def py(ctx: Context):
    return [
        'poetry',
        'run',
        'python',
    ]


@mk_task
def exp(ctx: Context):
    return [
        'poetry',
        'run',
        'python',
        'exp.py',
    ]


@mk_task
def atr(ctx: Context):
    return [
        'poetry',
        'run',
        'autodoc2',
        'list',
        './src/what_the_doc',
    ]