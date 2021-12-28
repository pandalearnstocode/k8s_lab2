import typer
from loguru import logger
from core.main import hello_world


app = typer.Typer()


@app.command("hello")
def hw():
    hello_world()


if __name__ == "__main__":
    logger.info("Starting CLI application")
    app()
    logger.info("Ending CLI application")