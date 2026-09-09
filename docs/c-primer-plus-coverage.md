# 《C Primer Plus》第 6 版覆盖核对

本文件记录本轮为《C Primer Plus》缺口新增的练习。核对基于
`.ref/markdown/C/C Primer Plus 第6版 中文版（史蒂芬·普拉达）.md`
和 `.ref/markdown/C/C Primer Plus.md`。

本轮新增后，项目从 102 个练习增加到 **146 个练习**，新增
`13_translation_units` 至 `19_modern_c_library` 七个主题。

## 逐章覆盖

| 章 | 主题 | 状态 | 对应练习 | 说明 |
| --- | --- | --- | --- | --- |
| 1 | 初识 C、编译链接机制 | 已补 | `00_getting_started/02`、`13_translation_units/01`-`03` | 头文件/源文件、`extern`、`static` 内部链接、多文件编译 |
| 2 | C 程序结构、调试 | 已覆盖 | `00_getting_started/01`、`04`、`06`、`04_functions/01` | 基础结构、断言、编译诊断 |
| 3 | 数据和类型 | 已补 | `01_types_variables/*`、`01_types_variables/09_long_double`、`10_stdlib_io/11`、`12_advanced_c/10` | `long double`、定宽整数、复数、类型转换 |
| 4 | 字符串和格式化 I/O | 已补 | `10_stdlib_io/13`、`10_stdlib_io/14`、`05_arrays_strings/06` | 宽度、精度、`*`、字段宽度、扫描集 |
| 5 | 运算符、表达式和语句 | 已补 | `02_operators/07`、`02_operators/*` | 复合赋值、逗号运算符、优先级、短路求值 |
| 6 | 循环 | 已补 | `03_control_flow/07`、`03_control_flow/03`-`04` | `while`、`do-while`、循环边界、嵌套循环 |
| 7 | 分支和跳转 | 已补 | `03_control_flow/01`-`06`、`14_character_io/04`、`10_stdlib_io/15` | `if/else`、`switch`、`goto`、`iso646.h`、`ctype.h` |
| 8 | 字符 I/O 和输入验证 | 已补 | `14_character_io/01`-`03` | `getc/putc`、`EOF/feof/ferror`、输入验证、菜单式校验 |
| 9 | 函数 | 已补 | `04_functions/08`、`13_translation_units/01`-`03` | 尾递归、多源文件、头文件组织 |
| 10 | 数组和指针 | 已补 | `05_arrays_strings/08`-`10` | VLA、复合字面量、指针兼容性、`const` |
| 11 | 字符串和字符串函数 | 已补 | `15_string_functions/01`-`05` | `strcat/strncat`、`strncpy`、`sprintf/snprintf`、`fgets`、字符串排序、`strtod` |
| 12 | 存储类别、链接和内存管理 | 已补 | `13_translation_units/02`-`03`、`01_types_variables/06`-`07`、`12_advanced_c/04` | 外部/内部链接、`static`、`volatile`、`restrict`、原子类型 |
| 13 | 文件输入/输出 | 已补 | `18_file_io_advanced/01`-`06` | `fprintf/fscanf`、`fgets/fputs`、`ungetc`、`fseek/ftell`、缓冲、二进制随机访问 |
| 14 | 结构和其他数据形式 | 已补 | `08_structs_unions_enums/09`-`12` | 结构体数组、按值/按指针传参、结构体文件 I/O、复杂声明 |
| 15 | 位操作 | 已补 | `16_data_representation/01`-`04` | 进制转换、整数/浮点位表示、位域与掩码 |
| 16 | C 预处理器和 C 库 | 已补 | `09_preprocessor/10`、`19_modern_c_library/01`-`03` | `#undef/defined`、`_Noreturn`、`tgmath.h`、`atexit` |
| 17 | 高级数据表示 | 已补 | `17_data_structures/01`-`03` | 队列 ADT、二叉查找树、动态数组 |
| 附录 B | 运算符、类型、C99/C11 库参考 | 部分 | 分散在各主题 | 作为参考表，不单独设练习；扩展整数类型属于 C23/实现扩展，未加入 |

## 仍然有意保留的差异

- `_Imaginary` 是 C99 的可选特性，主流编译器支持有限，未单独设练习。
- `_BitInt`、`typeof`、`nullptr` 等属于 C23 或编译器扩展，不属于《C Primer
  Plus》第 6 版的 C11 范围，暂未加入。
- 《C Primer Plus》中的平台工具链章节（Windows IDE、Macintosh、DOS）
  没有对应练习，只保留了 Linux/GCC 的可验证路径。

## 验证

```text
./clings verify    -> all 146 solutions passed
./clings selftest  -> all 146 exercises behave correctly
```

完整练习索引见 [curriculum.md](curriculum.md)，书籍阅读笔记见
[reading-notes.md](reading-notes.md)，更广泛的工程/系统缺口见
[gap-analysis.md](gap-analysis.md)。
