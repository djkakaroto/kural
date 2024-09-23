import pytest
from typer.testing import CliRunner
from kural.cmd.root import app  # Importa sua aplicação Typer

runner = CliRunner()


def test_hello():
    # Chama o comando com um argumento
    result = runner.invoke(app, ["hello", "Mundo"])

    # Verifica se o comando foi executado com sucesso
    assert result.exit_code == 0
    assert result.output.strip() == "Olá, Mundo!"
