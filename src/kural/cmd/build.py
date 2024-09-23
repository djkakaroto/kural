# cli.py
import typer

from kural.cmd.root import app

build_app = typer.Typer(
    add_completion=True,
    no_args_is_help=True,
    name="build",
    help="Faz build da aplicação usando dockefile",
)

app.add_typer(build_app)


def build_callback(value: str):
    if value is not None:
        print(f"Olá {value}")


@build_app.command(name="create", no_args_is_help=True)
def create(
    ctx: typer.Context,
    name: str = typer.Option(
        None,
        "--name",
        callback=build_callback,
        help="Informe um nome para saudação",
        is_eager=False,
    ),
):
    """Cria o build do app."""

    # if name is None:
    # typer.echo("É necessário informar --name TEXT")


@build_app.command(name="remove", no_args_is_help=True)
def remove(x: int, y: int):
    """Soma dois números."""
    result = x + y
    typer.echo(f"O resultado de {x} + {y} é {result}.")
