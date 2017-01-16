# potta

Installazione:
```bash
pip install potta
```

Project creation:
```bash
mkdir my_project
cd my_project
```

```bash
potta init --core arm_cm4 --compiler gcc --stl no
```

```bash
potta init --mcu stm32f411ve --compiler gcc  # Core is known from the MCU
```

Minimal files created:
```
include/
  mcu.h.j2
  mcu.svd
src/
  main.c
SConstruct
custom.py
layout.ld.j2
startup.S.j2
```

Build:
```bash
scons
```

---

Some files could also be put into `~/.potta`.
