# cli.py
import typer

from kural.cmd.root import app

system_app = typer.Typer(
    add_completion=True,
    no_args_is_help=True,
    name="system",
    help="Executa comandos do sistema",
)

app.add_typer(system_app)


def saudacoes_callback(value: str):
    if value is not None:
        print(f"Olá {value}")


@system_app.command(name="saudacoes", no_args_is_help=True)
def greet(
    ctx: typer.Context,
    name: str = typer.Option(
        None,
        "--name",
        # callback=saudacoes_callback,
        help="Informe um nome para saudação",
        is_eager=False,
    ),
):
    """Sauda uma pessoa pelo nome."""

    # if name is None:
    # typer.echo("É necessário informar --name TEXT")


@system_app.command(no_args_is_help=True)
def add(x: int, y: int):
    """Soma dois números."""
    result = x + y
    typer.echo(f"O resultado de {x} + {y} é {result}.")
