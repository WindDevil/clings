# 参考书阅读后的覆盖缺口分析

> 《C Primer Plus》本身的缺口已经在后续提交中补齐，逐章结果见
> [c-primer-plus-coverage.md](c-primer-plus-coverage.md)。本文件保留的是
> 超出《C Primer Plus》范围、面向真实 C 工程和系统编程的更大缺口。
> 多翻译单元、标准库深度、字符串/文件 I/O、基础数据结构和现代 C 库
> 已部分覆盖；剩余重点主要是分配器、POSIX 系统编程、安全/UB、链接/构建
> 工具链、调试测试和并发网络。
>
> 《C 陷阱与缺陷》中原来标为部分覆盖/未覆盖的条目也已拆回现有主题，
> 逐节结果见 [c-traps-and-pitfalls-coverage.md](c-traps-and-pitfalls-coverage.md)。

## 1. `.ref` 中的参考材料

已把 PV-Books 克隆到 `.ref/PV-Books`，并把筛选出的 C 书籍下载到
`.ref/books`、转换成 Markdown 到 `.ref/markdown`。两个参考仓库位于
`.ref/cpplings` 和 `.ref/cplings`。

本次筛选排除了 `C++/` 目录和所有 C++ 标题的书籍，包括
`Essential C++`。C 相关书籍分为四组：

| 分组 | 书籍 |
| --- | --- |
| C 语言核心 | 《C 程序设计语言（第 2 版）》《C Primer Plus》《C 陷阱与缺陷》《C 语言接口与实现》《C 专家编程》《狂人 C 程序员入门必备》《C 语言深度解剖》 |
| C 算法与数据结构 | 《数据结构与算法分析：C 语言描述》《C 语言程序 190 例》《C 语言趣味程序设计编程百例精解》《C 语言算法 100 例》 |
| C 系统编程 / POSIX | 《UNIX 环境高级编程》《UNIX 网络编程卷 1/2》《UNIX 编程艺术》《深入理解计算机系统》《程序员的自我修养：链接、装载与库》 |
| C 工程实践 | 《程序设计实践》《跟我一起写 Makefile》 |

筛选原则：保留 C 语言核心、C 算法/数据结构、C/POSIX 系统编程和 C 工程
实践书籍；排除 `C++/` 目录、`Essential C++`，以及 Java、Python、Go、
前端等与 C 无关的书籍。Linux 内核、操作系统和“C/C++ 混用”的算法书
（例如《编程珠玑》《算法竞赛入门经典》《剑指 Offer》）暂未纳入，如果
希望把“系统 C”扩展到内核/OS 层面，可以再加入。

完整清单和转换状态见：

- `.ref/books-manifest.json`
- `.ref/README.md`
- `.ref/OCR-REQUIRED.md`

### 转换质量

有文本层的 PDF、EPUB、DOC 已经成功转成 Markdown。以下 8 本仍是扫描版，
`pdftotext` 只能提取到很少文字，Markdown 中已加入 `OCR required` 警告：

| 书籍 | 页数 | 提取字符数 |
| --- | ---: | ---: |
| C 语言接口与实现 | 399 | 5,172 |
| C 专家编程 | 307 | 1,840 |
| 数据结构与算法分析：C 语言描述 | 406 | 2,434 |
| UNIX 环境高级编程 | 822 | 4,930 |
| UNIX 网络编程卷 1 | 874 | 5,242 |
| UNIX 网络编程卷 2 | 476 | 5,985 |
| UNIX 编程艺术 | 544 | 12,196 |
| 程序员的自我修养：链接、装载与库 | 485 | 14,915 |

《C 陷阱与缺陷》已经用 Tesseract `chi_sim+eng` 完成 OCR，Markdown 中
现有约 137,825 个字符，逐节覆盖见
[c-traps-and-pitfalls-coverage.md](c-traps-and-pitfalls-coverage.md)。

这些书的主题仍然可以从书名、目录结构和 C 领域的标准知识中分析，但要做
全文检索，需要安装 `ocrmypdf`/Tesseract 后重新转换：

```sh
ocrmypdf --skip-text -l chi_sim+eng input.pdf output.pdf
python3 tools/prepare_ref_books.py --skip-download
```

## 2. 当前项目已经覆盖什么

当前 `clings` 有 102 个练习，覆盖：

