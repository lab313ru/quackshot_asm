@echo off

set PATH=%PATH%;./bin/;

set pth=qs_as.bin

for %%i in (%pth%) do (set pth=%%~ni)

call make_cutscenes.bat
call make_fonts.bat
call make_mmenu.bat
call make_level_names.bat
call make_kosinski.bat
call make_dialogs.bat
call make_ingame_menu.bat
call make_mmenu_prestabuon.bat

asw -L -olist %pth%_list.txt -o %pth%_new.p qs_as.bin.lst
p2bin %pth%_new.p %pth%_new.bin
del %pth%_new.p /q

python checksum.py %pth%_new.bin