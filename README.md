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

# User story

John Doe wants to start developing for STM32F411VE (ARM CM4 core). For start he wants the minimal repo to blink an LED by bitbanging the peripheral register. John already has Potta installed (with default values).

First create project folder:
```
mkdir workspace/proj
cd workspace/proj
```

The project initialization
```bash
potta init --target stm32f411ve
```

will lead to the following project structure
```bash
.
+-- target/
|   +-- target.h.jinja
|   +-- target.ld.jinja
|   +-- target.s.jinja
|   +-- target.svd
+-- proj/
+-- SConstruct
+-- build.py
```

John starts to write the main function into `proj/main.c`.
```c
#include <target/target.h>              // By default the root of the proj is put into include path

int main() {
    RCC->AHBENR |= RCC_AHBENR_GPIOCEN;  // Enable clocks for GPIOC
    GPIOC->MODER |= (1<<16);            // Define PC08 as output
    GPIOC->BSRR = (1<<8);               // Make PC08 high
    while(1);
    // See, http://hertaville.com/stm32f0-gpio-tutorial-part-1.html
}
```

John would like to switch to IDE (without building the project yet). He imports the project to Eclipse by using import SCons project, and sees that there's an error showing that `target.h` does not exists. Well John needs to build to get that file.
