# cli.py
import typer

from kural.cmd.root import app

proxy_app = typer.Typer(
    add_completion=True, no_args_is_help=True, name="proxy", help="Gerencia o proxy"
)

app.add_typer(proxy_app)


def proxy_callback(value: str):
    if value is not None:
        print(f"Olá {value}")


@proxy_app.command(name="traefik", no_args_is_help=True)
def traefik(
    ctx: typer.Context,
    name: str = typer.Option(
        None,
        "--name",
        # callback=proxy_callback,
        help="Informe um nome para saudação",
        is_eager=False,
    ),
):
    """Sauda uma pessoa pelo nome."""

    # if name is None:
    # typer.echo("É necessário informar --name TEXT")


@proxy_app.command(name="nginx", no_args_is_help=True)
def nginx(x: int, y: int):
    """Soma dois números."""
    result = x + y
    typer.echo(f"O resultado de {x} + {y} é {result}.")
