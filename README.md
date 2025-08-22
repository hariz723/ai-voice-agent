# AI Voice Agent

This project implements an AI voice agent. Its purpose is to provide a conversational interface, likely utilizing speech-to-text and text-to-speech capabilities, along with some form of AI model for processing and generating responses.

## Setup Instructions

This project uses [Poetry](https://python-poetry.org/) for dependency management.

1.  **Install Poetry**:
    If you don't have Poetry installed, you can install it using pip:
    ```bash
    pip install poetry
    ```

2.  **Initialize Project (if not already done)**:
    Navigate to the project root directory and initialize Poetry. This will create a `pyproject.toml` file.
    ```bash
    poetry init --no-interaction
    ```
    If `poetry` command is not directly in your PATH, you might need to use:
    ```bash
    python -m poetry init --no-interaction
    ```

3.  **Install Dependencies**:
    Once `pyproject.toml` is set up, install all project dependencies:
    ```bash
    poetry install
    ```

## How to Run the Project

1.  **Activate the Poetry Shell**:
    This command activates the virtual environment managed by Poetry.
    ```bash
    poetry shell
    ```

2.  **Run the Agent**:
    Assuming `agent.py` is the main entry point, you can run the project using:
    ```bash
    python agent.py
    ```

## Project Structure

*   `agent.py`: The main script for the AI voice agent.
*   `constants.py`: Contains constant values used throughout the project.
*   `prompt.py`: Likely contains the prompts or templates for the AI model.
*   `pyproject.toml`: Poetry configuration file for project metadata and dependencies.
*   `README.md`: This file.
*   `.env.example`: Example file for environment variables.
*   `.gitignore`: Specifies intentionally untracked files to ignore.
*   `requirements.txt`: (Legacy) May contain initial dependencies, but Poetry is now used.
