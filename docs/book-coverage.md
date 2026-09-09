# 《C 语言深度解剖》章节覆盖

本项目把书籍作为“深入理解”的参考，而不是唯一的课程边界。下表把书的
七章映射到练习和工程文档；完整练习清单见
[curriculum.md](curriculum.md)。

## 第一章 关键字

| 书中的主题 | 对应练习 |
| --- | --- |
| `auto`、`register` | `01_types_variables/07_qualifiers` |
| `static`、作用域、生命周期 | `01_types_variables/06_storage_scope`, `04_functions/05_static_inline` |
| `short`、`int`、`long`、`char`、`float`、`double` | `01_types_variables/01_integer_types`, `01_types_variables/04_floating_point`, `01_types_variables/05_char_ascii` |
| 变量命名规则 | 全部练习 |
| `sizeof` | `02_operators/06_sizeof_incdec`, `05_arrays_strings/02_array_decay`, `08_structs_unions_enums/03_padding_alignment` |
| `signed`、`unsigned` | `01_types_variables/02_signed_unsigned`, `01_types_variables/03_overflow` |
| `if`、`else` | `03_control_flow/01_if_else` |
| `switch`、`case` | `03_control_flow/02_switch_case` |
| `do`、`while`、`for`、`break`、`continue` | `03_control_flow/03_loops`, `03_control_flow/04_break_continue` |
| `goto` | `03_control_flow/05_goto_cleanup` |
| `void`、`return` | `04_functions/07_void_and_return` |
| `const` | `01_types_variables/07_qualifiers`, `06_pointers/02_null_and_const` |
| `volatile` | `01_types_variables/07_qualifiers`, `12_advanced_c/11_signal` |
| `extern` | `01_types_variables/07_qualifiers` |
| `struct` | `08_structs_unions_enums/01_struct_basics` 至 `08_container_of` |
| 空结构体、柔性数组 | `07_dynamic_memory/06_flexible_array` |
| `union` | `08_structs_unions_enums/05_union`, `12_advanced_c/08_anonymous_union` |
| `enum` | `08_structs_unions_enums/06_enum` |
| `typedef` | `08_structs_unions_enums/07_typedef_designated` |

## 第二章 符号

| 书中的主题 | 对应练习 |
| --- | --- |
| 注释符号 | `00_getting_started/06_lexical_elements` |
| 接续符和转义符 | `00_getting_started/06_lexical_elements` |
| 单引号、双引号 | `01_types_variables/05_char_ascii`, `05_arrays_strings/04_string_literals` |
| 逻辑运算符、短路求值 | `02_operators/03_short_circuit` |
| 位运算符、移位 | `02_operators/04_bitwise`, `02_operators/05_shifts` |
| 花括号、作用域 | `03_control_flow/*`, `04_functions/05_static_inline` |
| `++`、`--` | `02_operators/06_sizeof_incdec`, `11_ub_safety/05_sequence_points` |
| 除法与负数取模 | `02_operators/01_arithmetic` |
| 运算符优先级 | `02_operators/02_precedence` |

## 第三章 预处理

| 书中的主题 | 对应练习 |
| --- | --- |
| 数值/字符串宏常量 | `09_preprocessor/01_object_macro` |
| 带参数的宏、宏展开陷阱 | `09_preprocessor/02_function_macro` |
| `#undef` | 生成器与练习中的宏定义 |
| 条件编译 | `09_preprocessor/04_conditional_compilation`, `00_getting_started/02_compilation_model` |
| 文件包含、头文件保护 | `09_preprocessor/05_include_guards` |
| `#error`、`#line` | `09_preprocessor/08_pragma_error_line` |
| `#pragma`、`#pragma pack` | `09_preprocessor/08_pragma_error_line`, `08_structs_unions_enums/03_padding_alignment` |
| `#`、`##` | `09_preprocessor/03_stringize_paste` |

## 第四章 指针和数组

| 书中的主题 | 对应练习 |
| --- | --- |
| 指针的内存布局 | `06_pointers/01_pointer_basics` |
| `*` 与地址 | `06_pointers/01_pointer_basics` |
| `int *p = NULL` 与 `*p = NULL` | `06_pointers/02_null_and_const`, `11_ub_safety/08_null_pointer` |
| 数组的内存布局 | `05_arrays_strings/01_array_basics` |
| 数组名作为左值和右值 | `05_arrays_strings/02_array_decay` |
| 指针与数组的访问方式 | `05_arrays_strings/02_array_decay`, `06_pointers/03_pointer_arithmetic` |
| `a` 和 `&a` 的区别 | `06_pointers/07_pointer_to_array` |
| 指针数组与数组指针 | `06_pointers/07_pointer_to_array` |
| 多维数组与多级指针 | `05_arrays_strings/03_multidimensional`, `06_pointers/04_pointer_to_pointer` |
| 数组参数与指针参数 | `05_arrays_strings/02_array_decay`, `04_functions/03_pass_by_pointer` |
| 函数指针、函数指针数组 | `04_functions/06_function_pointers`, `10_stdlib_io/04_qsort_bsearch` |

## 第五章 内存管理

| 书中的主题 | 对应练习 |
| --- | --- |
| 野指针 | `06_pointers/06_dangling_wild` |
| 栈、堆和静态区 | `01_types_variables/06_storage_scope`, `07_dynamic_memory/01_malloc_free` |
| 指针未初始化、入口校验 | `11_ub_safety/02_uninitialized`, `11_ub_safety/08_null_pointer` |
| 分配内存太小、内存越界 | `07_dynamic_memory/05_buffer_bounds`, `11_ub_safety/03_out_of_bounds` |
| 分配成功但未初始化 | `07_dynamic_memory/02_calloc`, `11_ub_safety/02_uninitialized` |
| 内存泄漏、`malloc` 使用 | `07_dynamic_memory/04_memory_leak`, `07_dynamic_memory/01_malloc_free` |
| `free` 之后继续使用 | `11_ub_safety/04_use_after_free` |
| 柔性数组 | `07_dynamic_memory/06_flexible_array` |

## 第六章 函数

| 书中的主题 | 对应练习 |
| --- | --- |
| 函数的由来与好处 | `04_functions/01_declaration_definition` |
| 编码风格、函数设计原则 | 全部练习 |
| 递归 | `04_functions/04_recursion` |
| 不使用变量实现 `strlen` | `05_arrays_strings/05_string_ops` |
| 函数指针 | `04_functions/06_function_pointers` |
| 变参函数 | `12_advanced_c/01_variadic` |
| `setjmp` / `longjmp` | `12_advanced_c/02_setjmp_longjmp` |

## 第七章 文件结构

书中的“文件内容规则、文件名规则”属于工程组织问题。本项目用以下文件
和文档来实践：

- `Makefile`、`CMakeLists.txt`、`CMakePresets.json`：构建组织。
- `include/clings/test.h`：公共测试接口。
- `tools/`：生成器和 PDF 转换器。
- `docs/architecture.md`：目录约定与分层。
- `CONTRIBUTING.md`：新增练习的规则。
