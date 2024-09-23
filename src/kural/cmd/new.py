# cli.py
import typer

from kural.cmd.root import app

new_app = typer.Typer(
    add_completion=True, no_args_is_help=True, name="new", help="Inicia um novo projeto"
)

app.add_typer(new_app)


def new_callback(value: str):
    if value is not None:
        print(f"Olá {value}")


@new_app.command(name="create", no_args_is_help=True)
def create(
    ctx: typer.Context,
    name: str = typer.Option(
        None,
        "--name",
        # callback=new_callback,
        help="Informe um nome para saudação",
        is_eager=False,
    ),
):
    """Sauda uma pessoa pelo nome."""

    # if name is None:
    # typer.echo("É necessário informar --name TEXT")


@new_app.command(name="remove", no_args_is_help=True)
def remove(x: int, y: int):
    """Soma dois números."""
    result = x + y
    typer.echo(f"O resultado de {x} + {y} é {result}.")
