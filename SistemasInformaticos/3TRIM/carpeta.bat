@ECHO OFF
@ECHO RESPALDO DE ARCHIVOS
REM creamos una variable conteniendo la fecha actual con el formato año-mes-dia
SET FOLDER=%date:~6,4%-%date:~3,2%-%date:~0,2%_%time:~0,2%%time:~3,2%
REM Creamos la carpeta donde se guardará la copia de respaldo
IF NOT EXIST Backup MKDIR Backup
MKDIR Backup%FOLDER%