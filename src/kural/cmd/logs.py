# cli.py
import typer

from kural.cmd.root import app

logs_app = typer.Typer(
    add_completion=True,
    no_args_is_help=True,
    name="logs",
    help="Mostra os logs para auditoria",
)

app.add_typer(logs_app)


def logs_callback(value: str):
    if value is not None:
        print(f"Olá {value}")


@logs_app.command(name="app", no_args_is_help=True)
def app(
    ctx: typer.Context,
    name: str = typer.Option(
        None,
        "--name",
        # callback=logs_callback,
        help="Informe um nome para saudação",
        is_eager=False,
    ),
):
    """Sauda uma pessoa pelo nome."""

    # if name is None:
    # typer.echo("É necessário informar --name TEXT")


@logs_app.command(name="proxy", no_args_is_help=True)
def proxy(x: int, y: int):
    """Soma dois números."""
    result = x + y
    typer.echo(f"O resultado de {x} + {y} é {result}.")