- 程序结构、编译流程、`argc/argv`、断言和编译器诊断；
- 整数、浮点、符号、溢出、字符、存储类、作用域、`const`、`volatile`、
  `restrict`、`extern`、`auto`、`register`；
- 算术、优先级、短路求值、位运算、移位、`sizeof`、自增自减；
- `if`、`switch`、循环、`break/continue`、`goto`、状态机；
- 函数、递归、`static`、函数指针、变参函数、`void/return`；
- 数组、数组退化、多维数组、字符串、`snprintf`、`strtok_r`；
- 指针、`NULL`、指针运算、二级指针、`void *`、野指针、指向数组的指针；
- `malloc/calloc/realloc/free`、泄漏、越界、柔性数组、链表；
- 结构体、嵌套结构体、对齐、位域、联合、枚举、`typedef`、`container_of`；
- 宏、`#`/`##`、条件编译、头文件保护、X-macro、`#error/#line/#pragma`、
  预定义宏；
- `printf/scanf`、`strtol`、`qsort/bsearch`、`math.h`、`time.h`、随机数、
  文件 I/O、`mem*`、字符串搜索、定宽整数、环境变量；
- 有符号溢出、未初始化、越界、释放后使用、序列点、严格别名、对齐、
  空指针；
- 变参函数、`setjmp/longjmp`、POSIX 线程、C11 原子、`_Generic`、
  `_Static_assert`、`alignof/alignas`、匿名联合、`_Thread_local`、
  复数、信号。

这些内容大致对应 K&R、C Primer Plus、C 语言深度解剖和 CSAPP 前半部分的
语言基础。**缺口不在“更多语法”，而在真实 C 项目需要的多文件组织、系统
API、分配器、数据结构、链接/构建、安全与工程化。**

## 3. 仍然缺失的内容

### 3.1 多翻译单元、链接和程序组织

当前练习都是单文件程序。`extern` 只在同一个翻译单元里演示，`static` 也
只演示文件内函数，尚未真正跨文件链接。

缺失主题：

- 头文件与源文件分离；
- 跨翻译单元的 `extern` 声明和定义；
- `static` 的内部链接与外部链接；
- `inline`、`static inline`、`extern inline` 的链接语义；
- 临时定义（tentative definition）、重复定义和链接错误；
- 头文件保护、`#pragma once`、前置声明、不透明类型；
- 静态库、共享库、符号可见性；
- `_Noreturn`、`restrict`/`volatile` 在 API 边界上的语义；
- ABI、调用约定、参数传递和返回值约定。

来源：K&R 第 4 章、C Primer Plus 第 12 章、Expert C Programming、
《程序员的自我修养》、CSAPP 第 7 章。

建议新主题：`13_translation_units`。

### 3.2 标准库深度

当前覆盖的是标准库的入门用法，以下内容尚未系统练习：

- `stdio.h`：缓冲、`setvbuf`、`fflush`、`ferror`、`feof`、`clearerr`、
  `ungetc`、`getline`、`tmpfile`、`freopen`、`popen`、`fmemopen`；
- `stdlib.h`：`atexit`、`exit`、`_Exit`、`abort`、`system`、`div`、
  `abs`、`strtod`、`strtoul`、`aligned_alloc`、`posix_memalign`；
- `string.h`：`strncpy`/`strncat` 的陷阱、`strspn`、`strcspn`、
  `strpbrk`、`strerror`、`memchr`；
- `time.h`：`mktime`、`localtime`、`strftime`、`clock`、`timespec`；
- `math.h`：`isnan`、`isinf`、`fpclassify`、`signbit`、`nextafter`、
  `fma`、`remainder`、NaN/Inf 处理；
- `locale.h`、`wchar.h`、`wctype.h`：locale、宽字符、多字节转换；
- `fenv.h`：浮点舍入模式和浮点异常。

来源：K&R 第 7/8 章和附录 B、C Primer Plus 第 4/8/11/13/16 章、
Expert C Programming、APUE。

建议新主题：`14_stdlib_depth`。

### 3.3 POSIX / Unix 系统编程

当前只有 `pthread` 计数器和 `signal` 两个系统编程练习。真实 C 项目大量
使用文件描述符、进程、IPC 和套接字。

缺失主题：

