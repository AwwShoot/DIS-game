Thanks for reading me.

I've cleaned this up so we can use it to put ideas/work that needs to be done here.
If you needed any info from the previous version, you can always check it on Github.

notes:
The screen as it is now, would form a 15x8 grid for 64x64 tiles with 48 pixels of height left over.

ideas:
Maybe snakes do increase in size when they bounce the ball
how will tetris pieces be placed?
maybe the ball destroys tetris tiles on impact, adding brick breaker into the mix as well.
how hard will it be to score? to win?


pyinstaller commands

pyi-makespec src/main/main.py <-- makes the specification file for the .exe to be in a folder with all of it's dependencies outside
pyi-makespec --onefile src/main/main.py <-- spec file for the .exe to contain it's dependencies
("src/assets", "src/assets") <-- put this in the "datas" section of the .spec file to include the non-code assets
pyinstaller main.spec <-- makes the .exe from a spec file
