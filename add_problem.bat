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


::@echo off
:: Check if first argument is missing
::if "%1"=="" (
   :: echo Usage: add_problem "Problem Name" "File Name With Extension"
   :: echo Example: add_problem "Binary Search" "binary_search.py"
   :: goto end
::)
:: Store arguments in variables
::set problem_name=%1
::set file_name=%2

:: Update README.md
::echo - [%problem_name%](./%file_name%)>>README.md

::Git Operation to add,commit and push
::git add .
::git commit -m "Add \"%problem_name%\" problem"
::git push origin main

::echo ✓ Added '%problem_name%' to GitHub!

:::end