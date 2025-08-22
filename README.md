# AI Voice Agent

This project implements an AI voice agent. Its purpose is to provide a conversational interface, likely utilizing speech-to-text and text-to-speech capabilities, along with some form of AI model for processing and generating responses.

## Setup Instructions

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

## Setup Instructions

1.  **Install uv**:
    If you don't have `uv` installed, you can install it using pip:
    ```bash
    pip install uv
    ```
    Alternatively, you can follow the official installation instructions for `uv` to get the standalone executable.

2.  **Initialize Project (if not already done)**:
    Navigate to the project root directory and initialize `pyproject.toml` if it doesn't exist. `uv` works with `pyproject.toml` directly. If you need to create one, you can use `poetry init` or create it manually. For now, we assume `pyproject.toml` is present.

3.  **Install Dependencies**:
    Install all project dependencies using `uv`:
    ```bash
    uv sync
    ```
    This command will create a virtual environment and install dependencies based on `pyproject.toml` and `uv.lock`.

## How to Run the Project

1.  **Activate the uv Virtual Environment**:
    `uv` automatically manages the virtual environment. You can run commands within it using `uv run`.

2.  **Run the Agent**:
    To use the turn-detector, silero, or noise-cancellation plugins, you first need to download the model files:
    ```bash
    uv run agent.py download-files
    ```
    Then, you can run the main agent console:
    ```bash
    uv run agent.py console
    ```

## Project Structure

*   `agent.py`: The main script for the AI voice agent.
*   `constants.py`: Contains constant values used throughout the project.
*   `prompt.py`: Likely contains the prompts or templates for the AI model.
*   `pyproject.toml`: Poetry configuration file for project metadata and dependencies.
*   `README.md`: This file.
*   `.env.example`: Example file for environment variables.
*   `.gitignore`: Specifies intentionally untracked files to ignore.
