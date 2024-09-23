# cli.py
import typer

from kural.cmd.root import app

config_app = typer.Typer(
    add_completion=True,
    no_args_is_help=True,
    name="config",
    help="Mostra a configuração atual do projeto",
)

app.add_typer(config_app)


def config_callback(value: str):
    if value is not None:
        print(f"Olá {value}")


@config_app.command(name="create", no_args_is_help=True)
def create(
    ctx: typer.Context,
    name: str = typer.Option(
        None,
        "--name",
        callback=config_callback,
        help="Informe um nome para saudação",
        is_eager=False,
    ),
):
    """Cria arquivo de configuração."""

    # if name is None:
    # typer.echo("É necessário informar --name TEXT")
