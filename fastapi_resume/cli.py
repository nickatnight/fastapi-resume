from pathlib import Path

import typer
import uvicorn

from fastapi_resume.utils import create_api, load_resume_data


app = typer.Typer(
    name="fast-resume",
    help="FastAPI Resume API Server",
    add_completion=False,
    rich_markup_mode="markdown",
)


@app.command()
def serve(
    data_file: str = typer.Argument(..., help="Path to the YAML data file"),
    host: str = typer.Option("0.0.0.0", "--host", "-h", help="Host to bind to"),
    port: int = typer.Option(8000, "--port", "-p", help="Port to bind to"),
    log_level: str = typer.Option(
        "info",
        "--log-level",
        "-l",
        help="Log level (debug, info, warning, error)",
        case_sensitive=False,
    ),
) -> None:
    """
    Start the FastAPI Resume API server.

    Provide the path to your YAML data file to serve your resume via API.

    Available endpoints:

    * /

    * /basic

    * /experience

    * /education

    * /skills

    * /projects

    * /contact

    ---

    View at localhost:8000/
    """
    # Validate data file exists
    data_path = Path(data_file)
    if not data_path.exists():
        typer.echo(f"Error: Data file '{data_file}' not found", err=True)
        raise typer.Exit(1)

    if not data_path.is_file():
        typer.echo(f"Error: '{data_file}' is not a file", err=True)
        raise typer.Exit(1)

    # Show startup information
    typer.echo("🚀 Starting Resume API server...")
    typer.echo(f"📁 Data file: {data_path.absolute()}")
    typer.echo(f"🌐 Server: http://{host}:{port}")
    typer.echo(f"🔗 API docs: http://{host}:{port}/docs")

    try:
        api = create_api(data_file=str(data_path.absolute()))

        # Start the server
        uvicorn.run(
            api,
            host=host,
            port=port,
            log_level=log_level.lower(),
        )
    except KeyboardInterrupt:
        typer.echo("\n👋 Server stopped by user")
    except Exception as e:
        typer.echo(f"❌ Error starting server: {e}", err=True)
        raise typer.Exit(1)


@app.command()
def validate(
    data_file: str = typer.Argument(..., help="Path to the YAML data file to validate"),
) -> None:
    """
    Validate a YAML data file without starting the server.
    """
    data_path = Path(data_file)

    if not data_path.exists():
        typer.echo(f"❌ Error: Data file '{data_file}' not found", err=True)
        raise typer.Exit(1)

    try:
        data = load_resume_data(str(data_path))
    except Exception as e:
        typer.echo(f"❌ Error validating file: {e}", err=True)
        raise typer.Exit(1)

    # Basic validation
    required_fields = ["name", "about", "position"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        typer.echo(
            f"⚠️  Warning: Missing recommended fields: {', '.join(missing_fields)}"
        )
    else:
        typer.echo("✅ All recommended fields present")

    typer.echo(f"✅ YAML file is valid and contains {len(data)} top-level keys")
    typer.echo(
        f"👤 Name: {data.get('name', {}).get('first', 'N/A')} {data.get('name', {}).get('last', 'N/A')}"
    )
    typer.echo(f"💼 Position: {data.get('position', 'N/A')}")


@app.command()
def info(
    data_file: str = typer.Argument(..., help="Path to the YAML data file"),
) -> None:
    """
    Display information about the resume data without starting the server.
    """
    data_path = Path(data_file)

    if not data_path.exists():
        typer.echo(f"❌ Error: Data file '{data_file}' not found", err=True)
        raise typer.Exit(1)

    try:
        data = load_resume_data(str(data_path))
    except Exception as e:
        typer.echo(f"❌ Error reading file: {e}", err=True)
        raise typer.Exit(1)

    typer.echo("📃📃 Resume Information:")
    typer.echo(
        f"  Name: {data.get('name', {}).get('first', 'N/A')} {data.get('name', {}).get('last', 'N/A')}"
    )
    typer.echo(f"  Position: {data.get('position', 'N/A')}")
    typer.echo(f"  Experience entries: {len(data.get('experience', []))}")
    typer.echo(f"  Education entries: {len(data.get('education', []))}")
    typer.echo(f"  Skill categories: {len(data.get('skills', []))}")
    typer.echo(f"  Projects: {len(data.get('projects', []))}")

    if data.get("contact"):
        contact = data["contact"]
        typer.echo(f"  Contact: {contact.get('email', 'N/A')}")