- 文件描述符：`open`、`read`、`write`、`close`、`lseek`；
- 文件元数据：`stat`、`fstat`、`access`、`chmod`；
- 目录：`opendir`、`readdir`、`closedir`、`getcwd`、`chdir`；
- 进程：`fork`、`exec`、`wait`、`waitpid`、僵尸进程；
- IPC：`pipe`、`dup2`、FIFO、共享内存、信号量；
- 信号：`sigaction`、信号掩码、异步信号安全函数；
- I/O 多路复用：`select`、`poll`、`epoll`；
- 内存映射：`mmap`、`munmap`、`msync`；
- 动态加载：`dlopen`、`dlsym`、`dlerror`；
- 套接字：TCP/UDP、`socket`、`bind`、`listen`、`accept`、`connect`、
  `send`、`recv`；
- `errno`、`strerror`、`perror` 的线程安全和错误处理；
- `getopt`/`getopt_long` 命令行解析。

来源：APUE、UNP 卷 1/2、CSAPP 第 8/10/11/12 章、《UNIX 编程艺术》。

建议新主题：`17_posix_system`。

### 3.4 内存、分配器和对象生命周期

当前只覆盖了 `malloc` 家族的基本用法。以下内容缺失：

- `aligned_alloc`、`posix_memalign`、`alloca`；
- arena、pool、slab、free-list 分配器；
- 自定义 `malloc`/`free` 的元数据和边界检查；
- 内存碎片、对齐、容量增长策略；
- `mmap`、`sbrk` 和虚拟内存；
- 所有权模型、借用/生命周期（用 C 的方式表达）；
- 双重释放检测、释放后使用检测；
- 对象生命周期、有效类型（effective type）、指针来源（pointer provenance）；
- `restrict` 的别名承诺和违反后果；
- `memcpy`/`memmove` 的重叠区域语义。

来源：《C 语言接口与实现》、Expert C Programming、CSAPP 第 9 章、
《程序员的自我修养》。

建议新主题：`15_allocators`。

### 3.5 C 语言数据结构与算法

当前只有链表。以下内容缺失：

- 动态数组/vector；
- 栈、队列、双端队列、环形缓冲区；
- 哈希表、集合、字典；
- 二叉搜索树、平衡树、堆/优先队列；
- Trie、图、并查集、LRU 缓存；
- 位集合、字符串驻留、通用容器；
- 复杂度分析、性能测量和内存布局。

来源：《数据结构与算法分析：C 语言描述》《C 语言接口与实现》、
《程序设计实践》第 2/3 章、狂人 C、C 语言算法 100 例。

建议新主题：`16_data_structures`。

### 3.6 未定义行为、安全和可移植性

当前覆盖了基础 UB，以下内容缺失：

- 有效类型和严格别名；
- 指针来源、指针比较和对象生命周期；
- 数据竞争、原子操作的内存序（`memory_order_*`）；
- 整数提升、隐式转换、截断和符号扩展；
- 移位、除零、`INT_MIN / -1` 等边界；
- 未对齐访问、`#pragma pack` 的可移植性；
- 字节序、二进制序列化、网络字节序；
- `CHAR_BIT`、整数宽度、二补码假设；
- 格式字符串漏洞、缓冲区溢出、整数溢出；
- TOCTOU、权限和文件安全问题；
- `-D_FORTIFY_SOURCE`、stack protector、ASan/UBSan/TSan/MSan。

来源：《C 陷阱与缺陷》、Expert C Programming、CSAPP 第 2/3 章、
C Primer Plus 第 15 章、《程序设计实践》第 8 章。

建议新主题：`18_security_ub`。

### 3.7 工具链、链接、装载和构建系统

当前项目有 Makefile/CMake 文件，但没有练习教学习者如何写它们，也没有
对象文件、符号表、静态库/共享库、动态链接的练习。

缺失主题：

- 预处理、编译、汇编、链接的完整流程；
- 目标文件、符号、重定位；
- 静态库、共享库、PIC；
- ELF 结构、`nm`、`objdump`、`readelf`、`ldd`、`ar`、`ranlib`；
- `dlopen`/`dlsym` 动态加载；
- Makefile：变量、规则、模式规则、隐含规则、函数、依赖；
- CMake：target、library、install、测试、工具链文件；
- 交叉编译、`pkg-config`、Autotools、Meson、Bazel；
- 编译选项、`-I`、`-L`、`-l`、`-Wl`、`-fPIC`、`-shared`。

