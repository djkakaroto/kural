# cli.py
import typer

from kural.cmd.root import app

rollback_app = typer.Typer(
    add_completion=True,
    no_args_is_help=True,
    name="rollback",
    help="Faz o rollback da aplicação",
)

app.add_typer(rollback_app)


def history_callback(value: str):
    if value is not None:
        print(f"Olá {value}")


@rollback_app.command(name="rollback", no_args_is_help=True)
def rollback(
    ctx: typer.Context,
    name: str = typer.Option(
        None,
        "--name",
        callback=history_callback,
        help="Informe um nome para saudação",
        is_eager=False,
    ),
):
    """Mostra os rollbacks."""

    # if name is None:
    # typer.echo("É necessário informar --name TEXT")


@rollback_app.command(name="history", no_args_is_help=True)
def history():
    """History do rollback."""
    typer.echo("O history")
