import typer

app = typer.Typer(add_completion=True, no_args_is_help=True)


def version_callback(value: bool):
    if value:
        print("kural v1.0.0")
        raise typer.Exit()


@app.callback()
def main(
    ctx: typer.Context,
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        help="Display Kural current version.",
        is_eager=True,
    ),
):
    # print(f"Hello Kural CLI")
    pass