来源：《程序员的自我修养》、CSAPP 第 7 章、《跟我一起写 Makefile》、
C Primer Plus 第 1 章。

建议新主题：`19_toolchain_build`。

### 3.8 调试、测试、性能和静态分析

当前有自带的 `clings verify/selftest`，但还没有把调试和性能工具作为
练习内容：

- GDB：断点、观察点、调用栈、core dump、条件断点；
- Valgrind：memcheck、callgrind、helgrind；
- Sanitizer：ASan、UBSan、TSan、MSan；
- 覆盖率：gcov、lcov；
- 模糊测试：libFuzzer、AFL；
- 单元测试框架：Unity、CMocka、Check；
- 静态分析：clang-tidy、cppcheck、scan-build；
- 性能：`perf`、`gprof`、缓存、分支预测、向量化；
- 编译器优化：`-O2`、`inline`、`restrict`、LTO。

来源：《程序设计实践》第 5/6/7 章、CSAPP 第 5/9 章、Expert C
Programming。

建议新主题：`19_toolchain_build` 或独立的 `20_debug_perf`。

### 3.9 并发、网络和系统

当前有 `pthread`、`atomic_int`、`_Thread_local` 和 `signal` 的基础
练习，以下内容缺失：

- 条件变量、读写锁、屏障、线程池；
- 线程取消、线程安全、可重入函数；
- `memory_order_relaxed/acquire/release/seq_cst`；
- 无锁队列、无锁栈、CAS；
- 数据竞争检测（TSan）；
- `select`/`poll`/`epoll`、非阻塞 I/O；
- TCP/UDP 套接字、网络字节序、协议解析；
- `sigaction`、信号掩码、异步信号安全；
- 定时器、实时调度、`clock_nanosleep`。

来源：APUE、UNP、CSAPP 第 12 章、C 标准 `threads.h`/`stdatomic.h`。

建议在 `17_posix_system` 和 `18_security_ub` 中分阶段加入。

### 3.10 国际化、编码和文本处理

当前只有 ASCII/`char` 基础和 UTF-8 提及，以下内容缺失：

- UTF-8 校验、编码、解码；
- `wchar_t`、`mbstowcs`、`wcstombs`、`mbrtowc`、`wcrtomb`；
- `iconv`、Unicode 规范化；
- `locale`、排序、数字/日期格式；
- C23 的 `char8_t`/`u8` 字符串相关变化；
- 文本文件的行尾、BOM、编码检测。

来源：C Primer Plus 第 4/8/16 章、《程序设计实践》第 8.8 节、
C 标准库资料。

建议在 `14_stdlib_depth` 中增加一个子主题。

### 3.11 嵌入式 C 和编译器扩展

当前没有嵌入式 C 练习。以下内容缺失：

- `volatile` 内存映射 I/O；
- 中断服务例程（ISR）和 `sig_atomic_t`；
- 位操作、寄存器读写、位带操作；
- `__attribute__((packed/aligned/section/weak/used))`；
- `__builtin_*`、`inline asm`；
- 链接脚本、启动代码、`-nostdlib`；
- 交叉编译、工具链文件；
- 看门狗、RTOS 基础。

来源：Expert C Programming、C 语言深度解剖、CSAPP，以及嵌入式 C 资料。

建议新主题：`21_embedded_c`。

### 3.12 C 标准版本和 C23

当前以 C17 为主，覆盖了 C11 的 `_Generic`、`_Static_assert`、
`alignas/alignof`、`stdatomic.h`、`_Thread_local`。以下内容缺失：

- C89/C90、C99、C11、C17、C23 的差异；
- 特性测试宏（feature test macros）；
- C23 的 `nullptr`、`constexpr`、`typeof`/`typeof_unqual`、
  `auto` 类型推导、`bool`/`true`/`false` 关键字；
- `_BitInt`、`#embed`、`__VA_OPT__`、`#elifdef`、`#warning`；
- `char8_t`/u8 字符串相关变化（取决于编译器支持）。

来源：C Primer Plus 第 1/16 章、K&R 附录 C、C 标准。

建议在 `20_c23_extensions` 中作为可选主题。

### 3.13 工程化和 API 设计

当前练习是单文件、短函数，缺少真实项目中的接口设计：

