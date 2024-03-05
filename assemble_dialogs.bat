@echo off

set PATH=%PATH%;./bin/;

asw -L -olist src\dialogs\kosinski_dialogs_dec_list.txt -o src\dialogs\kosinski_dialogs_dec_new.p src\dialogs\kosinski_dialogs_dec.bin.lst
p2bin src\dialogs\kosinski_dialogs_dec_new.p src\dialogs\kosinski_dialogs_new.bin
del src\dialogs\kosinski_dialogs_dec_new.p /q