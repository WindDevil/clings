# 《C 陷阱与缺陷》覆盖核对

《C 陷阱与缺陷》原 PDF 是扫描版，本轮已用 Tesseract
`chi_sim+eng` 完成 178 页 OCR：

- 原始 PDF：`.ref/books/C/C陷阱与缺陷.pdf`
- OCR 文本：`.ref/ocr/C/C陷阱与缺陷.txt`
- OCR 后 Markdown：`.ref/markdown/C/C陷阱与缺陷.md`
- 提取字符数：约 137,825

OCR 可能误识别个别字符、代码和标点；下面的章节结构和覆盖判断已按
OCR 文本逐节核对，但代码片段如需精确引用仍应回看 PDF。

## 逐章覆盖

| 章节 | 书中的主题 | 状态 | 现有练习 | 说明 |
| --- | --- | --- | --- | --- |
| 1.1 | `=` 不同于 `==` | 未覆盖 | 无 | 需要专门练习区分赋值与相等比较 |
| 1.2 | `&`/`|` 不同于 `&&`/`||` | 已覆盖 | `02_operators/03_short_circuit` | 通过 `left & touch()` 的初始错误演示 |
| 1.3 | 词法分析中的“贪心法” | 部分覆盖 | `00_getting_started/06_lexical_elements` | 覆盖转义和续行，但未覆盖 `a+++b`、`/*`、`=+` 等最长匹配问题 |
| 1.4 | 整型常量 | 部分覆盖 | `01_types_variables/01_integer_types`、`16_data_representation/01_base_conversion` | 覆盖类型范围和进制解析，未覆盖 `010` 是八进制、`0195` 等陷阱 |
| 1.5 | 字符与字符串 | 已覆盖 | `01_types_variables/05_char_ascii`、`05_arrays_strings/04_string_literals`、`00_getting_started/06_lexical_elements` | 单引号/双引号、转义、可修改字符串 |
| 2.1 | 理解函数声明 | 已覆盖 | `04_functions/01`、`08_structs_unions_enums/12`、`06_pointers/07` | 函数指针、复杂声明、指向数组的指针 |
| 2.2 | 运算符优先级 | 已覆盖 | `02_operators/02_precedence` | 括号和优先级 |
| 2.3 | 作为语句结束标志的分号 | 未覆盖 | 无 | 需要专门练习多余/缺失分号和空语句 |
| 2.4 | `switch` 语句 | 已覆盖 | `03_control_flow/02_switch_case` | fallthrough、default、case 值 |
| 2.5-2.6 | 悬挂 `else` 及 `else` 配对问题 | 部分覆盖 | `03_control_flow/01_if_else` | 覆盖 if/else 基础，未覆盖大括号与悬挂 else 的经典陷阱 |
| 3.1 | 指针与数组 | 已覆盖 | `05_arrays_strings/02`、`06_pointers/03`、`06_pointers/07` | 数组退化、指针运算、`a` 与 `&a` |
| 3.2 | 非数组的指针 | 部分覆盖 | `06_pointers/01`-`07` | 指针基础完整，但未专门练习对非数组对象做指针运算的语义 |
| 3.3 | 作为参数的数组声明 | 已覆盖 | `05_arrays_strings/02_array_decay` | 数组参数退化为指针 |
| 3.4 | 避免“举隅法” | 部分覆盖 | `05_arrays_strings/02`、`02_operators/06` | 覆盖 `sizeof` 和数组参数，但未系统讨论“部分代表整体”的错误推理 |
| 3.5 | 空指针并非空字符串 | 部分覆盖 | `06_pointers/02_null_and_const`、`11_ub_safety/08_null_pointer` | 覆盖 NULL 检查，未区分 `NULL`、`""` 和 `'\0'` 的语义 |
| 3.6 | 边界计算与不对称边界 | 部分覆盖 | `07_dynamic_memory/05_buffer_bounds`、`11_ub_safety/03_out_of_bounds` | 覆盖边界检查，未专门练习半开区间 `[low, high)` |
| 3.7 | 求值顺序 | 已覆盖 | `11_ub_safety/05_sequence_points` | 序列点和未定义求值顺序 |
| 3.8 | 运算符 `&&`、`||` 和 `!` | 已覆盖 | `02_operators/03_short_circuit` | 短路求值 |
| 3.9 | 整数溢出 | 已覆盖 | `01_types_variables/03_overflow`、`11_ub_safety/01_signed_overflow` | 无符号回绕和有符号溢出检查 |
| 3.10 | 为 `main` 提供返回值 | 未覆盖 | 无 | 需要专门练习 `return`/`exit` 状态码和 `EXIT_SUCCESS` |
| 4.1 | 什么是连接器 | 已覆盖 | `13_translation_units/01`-`03` | 多文件编译和链接 |
| 4.2 | 声明与定义 | 已覆盖 | `13_translation_units/02_extern_linkage`、`04_functions/01` | extern 声明和定义 |
| 4.3 | 命名冲突与 `static` 修饰符 | 已覆盖 | `13_translation_units/03_static_internal_linkage`、`04_functions/05` | 内部链接和文件作用域 |
| 4.4 | 形参、实参与返回值 | 已覆盖 | `04_functions/02`、`08_structs_unions_enums/10` | 参数传递、返回值和结构体传参 |
| 4.5 | 检查外部类型 | 部分覆盖 | `13_translation_units/02_extern_linkage` | 覆盖 extern，但未覆盖跨文件类型不一致的诊断 |
| 4.6 | 头文件 | 已覆盖 | `13_translation_units/01_header_source_split`、`09_preprocessor/05_include_guards` | 头文件、包含保护 |
| 5.1 | 返回整数的 `getchar` 函数 | 部分覆盖 | `14_character_io/01_getc_putc`、`14_character_io/02_eof_ferror` | 使用 `getc` 覆盖同类语义，未专门使用 `getchar` |
| 5.2 | 更新顺序文件 | 已覆盖 | `18_file_io_advanced/01`、`18_file_io_advanced/04`、`18_file_io_advanced/06` | `fprintf/fscanf`、`fseek/ftell`、二进制随机访问 |
| 5.3 | 缓冲输出与内存分配 | 部分覆盖 | `18_file_io_advanced/05`、`07_dynamic_memory/*` | 分别覆盖缓冲和分配，未把两者组合成输出缓冲案例 |
| 5.4 | 使用 `errno` 检测错误 | 已覆盖 | `10_stdlib_io/03_strtol_errno`、`18_file_io_advanced/*` | errno、文件错误和输入校验 |
| 5.5 | 库函数 `signal` | 已覆盖 | `12_advanced_c/11_signal` | signal、raise、`sig_atomic_t` |
| 6.1 | 不能忽视宏定义中的空格 | 部分覆盖 | `09_preprocessor/01`-`02` | 覆盖宏定义，未专门演示空格改变宏名或参数 |
| 6.2 | 宏并不是函数 | 已覆盖 | `09_preprocessor/02_function_macro` | 参数括号和展开陷阱 |
| 6.3 | 宏并不是语句 | 未覆盖 | 无 | 需要练习 `do { ... } while (0)` 和语句宏陷阱 |
| 6.4 | 宏并不是类型定义 | 未覆盖 | 无 | 需要专门对比 `#define` 与 `typedef` |
| 7.1 | 应对 C 语言标准变更 | 部分覆盖 | `00_getting_started/02_compilation_model` | 覆盖 `__STDC_VERSION__`，未覆盖标准变更案例 |
| 7.2 | 标识符名称的限制 | 未覆盖 | 无 | 属于低优先级可移植性细节 |
| 7.3 | 整数的大小 | 已覆盖 | `01_types_variables/01_integer_types`、`10_stdlib_io/11_stdint_inttypes` | 类型大小、范围和定宽整数 |
| 7.4 | 字符是有符号还是无符号 | 部分覆盖 | `01_types_variables/02`、`01_types_variables/05` | 覆盖 char 和符号，未专门讨论 `char` 的实现定义符号性 |
| 7.5 | 移位运算符 | 已覆盖 | `02_operators/05_shifts` | 移位、掩码和移位宽度 |
| 7.6 | 内存位置 0 | 部分覆盖 | `06_pointers/02`、`11_ub_safety/08_null_pointer` | 覆盖 NULL 检查，未讨论地址 0 和空指针表示的可移植性 |
| 7.7 | 除法运算时发生的截断 | 已覆盖 | `02_operators/01_arithmetic` | 整数除法、负数截断和取模 |
| 7.8 | 随机数的大小 | 部分覆盖 | `10_stdlib_io/07_random` | 覆盖 rand 和边界，未讨论 `RAND_MAX` 的可移植性 |
| 7.9 | 大小写转换 | 已覆盖 | `10_stdlib_io/15_ctype_full`、`01_types_variables/05_char_ascii` | ctype 和 ASCII 大小写转换 |
| 7.10 | 首先释放，然后重新分配 | 部分覆盖 | `07_dynamic_memory/03_realloc` | 覆盖 realloc，未覆盖 free 后再 realloc 的经典错误 |
| 7.11 | 可移植性问题的一个例子 | 部分覆盖 | 分散在 `11_ub_safety`、`16_data_representation` | 没有专门的综合可移植性练习 |
| 8.1 | 建议 | 已覆盖 | `docs/architecture.md`、`CONTRIBUTING.md`、代码风格 | 工程建议以文档形式覆盖 |
| 8.2 | 答案 | 不适用 | 书中练习题答案 | 不是课程练习 |

## 精确缺口清单

如果只针对《C 陷阱与缺陷》，目前还缺以下专门练习：

1. `=` 与 `==` 的混淆。
2. 词法分析的最长匹配/贪心法：`a+++b`、`/*`、`=+` 等。
3. 八进制整型常量：`010`、`0195`。
4. 分号、空语句和多写分号。
5. 悬挂 `else` 与大括号。
6. `NULL`、`""`、`'\0'` 的区别。
7. 不对称边界 `[low, high)`。
8. `main` 返回值与进程退出状态。
9. 跨翻译单元的外部类型检查。
10. 宏定义空格、宏作为语句、宏不是类型定义。
11. `char` 的符号性、地址 0、`RAND_MAX` 等可移植性细节。
12. `free` 后再 `realloc` 的经典错误。

这些是精确到书内小节的缺口；本轮只做 OCR 和核对，没有把上述练习加入
项目。
