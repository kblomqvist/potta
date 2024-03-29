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

First decide which tools to use and make set those to default:
```bash
potta set --global programmer=openocd  # update .potta.conf and also ~/.potta/defaults.json
potta set --global toolchain_path=`which arm-none-eabi-gcc`
```

Next init the project:
```bash
potta init                              # initialize project with default values (from ~/.potta/defaults.json)
potta set target=stm32f411ve            # update .potta.conf
potta set lang=cpp
potta fetch                             # fetches appropriate files from interweb (*.jinja, *.svd)
potta diff                              # compares local modifications to interweb versions
```

Minimal set of files created:
```
.
+-- target/
|   +-- SConscript
|   +-- target.h.jinja
|   +-- layout.ld.jinja
|   +-- startup.c.jinja
|   +-- target.svd
+-- my_project/                         <-- potta reads the basename of the cwd and use that here
|   +-- SConscript
+-- SConstruct
+-- build.py                            <-- contains potta.conf stuff?
```

Build:
```bash
scons
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
potta init
potta set --target stm32f411ve
```

will lead to the following project structure
```
.
+-- target/
|   +-- SConscript
|   +-- target.h.jinja
|   +-- layout.ld.jinja
|   +-- startup.c.jinja
|   +-- target.svd
+-- proj/
|   +-- SConscript
+-- SConstruct
+-- build.py                            <-- contains potta.conf stuff?
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

The project structure now looks like this
```
.
+-- target/
|   +-- SConscript
|   +-- target.h.jinja
|   +-- layout.ld.jinja
|   +-- startup.c.jinja
|   +-- target.svd
+-- proj/
|   +-- SConscript
|   +-- main.c
+-- SConstruct
+-- build.py
```

John would like to switch to IDE (without building the project yet). He imports the project to Eclipse by using import SCons project, and sees that there's an error showing that `target.h` does not exists. Well John needs to build to get that file.

Now John would like to hack with NVICs. He knows that CMSIS could help with that so John decides to install CMSIS.
```bash
potta add --package cmsis
```

The above command git clones cmsis botta package into `~/.potta/cmsis/` folder if not yet there, and updates the `build.py` accordingly to get the package build and linked into the proj.

To build the project SCons is directly used:
```bash
scons
```

The build is made into separate build folder (maybe with SCons duplicate=True):
```
.
+-- build/
|   +-- cmsis/
|       +-- objects.o
|   +-- target/
|       + startup.o
|   +-- proj/
|       +-- main.o
|       +-- proj.elf
|       +-- proj.hex
+-- target/
|   +-- SConscript
|   +-- target.h
|   +-- target.h.jinja
|   +-- layout.ld
|   +-- layout.ld.jinja
|   +-- startup.c
|   +-- startup.c.jinja
|   +-- target.svd
+-- proj/
|   +-- SConscript
|   +-- main.c
+-- SConstruct
+-- build.py
```

# Brainstorm

Do we need both assembly and C startups, or could we make all in C file with inline assembly.

In Moe there was SConscript files in separate dirs so maybe add here too. Also see, http://stackoverflow.com/questions/15411176/do-we-need-sconscript-file-in-every-source-directory.

## Works as Python virtualenv

```bash
potta venv foobar [--location ~/.potta]
```

## Package overlaying

```bash
potta overlay pkg [file(s)]
```

If files are not given will copy the whole package into current project folder. In other case the folder is created with the given files copied there. Also generates the SConscript to decide which files are compiled from project and which are from the original package.
