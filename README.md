# clings

`clings` 是一套面向 C 语言的动手练习集，参考
[rustlings](https://github.com/rust-lang/rustlings)、
[cpplings](https://github.com/nooneknowspeter/cpplings) 和
[cplings](https://github.com/rdjondo/cplings) 的组织方式，
并结合《C 语言深度解剖》的知识点设计。

每个练习都是一个可以独立编译和运行的 C 程序。初始文件故意保留
`TODO`、错误表达式或编译错误；你需要修改代码，让编译和测试通过。
练习覆盖从入门语法到指针、内存、预处理器、未定义行为、C11/C17
高级特性的完整路径。

## 特性

- **167 个练习，20 个主题**：从 `Hello, C!` 到多翻译单元、字符 I/O、
  数据结构、文件 I/O、线程和原子操作。
  `_Generic`。
- **自带测试框架**：不依赖 Catch2、GoogleTest 或第三方库。
- **自带 CLI**：列出、运行、提示、查看答案、重置进度和监听文件变化。
- **严格的编译反馈**：默认使用 `-Wall -Wextra -Wpedantic -Werror`，
  让你习惯阅读编译器诊断。
- **答案与初始模板分离**：`solutions/` 保存参考答案，
  `templates/` 保存原始练习，`exercises/` 是你实际修改的目录。
- **现代工程结构**：Makefile、CMake Presets、CTest、CI、Docker、
  clang-format、EditorConfig。
- **书籍参考**：PDF 已转换为 Markdown，并建立练习与章节的映射。

## 快速开始

### 环境要求

- C 编译器：GCC 或 Clang（C17；部分高级练习需要 POSIX 线程）
- Python 3.8+（运行 `./clings` CLI）
- GNU Make（可选）
- CMake 3.20+（可选）

Linux 上通常只需要：

```sh
sudo apt install build-essential python3
```

### 运行

```sh
# 查看全部练习
./clings list

# 运行下一个未完成的练习
./clings run

# 运行指定练习（支持完整 ID、目录名或唯一后缀）
./clings run 01_hello_world
./clings run 01_types_variables/01_integer_types

# 查看提示
./clings hint 01_hello_world

# 查看参考答案
./clings solution 01_hello_world

# 直接应用答案（会覆盖你的练习文件）
./clings solution 01_hello_world --apply

# 恢复初始练习
./clings reset 01_hello_world

# 监听文件变化，保存后自动重跑
./clings watch 01_hello_world
```

也可以使用 Makefile：

```sh
make list
make run
make verify
make selftest
make doctor
make clean
```

## 学习流程

1. 阅读 `exercises/<topic>/README.md` 和练习文件顶部的目标、书籍参考。
2. 修改 `exercises/<topic>/<exercise>.c`，运行 `./clings run <exercise>`。
3. 如果卡住，先用 `./clings hint <exercise>`，再看编译器或测试输出。
4. 通过后继续下一个练习；进度记录在 `.clings/progress.json`。
5. 完成一个主题后，对照 `docs/knowledge-map.md` 检查是否理解相关概念。
6. 最后运行 `./clings verify` 验证所有参考答案，或运行
   `./clings selftest` 检查项目自身的完整性。

有些练习一开始会**编译失败**，这是刻意的：练习目标之一就是学会根据
编译器诊断定位问题。另一些练习可以编译，但测试会失败。

## 练习主题

| 主题 | 练习数 | 主要内容 |
| --- | ---: | --- |
| `00_getting_started` | 9 | 程序结构、编译流程、`argc/argv`、断言、编译器诊断、`main` 返回值、标准版本 |
| `01_types_variables` | 11 | 整数/浮点类型、符号、溢出、字符、存储类、限定符、八进制常量、`char` 符号性 |
| `02_operators` | 9 | 算术、优先级、短路求值、位运算、移位、`sizeof`、复合赋值、赋值/相等、最长匹配 |
| `03_control_flow` | 9 | `if`、`switch`、循环、`break/continue`、`goto`、状态机、分号陷阱、悬挂 `else` |
| `04_functions` | 8 | 声明/定义、参数、递归、尾递归、`static`、函数指针、`void/return` |
| `05_arrays_strings` | 11 | 数组、数组退化、多维数组、字符串、`snprintf`、分词、VLA、复合字面量、不对称边界 |
| `06_pointers` | 10 | 指针基础、`NULL`、指针运算、二级指针、`void *`、野指针、`NULL`/空串、one-past |
| `07_dynamic_memory` | 8 | `malloc/calloc/realloc/free`、泄漏、越界、柔性数组、链表、free 后 realloc |
| `08_structs_unions_enums` | 12 | 结构体、嵌套、对齐、位域、联合、枚举、`typedef`、结构体数组/传参/文件、复杂声明 |
| `09_preprocessor` | 13 | 对象宏、函数宏、`#`/`##`、条件编译、头文件保护、变参宏、X-macro、宏空格/语句/类型陷阱 |
| `10_stdlib_io` | 16 | `printf/scanf`、高级格式化、`strtol`、`qsort/bsearch`、`math.h`、`time.h`、随机数、`RAND_MAX`、文件 I/O、`mem*`、`ctype.h` |
| `11_ub_safety` | 8 | 有符号溢出、未初始化、越界、释放后使用、序列点、严格别名、对齐、空指针 |
| `12_advanced_c` | 11 | 变参函数、`setjmp/longjmp`、POSIX 线程、C11 原子、`_Generic`、静态断言、对齐、匿名联合、`_Thread_local`、复数、信号 |
| `13_translation_units` | 4 | 头文件/源文件分离、跨文件 `extern`、`static` 内部链接、外部类型检查 |
| `14_character_io` | 5 | `getc/putc`、`EOF/feof/ferror`、输入验证、`iso646.h`、`getchar/putchar` |
| `15_string_functions` | 5 | `strcat/strncat`、`strncpy`、`sprintf/snprintf`、`fgets`、字符串排序、`strtod` |
| `16_data_representation` | 4 | 进制转换、整数位表示、浮点位表示、位域与掩码 |
| `17_data_structures` | 3 | 队列 ADT、二叉查找树、动态数组 |
| `18_file_io_advanced` | 7 | `fprintf/fscanf`、`fgets/fputs`、`ungetc`、`fseek/ftell`、缓冲、二进制随机访问、缓冲输出+内存 |
| `19_modern_c_library` | 4 | `_Noreturn`、`tgmath.h`、`atexit`、`atomic_flag` |

总计 **167 个练习**。完整映射见 [docs/curriculum.md](docs/curriculum.md)
和 [docs/knowledge-map.md](docs/knowledge-map.md)。

## 项目结构

```text
.
├── clings                     # 零依赖 Python CLI
├── exercises/                 # 你要修改的练习
│   ├── 00_getting_started/
│   ├── ...
│   └── 12_advanced_c/
├── solutions/                 # 参考答案（与 exercises 同结构）
├── templates/                 # 原始练习，用于 ./clings reset
├── include/clings/test.h      # 自带测试框架
├── tools/
│   ├── generate_exercises.py  # 从规格生成练习/答案/模板/文档
│   ├── spec.py                # 练习规格数据结构
│   ├── specs_00_04.py         # 前五章练习规格
│   ├── specs_05_08.py         # 中间四章练习规格
│   ├── specs_09_12.py         # 后四章练习规格
│   ├── specs_c_primer_existing.py # C Primer Plus 缺口（现有主题）
│   ├── specs_c_primer_new.py  # C Primer Plus 缺口（新主题）
│   ├── pdf_to_markdown.py     # PDF -> Markdown 转换器
│   └── prepare_ref_books.py   # PV-Books C 书籍下载/转换器
├── docs/
│   ├── architecture.md        # 运行器、生成器、测试框架设计
│   ├── curriculum.md          # 按主题列出全部练习
│   ├── knowledge-map.md       # 按 C 知识领域列出覆盖范围
│   ├── book-coverage.md       # 《C 语言深度解剖》章节到练习的映射
│   ├── reading-notes.md       # 20 本 C 参考书的阅读笔记
│   ├── gap-analysis.md        # 尚未加入的知识点与优先级路线图
│   ├── c-primer-plus-coverage.md # C Primer Plus 逐章覆盖核对
│   ├── c-traps-and-pitfalls-coverage.md # C 陷阱与缺陷 OCR 后逐节核对
│   └── reference/             # PDF 转换后的参考书
├── .ref/                      # 本地参考书库（已 gitignore）
│   ├── PV-Books/              # PaleVerge/PV-Books 完整克隆
│   ├── books/                 # 筛选出的 C 书籍
│   ├── markdown/              # C 书籍的 Markdown 转换
│   ├── cpplings/              # 参考仓库
│   ├── cplings/               # 参考仓库
│   ├── OCR-REQUIRED.md        # 扫描版 PDF 的 OCR 待办
│   └── books-manifest.json    # 下载/转换清单
├── CMakeLists.txt
├── CMakePresets.json
├── Makefile
└── Dockerfile
```

## 构建方式

### 方式一：CLI + 按需编译（推荐）

`./clings` 会在需要时用系统编译器编译单个练习，构建产物放在
`build/clings/`。这种方式适合日常学习。

```sh
./clings doctor
./clings verify
```

### 方式二：Makefile

```sh
make verify
make selftest
make check-generated
```

### 方式三：CMake + CTest

```sh
cmake --preset default
cmake --build --preset default
ctest --preset default
```

CMake 默认只构建 `solutions/` 中的答案，并把它们注册为 CTest 测试。
初始练习使用 `EXCLUDE_FROM_ALL`，避免故意编译失败的练习阻塞整个构建。
要单独构建某个练习：

```sh
cmake --build build/cmake --target exercise_01_types_variables_01_integer_types
```

### 方式四：Docker

```sh
docker build -t clings .
docker run --rm -it -v "$PWD:/clings" clings ./clings list
```

## 编译器与运行时

默认编译参数：

```text
-std=c17 -Wall -Wextra -Wpedantic -Werror -Wshadow
-Wstrict-prototypes -Wpointer-arith -Wformat=2 -Wundef
-D_POSIX_C_SOURCE=200809L -D_DEFAULT_SOURCE -g -O0
```

可以通过环境变量覆盖：

```sh
CC=clang ./clings verify
CFLAGS="-fsanitize=address,undefined" ./clings run 06_pointers/03_pointer_arithmetic
```

如果安装了 `valgrind`、`clang-tidy` 或 `cppcheck`，建议对内存和指针主题
额外运行：

```sh
valgrind ./build/clings/07_dynamic_memory/01_malloc_free.exercise
clang-tidy exercises/07_dynamic_memory/01_malloc_free.c -- -std=c17 -Iinclude
```

## 添加新练习

练习由 `tools/specs_*.py` 中的规格生成。每个规格包含正确代码、测试代码
和一组“正确片段 -> 初始片段”的替换。这样练习和答案不会不同步。

```sh
# 编辑 tools/specs_*.py
python3 tools/generate_exercises.py
./clings verify
./clings selftest
python3 tools/generate_exercises.py --check
```

详见 [CONTRIBUTING.md](CONTRIBUTING.md) 和
[docs/architecture.md](docs/architecture.md)。

## 参考与致谢

- [nooneknowspeter/cpplings](https://github.com/nooneknowspeter/cpplings)
- [rdjondo/cplings](https://github.com/rdjondo/cplings)
- [rustlings](https://github.com/rust-lang/rustlings)
- 《C 语言深度解剖》，陈正冲 编著
- C17 标准（ISO/IEC 9899:2018）

## 参考书库与缺口分析

`.ref` 目录保存了本地参考书库：

- `.ref/PV-Books`：PV-Books 的完整克隆；
- `.ref/books`：筛选出的 C 书籍，已排除 C++；
- `.ref/markdown`：这些书的 Markdown 转换；
- `.ref/cpplings`、`.ref/cplings`：两个参考练习仓库；
- `.ref/OCR-REQUIRED.md`：扫描版 PDF 的 OCR 清单。

阅读笔记见 [docs/reading-notes.md](docs/reading-notes.md)，尚未加入课程的
知识点与建议优先级见 [docs/gap-analysis.md](docs/gap-analysis.md)。

## 许可

项目代码使用 MIT License，见 [LICENSE](LICENSE)。
《C 语言深度解剖》PDF 及其 Markdown 转换件遵循原书版权声明，
不因本项目而改变许可。
