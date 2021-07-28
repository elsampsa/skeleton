
## Windows tips

Business as usual - windows sucks big time and everything becomes cumbersome and difficult.  What a waste of time!

Here are some tips to get your python system up & working in windows 10+

All commands refer to **windows standard terminal**.  **NOT** windows powershell (it has semi-compatible syntax that will mess up your path if you use the commands suggested here).

First of all, **prefer installing python from python.org instead of windows store**

Next, you might (or might not) need to fix long path names in the system registry:

- Click Start, and then click Run.
- In the Open box, paste %systemroot%\syswow64\regedit , and then click OK.
- Then change: ``HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem@LongPathsEnabled to 1``

To begin with, upgrade the package manager like this:
```
pip3 install --upgrade pip
```

Then install ipython3:
```
pip3 install ipython
```

At this stage pip might complain that your installed scripts (exes, etc.) are not in $PATH, it also shows where they are installed.  So let's fix that.  Launch windows terminal *as superuser* and type:
```
C:\Windows\System32\setx /M PATH "%PATH%;C:\Path\to\python\scripts"
```
where you should substitute ``C:\Path\to\python\scripts`` with the correct you saw in the terminal.

*a windows tip: paths with spaces are appended like this:*
```
setx /M PATH "%PATH%;C:\Program Files\MiKTeX 2.9\miktex\bin\x64"
```

Close your windows terminal & start a new one.

After this, start a new terminal and test from command line:
```
ipython3
```

If it works, then congrats, you have installed python3 correctly to your system.







