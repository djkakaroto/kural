# cli.py
import typer

from kural.cmd.root import app

deploy_app = typer.Typer(
    add_completion=True,
    no_args_is_help=True,
    name="deploy",
    help="Faz o deploy da aplicação",
)

app.add_typer(deploy_app)


def deploy_callback(value: str):
    if value is not None:
        print(f":::: Deploy :::: {value}")


@deploy_app.command(name="docker", no_args_is_help=True)
def docker(
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


@deploy_app.command(name="swarm", no_args_is_help=True)
def swarm(x: int, y: int):
    """Soma dois números."""
    result = x + y
    typer.echo(f"O resultado de {x} + {y} é {result}.")


@deploy_app.command(name="kubernetes", no_args_is_help=True)
def kubernetes(x: int, y: int):
    """Soma dois números."""
    result = x + y
    typer.echo(f"O resultado de {x} + {y} é {result}.")
