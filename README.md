# potta

Installazione:
```bash
pip install potta
```

Project creation:
```bash
mkdir my_project
cd my_project
potta init --core arm_cm4 --stl no
```

Minimal files created:
```
include/
  mcu.h
src/
  main.c
SConstruct
layout.ld
startup.S
```

Build:
```bash
scons
```
