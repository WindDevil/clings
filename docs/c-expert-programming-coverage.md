# 《C 专家编程》覆盖核对

原 PDF 是扫描版，本轮已用 Tesseract `chi_sim+eng` 完成 307 页 OCR：

- 原始 PDF：`.ref/books/Algorithms/C专家编程.pdf`
- OCR 文本：`.ref/ocr/Algorithms/C专家编程.txt`
- OCR 后 Markdown：`.ref/markdown/Algorithms/C专家编程.md`
- 提取字符数：约 323,533

这本书的重点是 **C 语言背后的编译器、链接器、运行时、内存和 ABI
细节**，不是入门语法。现有 167 个练习覆盖了语言语法、指针、内存基础和
部分未定义行为，但书中的大量“实现细节”还没有对应练习。

## 逐章覆盖

| 章 | 书中的主题 | 状态 | 现有练习 | 说明 |
| --- | --- | --- | --- | --- |
| 1 | C: 穿越时空的迷雾 | 部分覆盖 | `00_getting_started/02_compilation_model`、`00_getting_started/08_standard_changes`、`00_getting_started/09_identifier_length` | 覆盖标准版本和编译模型，没有 C 历史、ANSI C 变更、实现定义行为、pragma 细节 |
| 2 | 这不是 Bug，而是语言特性 | 部分覆盖 | `11_ub_safety/*`、`01_types_variables/07_qualifiers`、`02_operators/*` | 覆盖 UB、volatile、restrict、const、位运算，没有系统讨论“语言特性 vs Bug”的案例 |
| 3 | 分析 C 语言的声明 | 部分覆盖 | `08_structs_unions_enums/12_complex_declarations`、`04_functions/06_function_pointers`、`06_pointers/07_pointer_to_array`、`09_preprocessor/13_macro_not_typedef` | 覆盖函数指针、复杂声明、typedef 与宏区别，没有完整声明语法解析练习 |
| 4 | 数组和指针并不相同 | 已覆盖 | `05_arrays_strings/02_array_decay`、`06_pointers/03_pointer_arithmetic`、`06_pointers/07_pointer_to_array` | 数组退化、指针运算、`a` 与 `&a`、数组参数 |
| 5 | 对链接的思考 | 部分覆盖 | `13_translation_units/01`-`04` | 有多文件链接、extern、static、外部类型检查，没有动态链接、interpositioning、链接器报告、符号解析细节 |
| 6 | 运动的诗章：运行时数据结构 | 部分覆盖 | `12_advanced_c/02_setjmp_longjmp`、`12_advanced_c/03_pthreads`、`12_advanced_c/09_thread_local` | 覆盖 setjmp、线程、TLS，没有 a.out/ELF、段、栈帧、活动记录、调用约定、进程内存布局 |
| 7 | 对内存的思考 | 部分覆盖 | `07_dynamic_memory/*`、`11_ub_safety/*` | 覆盖 malloc/free、泄漏、越界、对齐，没有 malloc 实现、cache、内存分配策略和性能细节 |
| 8 | 为什么程序员无法分清万圣节和圣诞节 | 部分覆盖 | `01_types_variables/02_signed_unsigned`、`01_types_variables/03_overflow`、`10_stdlib_io/01`、`10_stdlib_io/13` | 覆盖符号/溢出/格式化，没有整型提升、缺省参数提升、函数原型与 `printf` 可变参数的完整讨论 |
| 9 | 再论数组 | 部分覆盖 | `05_arrays_strings/03_multidimensional`、`06_pointers/07_pointer_to_array`、`02_operators/06_sizeof_incdec` | 有多维数组、数组指针、sizeof，没有更深入的数组/指针等价与下标运算细节 |
| 10 | 再论指针 | 部分覆盖 | `06_pointers/01`-`10`、`04_functions/06_function_pointers`、`12_advanced_c/01_variadic` | 指针基础较完整，没有函数指针数组、指针别名、restrict 契约、复杂指针声明的系统训练 |
| 11 | 你懂得 C，所以 C++ 不在话下 | 不适用 | 无 | 这是 C/C++ 差异章节，按项目约定不加入 C++ 内容 |

## 结论

现有项目覆盖了这本书中**偏语言层面的部分**：

- 数组与指针的区别；
- 多翻译单元和基础链接；
- 内存分配、泄漏、越界；
- 部分未定义行为；
- 部分类型转换和格式化。

但这本书真正独特的内容还缺：

1. **编译器和标准细节**：ANSI C 变更、实现定义行为、pragma、编译器限制。
2. **声明语法**：完整声明解析、复杂声明、函数指针数组。
3. **链接器细节**：动态链接、interpositioning、符号解析、链接器报告。
4. **运行时结构**：a.out/ELF、段、栈帧、活动记录、调用约定、进程内存布局。
5. **内存实现**：malloc 实现、cache、分配策略、性能。
6. **类型提升**：整型提升、缺省参数提升、原型与可变参数。
7. **高级数组/指针**：数组指针、函数指针表、别名和 restrict。

本轮只做 OCR 和覆盖核对，没有把这些练习加入项目。
