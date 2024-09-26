
@echo off
echo Welcome to BashClient Launcher!

:menu
echo.
echo 1. Launch BashClient
echo 2. Install Mods
echo 3. Open Mod Manager
echo 4. Exit
set /p choice=Enter your choice: 

if %choice%==1 goto launch
if %choice%==2 goto install_mods
if %choice%==3 goto open_mod_manager
if %choice%==4 goto exit
goto menu

:launch
echo Launching BashClient...
start "" "BashClient\bashclient.exe"
goto menu

:install_mods
echo Installing Mods...
xcopy /Y /E "mods\*" "%APPDATA%\.minecraft\mods\"
echo Mods installed successfully!
goto menu

:open_mod_manager
echo Opening Mod Manager...
start "" "python" "open_mod_manager.py"
goto menu

:exit
exit
