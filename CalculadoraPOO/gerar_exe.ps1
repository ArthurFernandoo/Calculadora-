Write-Host "Instalando PyInstaller..." -ForegroundColor Cyan
python -m pip install pyinstaller

Write-Host "Gerando CalculadoraPOO.exe..." -ForegroundColor Cyan
python -m PyInstaller --onefile --windowed --name CalculadoraPOO main.py

Write-Host "Concluido! O arquivo esta na pasta dist\CalculadoraPOO.exe" -ForegroundColor Green
Pause
