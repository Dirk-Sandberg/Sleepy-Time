# Sleepy-Time
Shuts off PC at 9pm every night

Abort the shutdown if you REALLY need to spend more time on the PC by opening a command prompt and typing 'shutdown -a', then kill the running Python process in Task Manager.

Uses a .pyw file extension instead of .py so that pythonw.exe is the program that runs it, which omits the use of a command prompt.

Put the program in your windows startup scripts folder (C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp) to make the program launch by itself when your PC is turned back on.
