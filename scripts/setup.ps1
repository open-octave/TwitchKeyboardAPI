# PowerShell script for installation

# Note to run this script, you need to run the following in an elevated PowerShell session: `Set-ExecutionPolicy Unrestricted` 

# Install Git
Write-Output "`nVerifying installation Git installation..."
try {
    git --version | Out-Null
    Write-Output "`nGit is installed..."
} catch {
    Write-Output "`nGit is not installed."
    Write-Output "Please download and install Git from https://git-scm.com/downloads then run this script again.`n"
    exit 1
}

# Install Pyenv
Write-Output "`nVerifying installation of Pyenv..."
try {
    pyenv --version | Out-Null
    Write-Output "`nPyenv is installed..."
} catch {
    Write-Output "`nPyenv is not installed."
    Write-Output "Installing Pyenv..."

    Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"

    Write-Output "`nPyenv is installed..."
    Write-Output "Please restart your terminal and run this script again.`n"
    exit 1
}

# Install Python 3.11.9
Write-Output "`nVerifying installation of Python 3.11.9..."
pyenv install 3.11.9
pyenv global 3.11.9
Write-Output "`nPython 3.11.9 is installed..."

# Install Scoop
Write-Output "`nVerifying installation of Scoop..."
try {
    scoop --version | Out-Null
    Write-Output "`nScoop is installed..."
} catch {
    Write-Output "`nScoop is not installed."
    Write-Output "Installing Scoop..."

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
    Invoke-RestMethod -Uri "https://get.scoop.sh" | Invoke-Expression

    Write-Output "Scoop is installed..."
}


# Install Poetry with pipx
Write-Output "`nVerifying installation of Poetry..."
try {
    poetry --version | Out-Null
    Write-Output "`nPoetry is installed..."
} catch {
    Write-Output "`nPoetry is not installed."
    Write-Output "Installing Poetry..."

    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -


    if (-not (Get-Command poetry -ErrorAction Ignore)) {
        $env:Path += ";$env:APPDATA\Python\Scripts"
        [Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path", "User") + ";$env:APPDATA\Python\Scripts", "User")
    }

    poetry config virtualenvs.in-project true
    
    Write-Output "Poetry is installed..."
}


# Install Github CLI with Scoop
Write-Output "`nVerifying installation of Github CLI..."
try {
    gh --version | Out-Null
    Write-Output "`nGithub CLI is installed..."
} catch {
    Write-Output "`nGithub CLI is not installed."
    Write-Output "Installing Github CLI..."

    scoop install gh

    Write-Output "`nConfiguring Github CLI..."
    gh auth login

    Write-Output "Github CLI is installed..."
}



Write-Output "`nAll installations completed successfully."


# Note: Run the app using VSCode's play button because trying to use the terminal is not working as expected.