- 头文件组织、前置声明、不透明类型；
- ADT 接口与实现分离；
- 错误码、错误处理约定、资源清理；
- 命名、注释、文档、版本和 ABI 稳定性；
- 单元测试、集成测试、CI；
- 跨平台可移植性；
- 打包、安装和分发。

来源：《C 语言接口与实现》《程序设计实践》《程序员的自我修养》、
Clean Code 相关章节。

## 4. 建议的优先级路线图

### P0：先补齐 C 语言本身的闭环

| 主题 | 建议练习 | 数量 |
| --- | --- | ---: |
| 多翻译单元与链接 | 头文件/源文件、`extern`、`static`、`inline`、静态库 | 5 |
| 标准库深度 | `stdio` 缓冲、文件错误、`atexit`、`strtod`、时间格式化、`math` 分类、locale/宽字符、边界字符串 | 8 |
| 分配器与对象生命周期 | `aligned_alloc`、`posix_memalign`、arena、pool、malloc 追踪 | 5 |
| 数据结构 | 动态数组、栈/队列、哈希表、BST、堆、图、Trie、LRU | 8 |
| 安全与 UB | 有效类型、指针来源、格式字符串、整数溢出、数据竞争、`restrict` 违规 | 6 |

P0 完成后，项目从“语言练习”升级为“能写真实 C 程序”。

### P1：系统编程和工程能力

| 主题 | 建议练习 | 数量 |
| --- | --- | ---: |
| POSIX 文件与进程 | `open/read/write`、`stat`、目录、`fork/exec/wait`、`pipe/dup2` | 6 |
| 信号与 I/O 多路复用 | `sigaction`、`select/poll/epoll`、非阻塞 I/O | 4 |
| 链接与构建 | 对象文件、静态/共享库、ELF 工具、Makefile、CMake | 6 |
| 调试与测试 | GDB、Valgrind、Sanitizer、覆盖率、模糊测试 | 5 |
| 并发进阶 | 条件变量、读写锁、屏障、线程池、内存序 | 5 |

### P2：高级和平台相关

| 主题 | 建议练习 | 数量 |
| --- | --- | ---: |
| 网络编程 | TCP/UDP、套接字、协议解析、网络字节序 | 4 |
| 国际化与编码 | UTF-8、宽字符、locale、iconv | 4 |
| 嵌入式 C | `volatile` MMIO、ISR、链接脚本、属性/内置函数 | 4 |
| C23 与编译器扩展 | `nullptr`、`constexpr`、`typeof`、`_BitInt`、`#embed`、`__VA_OPT__` | 5 |
| 性能与优化 | `perf`、缓存、向量化、LTO、`restrict` | 4 |

合计建议新增约 **70 个练习**，使总规模达到约 **170 个练习**。其中
P0 约 32 个，是下一阶段最值得先做的部分。

## 5. 对项目结构的直接影响

当前运行器只编译单个 `.c` 文件。要加入多翻译单元、静态库和系统编程
练习，需要先做三项基础改造：

1. 练习规格支持 `sources: [...]` 和 `headers: [...]`，运行器编译并链接
   同一目录下的多个源文件。
2. 练习规格支持 `ldflags`/`libs`，用于 `-pthread`、`-ldl`、`-lrt`、
   `-lm`、`-lsocket` 等平台差异。
3. 增加“项目型练习”目录，允许一个练习包含 `src/`、`include/`、
   `Makefile` 和测试文件。

完成这三项改造后，再按 P0 路线图批量添加练习，收益最大。

## 6. 结论

参考书补充后，最明显的结论是：

1. **语言基础已经比较完整**：关键字、运算符、控制流、函数、指针、数组、
   结构体、预处理器、基础标准库和基础 UB 都有覆盖。
2. **真正的缺口是“工程化 C”**：多文件、链接、构建、静态/共享库、
   POSIX API、数据结构、分配器、调试测试工具。
3. **第二层缺口是“系统级 C”**：进程、信号、IPC、套接字、并发内存模型、
   网络和嵌入式。
4. **第三层缺口是“现代 C 和平台扩展”**：C23、编译器属性、性能优化、
   国际化、Windows/嵌入式差异。

建议下一步先做 P0 的 32 个练习，并同步改造运行器支持多文件项目；
之后再按 P1/P2 扩展。
