# cli.py
import typer

from kural.cmd.root import app

db_app = typer.Typer(
    add_completion=True,
    no_args_is_help=True,
    name="database",
    help="Gerencia tarefas com o banco de dados",
)

app.add_typer(db_app)


def database_callback(value: str):
    if value is not None:
        print(f"Olá {value}")


@db_app.command(name="sync", no_args_is_help=True)
def sync(
    ctx: typer.Context,
    name: str = typer.Option(
        None,
        "--name",
        # callback=database_callback,
        help="Informe um nome para saudação",
        is_eager=False,
    ),
):
    """Sauda uma pessoa pelo nome."""

    # if name is None:
    # typer.echo("É necessário informar --name TEXT")


@db_app.command(name="backup", no_args_is_help=True)
def backup(x: int, y: int):
    """Soma dois números."""
    result = x + y
    typer.echo(f"O resultado de {x} + {y} é {result}.")


@db_app.command(name="migration", no_args_is_help=True)
def migration(x: int, y: int):
    """Soma dois números."""
    result = x + y
    typer.echo(f"O resultado de {x} + {y} é {result}.")
