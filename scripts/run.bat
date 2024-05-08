@echo off

:: Verify that Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python could not be found, please install Python.
    exit /b
)

:: Verify that Poetry is installed
where poetry >nul 2>nul
if %errorlevel% neq 0 (
    echo Poetry could not be found, installing Poetry...
    (curl -sSL https://install.python-poetry.org | powershell -)
)

:: Install dependencies using Poetry
poetry install

:: Run the application
poetry run python ./twitch_keyboard_api/__main__.py