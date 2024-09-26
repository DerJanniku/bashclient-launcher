
@echo off
echo Welcome to BashClient Launcher!

:menu
echo.
echo 1. Launch BashClient
echo 2. Install Mods
echo 3. Run Auto-Translator
echo 4. Start Java Backend
echo 5. Start Minecraft Client
echo 6. Exit
set /p choice=Enter your choice: 

if %choice%==1 goto launch
if %choice%==2 goto install_mods
if %choice%==3 goto run_translator
if %choice%==4 goto start_java_backend
if %choice%==5 goto start_minecraft_client
if %choice%==6 goto exit
goto menu

:launch
echo Launching BashClient...
start "" "BashClientashclient.exe"
goto menu

:install_mods
echo Installing Mods...
xcopy /Y /E "mods\*" "%APPDATA%\.minecraft\mods"
echo Mods installed successfully!
goto menu

:run_translator
echo Running Auto-Translator...
start "" "python" "translationsun_translator.py"
goto menu

:start_java_backend
echo Starting Java Backend...
start "" "cmd" /c "cd java-backend && java -jar build\libs\java-backend-1.0-SNAPSHOT.jar"
goto menu

:start_minecraft_client
echo Starting Minecraft Client...
start "" "cmd" /c "cd minecraft-client && java -jar build\libs\minecraft-client-1.0-SNAPSHOT.jar"
goto menu

:exit
exit
