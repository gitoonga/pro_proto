# setup_venv.ps1
# This script sets up a Python virtual environment for the project.

$VENV_DIR = ".venv"

# 1. Check if Python is installed
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Error "Python is not installed or not in your PATH. Please install Python 3.x."
    exit 1
}

# 2. Create virtual environment if it doesn't exist
if (!(Test-Path $VENV_DIR)) {
    Write-Host "Creating virtual environment in '$VENV_DIR'..." -ForegroundColor Cyan
    python -m venv $VENV_DIR
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Failed to create virtual environment."
        exit 1
    }
} else {
    Write-Host "Virtual environment '$VENV_DIR' already exists." -ForegroundColor Yellow
}

# 3. Upgrade pip and install requirements
Write-Host "Installing/Updating requirements..." -ForegroundColor Cyan
& ".\$VENV_DIR\Scripts\python.exe" -m pip install --upgrade pip
if (Test-Path "requirements.txt") {
    & ".\$VENV_DIR\Scripts\python.exe" -m pip install -r requirements.txt
} else {
    Write-Host "No requirements.txt found. Installing basic 'protobuf' library..." -ForegroundColor Yellow
    & ".\$VENV_DIR\Scripts\python.exe" -m pip install protobuf
}

Write-Host "`nSetup complete!" -ForegroundColor Green
Write-Host "To activate the virtual environment, run:" -ForegroundColor White
Write-Host ".\$VENV_DIR\Scripts\Activate.ps1" -ForegroundColor Green
