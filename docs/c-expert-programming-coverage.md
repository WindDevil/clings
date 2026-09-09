# 《C 专家编程》覆盖核对

原 PDF 是扫描版，本轮已用 Tesseract `chi_sim+eng` 完成 307 页 OCR：

- 原始 PDF：`.ref/books/Algorithms/C专家编程.pdf`
- OCR 文本：`.ref/ocr/Algorithms/C专家编程.txt`
- OCR 后 Markdown：`.ref/markdown/Algorithms/C专家编程.md`
- 提取字符数：约 323,533

这本书的重点是 **C 语言背后的编译器、链接器、运行时、内存和 ABI
细节**，不是入门语法。原有 167 个练习覆盖了语言语法、指针、内存基础和
部分未定义行为；本轮补到 177 个练习后，主要语言/运行时缺口已经有了
对应练习。

## 逐章覆盖

| 章 | 书中的主题 | 状态 | 现有练习 | 说明 |
| --- | --- | --- | --- | --- |
| 1 | C: 穿越时空的迷雾 | 已覆盖（基础） | `00_getting_started/02_compilation_model`、`00_getting_started/08_standard_changes`、`00_getting_started/09_identifier_length`、`00_getting_started/10_implementation_defined` | 覆盖标准版本、编译模型、实现定义行为和 pragma |
| 2 | 这不是 Bug，而是语言特性 | 已覆盖（基础） | `11_ub_safety/*`、`01_types_variables/07_qualifiers`、`02_operators/*`、`01_types_variables/12_integer_promotions` | 覆盖 UB、volatile、restrict、const、位运算和整型提升 |
| 3 | 分析 C 语言的声明 | 已覆盖 | `08_structs_unions_enums/12_complex_declarations`、`08_structs_unions_enums/13_declaration_grammar`、`04_functions/06_function_pointers`、`06_pointers/07_pointer_to_array`、`09_preprocessor/13_macro_not_typedef` | 覆盖函数指针、函数指针表、复杂声明、typedef 与宏区别 |
| 4 | 数组和指针并不相同 | 已覆盖 | `05_arrays_strings/02_array_decay`、`06_pointers/03_pointer_arithmetic`、`06_pointers/07_pointer_to_array` | 数组退化、指针运算、`a` 与 `&a`、数组参数 |
| 5 | 对链接的思考 | 已覆盖（基础） | `13_translation_units/01`-`05` | 有多文件链接、extern、static、外部类型检查、动态链接；interpositioning 和链接器报告仍偏工具 |
| 6 | 运动的诗章：运行时数据结构 | 已覆盖（基础） | `12_advanced_c/02_setjmp_longjmp`、`12_advanced_c/12_stack_frame`、`16_data_representation/05_endianness`、`12_advanced_c/03_pthreads` | 覆盖 setjmp、栈帧、端序、线程、TLS；a.out/ELF 和调用约定仍偏平台 |
| 7 | 对内存的思考 | 已覆盖（基础） | `07_dynamic_memory/01`-`10`、`11_ub_safety/*` | 覆盖 malloc/free、泄漏、越界、对齐、arena、分配统计；cache 和完整 malloc 实现仍偏实现细节 |
| 8 | 为什么程序员无法分清万圣节和圣诞节 | 已覆盖 | `01_types_variables/12_integer_promotions`、`04_functions/09_default_argument_promotions`、`10_stdlib_io/17_printf_varargs` | 覆盖整型提升、默认参数提升和 varargs |
| 9 | 再论数组 | 部分覆盖 | `05_arrays_strings/03_multidimensional`、`06_pointers/07_pointer_to_array`、`02_operators/06_sizeof_incdec` | 有多维数组、数组指针、sizeof，没有更深入的数组/指针等价与下标运算细节 |
| 10 | 再论指针 | 已覆盖（基础） | `06_pointers/01`-`11`、`08_structs_unions_enums/13_declaration_grammar`、`12_advanced_c/01_variadic` | 覆盖函数指针表、restrict 契约和指针基础 |
| 11 | 你懂得 C，所以 C++ 不在话下 | 不适用 | 无 | 这是 C/C++ 差异章节，按项目约定不加入 C++ 内容 |

## 结论

现有项目现在覆盖了这本书中**偏语言层面的主要部分**：

- 数组与指针的区别；
- 多翻译单元和基础链接；
- 内存分配、泄漏、越界；
- 部分未定义行为；
- 类型提升、默认参数提升和格式化；
- 实现定义行为、栈帧、端序、动态链接、arena 和分配统计。

仍然偏工具或平台的内容包括：

1. **链接器细节**：interpositioning、符号解析、链接器报告。
2. **运行时结构**：a.out/ELF、段、调用约定、进程内存布局。
3. **内存实现**：完整 malloc 实现、cache、性能分析。
4. **平台差异**：不同 ABI、编译器和操作系统的行为差异。

本轮已把上述主要缺口加入现有主题，没有单独建立书籍主题。
