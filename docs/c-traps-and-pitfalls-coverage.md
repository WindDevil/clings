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
| 1.1 | `=` 不同于 `==` | 已覆盖 | `02_operators/08_assignment_vs_equality` | 区分赋值和相等比较 |
| 1.2 | `&`/`|` 不同于 `&&`/`||` | 已覆盖 | `02_operators/03_short_circuit` | 通过 `left & touch()` 的初始错误演示 |
| 1.3 | 词法分析中的“贪心法” | 已覆盖 | `02_operators/09_maximal_munch`、`00_getting_started/06_lexical_elements` | `a+++b` 的最长匹配和注释表达式 |
| 1.4 | 整型常量 | 已覆盖 | `01_types_variables/10_octal_constants`、`16_data_representation/01_base_conversion` | `010` 是八进制，`0195` 被拒绝 |
| 1.5 | 字符与字符串 | 已覆盖 | `01_types_variables/05_char_ascii`、`05_arrays_strings/04_string_literals`、`00_getting_started/06_lexical_elements` | 单引号/双引号、转义、可修改字符串 |
| 2.1 | 理解函数声明 | 已覆盖 | `04_functions/01`、`08_structs_unions_enums/12`、`06_pointers/07` | 函数指针、复杂声明、指向数组的指针 |
| 2.2 | 运算符优先级 | 已覆盖 | `02_operators/02_precedence` | 括号和优先级 |
| 2.3 | 作为语句结束标志的分号 | 已覆盖 | `03_control_flow/08_semicolon_pitfalls` | `if (...);` 空语句陷阱 |
| 2.4 | `switch` 语句 | 已覆盖 | `03_control_flow/02_switch_case` | fallthrough、default、case 值 |
| 2.5-2.6 | 悬挂 `else` 及 `else` 配对问题 | 已覆盖 | `03_control_flow/09_dangling_else`、`03_control_flow/01_if_else` | 大括号绑定 `else` 的经典陷阱 |
| 3.1 | 指针与数组 | 已覆盖 | `05_arrays_strings/02`、`06_pointers/03`、`06_pointers/07` | 数组退化、指针运算、`a` 与 `&a` |
| 3.2 | 非数组的指针 | 已覆盖 | `06_pointers/10_one_past_pointer`、`06_pointers/01`-`07` | 单对象只允许 one-past 指针运算 |
| 3.3 | 作为参数的数组声明 | 已覆盖 | `05_arrays_strings/02_array_decay` | 数组参数退化为指针 |
| 3.4 | 避免“举隅法” | 已覆盖（组合） | `05_arrays_strings/02_array_decay`、`02_operators/06_sizeof_incdec` | 用数组退化和 `sizeof` 演示“部分不能代表整体” |
| 3.5 | 空指针并非空字符串 | 已覆盖 | `06_pointers/08_null_empty_string`、`06_pointers/02_null_and_const` | 区分 `NULL`、`""` 和 `'\0'` |
| 3.6 | 边界计算与不对称边界 | 已覆盖 | `05_arrays_strings/11_asymmetric_bounds`、`07_dynamic_memory/05_buffer_bounds` | 半开区间 `[low, high)` |
| 3.7 | 求值顺序 | 已覆盖 | `11_ub_safety/05_sequence_points` | 序列点和未定义求值顺序 |
| 3.8 | 运算符 `&&`、`||` 和 `!` | 已覆盖 | `02_operators/03_short_circuit` | 短路求值 |
| 3.9 | 整数溢出 | 已覆盖 | `01_types_variables/03_overflow`、`11_ub_safety/01_signed_overflow` | 无符号回绕和有符号溢出检查 |
| 3.10 | 为 `main` 提供返回值 | 已覆盖 | `00_getting_started/07_main_return_value` | `EXIT_SUCCESS`/`EXIT_FAILURE` |
| 4.1 | 什么是连接器 | 已覆盖 | `13_translation_units/01`-`03` | 多文件编译和链接 |
| 4.2 | 声明与定义 | 已覆盖 | `13_translation_units/02_extern_linkage`、`04_functions/01` | extern 声明和定义 |
| 4.3 | 命名冲突与 `static` 修饰符 | 已覆盖 | `13_translation_units/03_static_internal_linkage`、`04_functions/05` | 内部链接和文件作用域 |
| 4.4 | 形参、实参与返回值 | 已覆盖 | `04_functions/02`、`08_structs_unions_enums/10` | 参数传递、返回值和结构体传参 |
| 4.5 | 检查外部类型 | 已覆盖 | `13_translation_units/04_external_type_check` | 声明类型与定义类型不一致 |
| 4.6 | 头文件 | 已覆盖 | `13_translation_units/01_header_source_split`、`09_preprocessor/05_include_guards` | 头文件、包含保护 |
| 5.1 | 返回整数的 `getchar` 函数 | 已覆盖 | `14_character_io/05_getchar_putchar`、`14_character_io/01_getc_putc` | `getchar`/`putchar` 和 EOF |
| 5.2 | 更新顺序文件 | 已覆盖 | `18_file_io_advanced/01`、`18_file_io_advanced/04`、`18_file_io_advanced/06` | `fprintf/fscanf`、`fseek/ftell`、二进制随机访问 |
| 5.3 | 缓冲输出与内存分配 | 已覆盖 | `18_file_io_advanced/07_buffered_output_memory`、`18_file_io_advanced/05` | `malloc` + `setvbuf` + 输出 + 释放 |
| 5.4 | 使用 `errno` 检测错误 | 已覆盖 | `10_stdlib_io/03_strtol_errno`、`18_file_io_advanced/*` | errno、文件错误和输入校验 |
| 5.5 | 库函数 `signal` | 已覆盖 | `12_advanced_c/11_signal` | signal、raise、`sig_atomic_t` |
| 6.1 | 不能忽视宏定义中的空格 | 已覆盖 | `09_preprocessor/11_macro_whitespace` | 空格把函数宏变成对象宏 |
| 6.2 | 宏并不是函数 | 已覆盖 | `09_preprocessor/02_function_macro` | 参数括号和展开陷阱 |
| 6.3 | 宏并不是语句 | 已覆盖 | `09_preprocessor/12_macro_statement` | `do { ... } while (0)` |
| 6.4 | 宏并不是类型定义 | 已覆盖 | `09_preprocessor/13_macro_not_typedef` | `typedef` 与对象宏的区别 |
| 7.1 | 应对 C 语言标准变更 | 已覆盖 | `00_getting_started/08_standard_changes` | `__STDC_VERSION__` 和 C11 检测 |
| 7.2 | 标识符名称的限制 | 已覆盖 | `00_getting_started/09_identifier_length` | 长内部标识符 |
| 7.3 | 整数的大小 | 已覆盖 | `01_types_variables/01_integer_types`、`10_stdlib_io/11_stdint_inttypes` | 类型大小、范围和定宽整数 |
| 7.4 | 字符是有符号还是无符号 | 已覆盖 | `01_types_variables/11_char_signedness` | `signed char` 与 `unsigned char` |
| 7.5 | 移位运算符 | 已覆盖 | `02_operators/05_shifts` | 移位、掩码和移位宽度 |
| 7.6 | 内存位置 0 | 已覆盖 | `06_pointers/09_memory_location_zero` | 地址 0 与 NULL |
| 7.7 | 除法运算时发生的截断 | 已覆盖 | `02_operators/01_arithmetic` | 整数除法、负数截断和取模 |
| 7.8 | 随机数的大小 | 已覆盖 | `10_stdlib_io/16_rand_max`、`10_stdlib_io/07_random` | `RAND_MAX >= 32767` |
| 7.9 | 大小写转换 | 已覆盖 | `10_stdlib_io/15_ctype_full`、`01_types_variables/05_char_ascii` | ctype 和 ASCII 大小写转换 |
| 7.10 | 首先释放，然后重新分配 | 已覆盖 | `07_dynamic_memory/08_free_then_realloc` | 不要先 free 再 realloc |
| 7.11 | 可移植性问题的一个例子 | 已覆盖（组合） | `00_getting_started/08`、`01_types_variables/11`、`06_pointers/09`、`10_stdlib_io/16` | 由多个可移植性练习组合覆盖 |
| 8.1 | 建议 | 已覆盖 | `docs/architecture.md`、`CONTRIBUTING.md`、代码风格 | 工程建议以文档形式覆盖 |
| 8.2 | 答案 | 不适用 | 书中练习题答案 | 不是课程练习 |

## 结论

《C 陷阱与缺陷》中原来标为“部分覆盖”和“未覆盖”的条目已经全部补入
现有主题，没有单独建立书籍主题。练习通过 `reference` 字段和本文件保留
与书本章节的映射。

验证结果：

```text
./clings verify    -> all 167 solutions passed
./clings selftest  -> all 167 exercises behave correctly
```
