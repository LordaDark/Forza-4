@echo off
echo === Creazione Installer Forza 4 ===

echo.
echo 1. Compilazione del gioco con PyInstaller...
pyinstaller --onefile --windowed --icon=src/assets/icon.ico --name=Forza4 src/main.py

echo.
echo 2. Creazione dell'installer con NSIS...
"C:\Program Files (x86)\NSIS\makensis.exe" installer.nsi

echo.
echo Installer creato con successo!
echo Il file di installazione si trova in: Forza4_Setup.exe

pause