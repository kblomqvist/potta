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

```bash
potta init   # initialize project with default values (from ~/.potta)
potta set --target stm32f411ve # update .potta.conf
potta set --compiler gcc
potta set --global --programmer openocd  # update .potta.conf and also ~/.potta
potta set --compiler_path /path/gcc-arm-4.7.0 --linker-path /path/ld-arm-4.7.0
potta set --lang cpp
potta fetch  # fetches appropriate files from interweb (*.jinja, *.svd)
potta diff   # compares local modifications to interweb versions
```

Minimal set of files created:
```
.potta.conf
include/
  mcu.h.jinja
  mcu.svd
src/
  main.c
SConstruct
custom.py
layout.ld.jinja
startup.S.jinja
```

Build:
```bash
scons  # Will generate mcu.h, layout.ld and startup.S
```

---

Some files could also be put into `~/.potta`.
