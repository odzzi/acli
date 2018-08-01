rem @echo off
set CUR_DIR=%cd%
set DIR=%~dp0

cd %DIR%
python -m acli.main %CUR_DIR% %*

cd %CUR_DIR%