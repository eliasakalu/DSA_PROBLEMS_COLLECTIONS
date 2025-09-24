@echo off
setlocal enabledelayedexpansion

:: Check if arguments are missing
if "%~1"=="" (
    echo Usage: add_problem "Problem Name" "File Name With Extension"
    echo Example: add_problem "Binary Search" "binary_search.py"
    goto end
)

:: Store arguments safely
set "problem_name=%~1"
set "file_name=%~2"

:: Update README.md
echo - [!problem_name!](./!file_name!) >> README.md

:: Git operations
git add .
git commit -m "Add !problem_name! problem"
git push origin main

echo ✓ Added '!problem_name!' to GitHub!

:end
endlocal


@REM @echo off
@REM :: Check if first argument is missing
@REM if "%1"=="" (
@REM     echo Usage: add_problem "Problem Name" "File Name With Extension"
@REM     echo Example: add_problem "Binary Search" "binary_search.py"
@REM     goto end
@REM )
@REM :: Store arguments in variables
@REM set problem_name=%1
@REM set file_name=%2

@REM :: Update README.md
@REM echo - [%problem_name%](./%file_name%)>>README.md

@REM ::Git Operation to add,commit and push
@REM git add .
@REM git commit -m "Add \"%problem_name%\" problem"
@REM git push origin main

@REM echo ✓ Added '%problem_name%' to GitHub!

@REM :end