# Curriculum and coverage map

This map connects each topic to the exercises that teach it and to the
corresponding section of *C语言深度解剖*.  The book is a deep-dive
companion; the exercises also cover standard-library, tooling, and
portability topics that are outside the book's original scope.

Total exercises: **146** across **20** topics.

## 00_getting_started - Getting Started

| Exercise | Objective | Book reference |
| --- | --- | --- |
| `00_getting_started/01_hello_world` | Understand the minimal C program and formatted output. | 第一章 前言；任意 C 入门章节 |
| `00_getting_started/02_compilation_model` | See how the preprocessor and the C standard version are exposed. | 第三章 预处理；编译流程资料 |
| `00_getting_started/03_main_args` | Work with the arguments passed to main. | 第六章 函数；C 标准 5.1.2.2.1 |
| `00_getting_started/04_debug_assert` | Use assert for programmer errors and return values for user errors. | 第五章 内存管理；调试与测试资料 |
| `00_getting_started/05_compiler_diagnostics` | Fix a format-string warning that the compiler reports. | 第一章 1.5 sizeof；格式化输入输出资料 |
| `00_getting_started/06_lexical_elements` | Recognize comments, backslash-newline continuation, and escape sequences. | 第二章 2.1 注释符号；2.2 接续符和转义符 |

## 01_types_variables - Types, Variables, and Storage

| Exercise | Objective | Book reference |
| --- | --- | --- |
| `01_types_variables/01_integer_types` | Use sizeof, CHAR_BIT, INT_MIN, and INT_MAX correctly. | 第一章 1.4 基本数据类型 |
| `01_types_variables/02_signed_unsigned` | Avoid the usual arithmetic conversion trap when comparing. | 第一章 1.4 signed、unsigned 关键字 |
| `01_types_variables/03_overflow` | Understand modulo wrap and avoid signed integer overflow. | 第一章 1.4 基本数据类型；第五章 内存管理 |
| `01_types_variables/04_floating_point` | Compare floating-point values with an epsilon. | 第一章 1.6.2 float 与零值比较 |
| `01_types_variables/05_char_ascii` | Work with char values and the ctype classification functions. | 第一章 1.4 基本数据类型 |
| `01_types_variables/06_storage_scope` | Observe the lifetime of a static variable and block scope. | 第一章 1.1-1.3 auto、register、static |
| `01_types_variables/07_qualifiers` | Use const, volatile, restrict, extern, auto, and register. | 第一章 1.1-1.3 auto、register、static；1.11 const；1.12 volatile；1.13 extern |
| `01_types_variables/08_stdbool_stddef` | Use bool and size_t from the standard headers. | 第一章 1.4 基本数据类型；C99/C11 标准库 |
| `01_types_variables/09_long_double` | Use long double and compare its precision with double. | C Primer Plus 第3章 3.4.6 |

## 02_operators - Operators and Expressions

| Exercise | Objective | Book reference |
| --- | --- | --- |
| `02_operators/01_arithmetic` | Practice integer division, modulo, and truncation. | 第二章 2.4 逻辑运算符；2.8 除法 |
| `02_operators/02_precedence` | Use parentheses to express intent clearly. | 第二章 2.9 运算符的优先级 |
| `02_operators/03_short_circuit` | Observe that && and || may not evaluate their right operand. | 第二章 2.4 逻辑运算符 |
| `02_operators/04_bitwise` | Use masks and bitwise operators safely. | 第二章 2.5 位运算符 |
| `02_operators/05_shifts` | Build masks and avoid shifting by the width of the type. | 第二章 2.5.1 左移和右移 |
| `02_operators/06_sizeof_incdec` | Distinguish sizeof expressions from increment side effects. | 第一章 1.5 sizeof；第二章 2.7 ++、-- |
| `02_operators/07_compound_assignment` | Use +=, -=, *=, /=, %= and the comma operator. | C Primer Plus 第5章 5.3、第6章 6.6-6.7 |

## 03_control_flow - Control Flow

| Exercise | Objective | Book reference |
| --- | --- | --- |
| `03_control_flow/01_if_else` | Write clear conditional branches. | 第一章 1.6 if、else 组合 |
| `03_control_flow/02_switch_case` | Use intentional fallthrough and a default case. | 第一章 1.7 switch、case 组合 |
| `03_control_flow/03_loops` | Get loop bounds and accumulators right. | 第一章 1.8 do、while、for |
| `03_control_flow/04_break_continue` | Use break to stop early and continue to skip one iteration. | 第一章 1.8.1 break 与 continue 的区别 |
| `03_control_flow/05_goto_cleanup` | Use goto for a clear cleanup path in C. | 第一章 1.9 goto 关键字；第六章 函数设计 |
| `03_control_flow/06_state_machine` | Track state while scanning a string. | 第三章 3.2 条件编译；控制流综合练习 |
| `03_control_flow/07_while_do_while` | Distinguish entry-condition and exit-condition loops. | C Primer Plus 第6章 6.2、6.8 |

## 04_functions - Functions and Scope

| Exercise | Objective | Book reference |
| --- | --- | --- |
| `04_functions/01_declaration_definition` | Use a forward declaration and an internal helper. | 第六章 函数 |
| `04_functions/02_parameters_return` | Return values through parameters and clamp a range. | 第六章 6.2 编码风格；6.2 函数设计 |
| `04_functions/03_pass_by_pointer` | Modify caller-owned data through pointers. | 第四章 4.6 数组参数与指针参数 |
| `04_functions/04_recursion` | Write recursive functions with correct base cases. | 第六章 6.4 函数递归 |
| `04_functions/05_static_inline` | Use static functions and file-scope state. | 第一章 1.3 static 关键字；第六章 函数 |
| `04_functions/06_function_pointers` | Store functions in variables and choose one at runtime. | 第四章 4.7 函数指针 |
| `04_functions/07_void_and_return` | Return early from a void function and return values from int functions. | 第一章 1.10 void 关键字；1.10 return 关键字 |
| `04_functions/08_tail_recursion` | Rewrite a recursive sum using an accumulator. | C Primer Plus 第9章 9.3.3 |

## 05_arrays_strings - Arrays and Strings

| Exercise | Objective | Book reference |
| --- | --- | --- |
| `05_arrays_strings/01_array_basics` | Iterate over an array and compute a sum and maximum. | 第四章 4.2 数组 |
| `05_arrays_strings/02_array_decay` | See how an array parameter becomes a pointer. | 第四章 4.3 指针与数组之间的恩恩怨怨 |
| `05_arrays_strings/03_multidimensional` | Transpose a 3x3 matrix with nested loops. | 第四章 4.5 多维数组与多级指针 |
| `05_arrays_strings/04_string_literals` | Scan a const string and modify a mutable char array. | 第四章 4.2 数组；第二章 2.3 单引号、双引号 |
| `05_arrays_strings/05_string_ops` | Implement strlen, strcmp, and strcpy with pointers. | 第四章 4.3 指针与数组；第六章 6.4.2 strlen |
| `05_arrays_strings/06_safe_format` | Format text into a fixed-size buffer without overflow. | 第三章 3.1 宏定义；标准库 printf 资料 |
| `05_arrays_strings/07_tokenize` | Split a string without modifying the caller's buffer. | 第五章 内存管理；标准库 string.h 资料 |
| `05_arrays_strings/08_vla` | Create an array whose length is a runtime value. | C Primer Plus 第10章 10.8 |
| `05_arrays_strings/09_compound_literals` | Create a temporary struct value with a compound literal. | C Primer Plus 第10章 10.9 |
| `05_arrays_strings/10_pointer_compatibility` | Pass a non-const array through a pointer-to-const. | C Primer Plus 第10章 10.6-10.7 |

## 06_pointers - Pointers and Memory Layout

| Exercise | Objective | Book reference |
| --- | --- | --- |
| `06_pointers/01_pointer_basics` | Read and write through pointers. | 第四章 4.1 指针 |
| `06_pointers/02_null_and_const` | Check for NULL and respect pointer-to-const. | 第四章 4.1.3 int *p = NULL 和 *p = NULL |
| `06_pointers/03_pointer_arithmetic` | Walk an array with pointers and return a pointer into it. | 第四章 4.3.1 以指针的形式访问和以下标的形式访问 |
| `06_pointers/04_pointer_to_pointer` | Let a function allocate and update a caller-owned pointer. | 第四章 4.5.2 二级指针 |
| `06_pointers/05_void_pointer` | Use void pointers and unsigned char for type-agnostic code. | 第四章 4.1.6 如何达到手中无剑、胸中也无剑的地步 |
| `06_pointers/06_dangling_wild` | Set a freed pointer to NULL to prevent accidental reuse. | 第五章 5.1 什么是野指针；5.3.5 内存泄漏 |
| `06_pointers/07_pointer_to_array` | Distinguish a pointer to an array from a pointer to its first element. | 第四章 4.3.2 a 和 &a 的区别；4.4 指针数组和数组指针 |

## 07_dynamic_memory - Dynamic Memory and Data Structures

| Exercise | Objective | Book reference |
| --- | --- | --- |
| `07_dynamic_memory/01_malloc_free` | Use malloc and free for a dynamically sized array. | 第五章 5.3.5 内存泄漏；如何使用 malloc 函数 |
| `07_dynamic_memory/02_calloc` | Use calloc when every byte must start as zero. | 第五章 5.3.5.3 用 malloc 函数申请 0 字节内存 |
| `07_dynamic_memory/03_realloc` | Use realloc safely and initialize only the new elements. | 第五章 5.3.5 内存泄漏；malloc/realloc 资料 |
| `07_dynamic_memory/04_memory_leak` | Pair every allocation with a matching free. | 第五章 5.3.5 内存泄漏 |
| `07_dynamic_memory/05_buffer_bounds` | Copy at most dest_size - 1 bytes and always terminate. | 第五章 5.3.4 内存越界；5.3.2 为指针分配的内存太小 |
| `07_dynamic_memory/06_flexible_array` | Allocate a struct plus trailing data in one block. | 第一章 1.14.2 柔性数组 |
| `07_dynamic_memory/07_linked_list` | Build, traverse, and free a linked list. | 第五章 内存管理；结构体与指针综合 |

## 08_structs_unions_enums - Structs, Unions, Enums, and Bitfields

| Exercise | Objective | Book reference |
| --- | --- | --- |
| `08_structs_unions_enums/01_struct_basics` | Create a struct value and access its members through a pointer. | 第一章 1.14 struct 关键字 |
| `08_structs_unions_enums/02_nested_structs` | Access a nested member through an outer struct pointer. | 第一章 1.14 struct 关键字 |
| `08_structs_unions_enums/03_padding_alignment` | Observe padding and member offsets with offsetof. | 第一章 1.14.1 空结构体多大；第三章 3.6.8 #pragma pack |
| `08_structs_unions_enums/04_bitfields` | Store several small flags in one struct. | 第一章 1.14 struct 关键字；2.5 位运算符 |
| `08_structs_unions_enums/05_union` | Compare union size with the size of its largest member. | 第一章 1.15 union 关键字 |
| `08_structs_unions_enums/06_enum` | Use an enum for a small closed set of values. | 第一章 1.16 enum 关键字 |
| `08_structs_unions_enums/07_typedef_designated` | Use a typedef and initialize members by name. | 第一章 1.17 typedef 关键字 |
| `08_structs_unions_enums/08_container_of` | Recover an outer struct from a pointer to one of its members. | 第一章 1.14 struct 关键字；1.5 sizeof |
| `08_structs_unions_enums/09_struct_array` | Traverse an array of structs and find the best element. | C Primer Plus 第14章 14.4 |
| `08_structs_unions_enums/10_struct_pass` | Compare struct value parameters with struct pointer parameters. | C Primer Plus 第14章 14.7 |
| `08_structs_unions_enums/11_struct_file` | Store a struct with fwrite and read it back with fread. | C Primer Plus 第14章 14.8 |
| `08_structs_unions_enums/12_complex_declarations` | Read and use a typedef for a function pointer and an array of function pointers. | C Primer Plus 第14章 14.13-14.14 |

## 09_preprocessor - Preprocessor and Macros

| Exercise | Objective | Book reference |
| --- | --- | --- |
| `09_preprocessor/01_object_macro` | Use a named compile-time constant. | 第三章 3.1.1 数值宏常量 |
| `09_preprocessor/02_function_macro` | Protect macro arguments and the whole expansion with parentheses. | 第三章 3.1.4 用 define 宏定义表达式 |
| `09_preprocessor/03_stringize_paste` | Use # to stringize and ## to paste tokens. | 第三章 3.7 #运算符；3.8 ##运算符 |
| `09_preprocessor/04_conditional_compilation` | Select code at preprocessing time based on the language version. | 第三章 3.2 条件编译 |
| `09_preprocessor/05_include_guards` | Prevent multiple inclusion with a preprocessor guard. | 第三章 3.3 文件包含 |
| `09_preprocessor/06_variadic_macros` | Forward a variable argument list to a variadic function. | 第三章 3.1 宏定义；第六章 函数 |
| `09_preprocessor/07_x_macros` | Generate an enum and a string table from one list. | 第三章 3.1 宏定义；3.7 #运算符 |
| `09_preprocessor/08_pragma_error_line` | Use diagnostics, line control, and packing pragmas. | 第三章 3.4 #error；3.5 #line；3.6.8 #pragma pack |
| `09_preprocessor/09_std_macros` | Use __FILE__, __LINE__, __func__, and __STDC_VERSION__. | 第三章 3.1 宏定义；编译器预定义宏 |
| `09_preprocessor/10_undef_defined` | Undefine a macro and test it with defined(). | C Primer Plus 第16章 16.6.1-16.6.2 |

## 10_stdlib_io - Standard Library and File I/O

| Exercise | Objective | Book reference |
| --- | --- | --- |
| `10_stdlib_io/01_printf_formats` | Match each conversion specifier to its argument type. | 第一章 1.5 sizeof；标准库 printf 资料 |
| `10_stdlib_io/02_scanf_parse` | Parse a comma-separated pair with sscanf. | 第一章 1.6 条件判断；标准库 scanf 资料 |
| `10_stdlib_io/03_strtol_errno` | Use strtol, errno, and the end pointer to validate input. | 第五章 5.3.1 函数的入口校验；标准库 strtol 资料 |
| `10_stdlib_io/04_qsort_bsearch` | Use comparison callbacks for sorting and searching. | 第四章 4.7 函数指针；标准库 qsort 资料 |
| `10_stdlib_io/05_math_functions` | Use hypot and other functions from math.h. | 第一章 1.4 基本数据类型；标准库 math.h 资料 |
| `10_stdlib_io/06_time_functions` | Use time_t and difftime. | 标准库 time.h 资料 |
| `10_stdlib_io/07_random` | Seed the generator and bound its output. | 标准库 stdlib.h 资料 |
| `10_stdlib_io/08_file_io` | Write and read a text file with fopen, fputs, and fread. | 第五章 5.3.5 内存泄漏；标准库 stdio.h 资料 |
| `10_stdlib_io/09_memory_functions` | Use the byte-oriented memory functions correctly. | 第四章 指针与数组；标准库 string.h 资料 |
| `10_stdlib_io/10_string_search` | Use strchr, strrchr, and strstr. | 第五章 内存管理；标准库 string.h 资料 |
| `10_stdlib_io/11_stdint_inttypes` | Use uint64_t and PRIu64 from stdint.h and inttypes.h. | 第一章 1.4 基本数据类型；C99 标准库 |
| `10_stdlib_io/12_environment` | Read and write environment variables with getenv and setenv. | 第五章 5.3.1.3 函数的入口校验；标准库 stdlib.h 资料 |
| `10_stdlib_io/13_printf_advanced` | Use width, zero padding, precision, and the * width argument. | C Primer Plus 第4章 4.4.3-4.4.6 |
| `10_stdlib_io/14_scanf_advanced` | Use field width and a scanset in sscanf. | C Primer Plus 第4章 4.4.5、第11章 11.2.4 |
| `10_stdlib_io/15_ctype_full` | Use isalnum and toupper with unsigned char casts. | C Primer Plus 第7章 7.2.2、第11章 11.7 |

## 11_ub_safety - Undefined Behavior, Safety, and Portability

| Exercise | Objective | Book reference |
| --- | --- | --- |
| `11_ub_safety/01_signed_overflow` | Detect overflow before performing signed addition. | 第一章 1.4 signed、unsigned 关键字；第五章 内存管理 |
| `11_ub_safety/02_uninitialized` | Give every local variable a defined initial value. | 第五章 5.3.3 内存分配成功，但并未初始化 |
| `11_ub_safety/03_out_of_bounds` | Reject indices outside the logical array length. | 第五章 5.3.4 内存越界 |
| `11_ub_safety/04_use_after_free` | Clear a pointer after freeing its target. | 第五章 5.3.6 内存已经被释放了，但是继续通过指针来使用 |
| `11_ub_safety/05_sequence_points` | Avoid unsequenced reads and writes of the same object. | 第二章 2.7 ++、--操作符 |
| `11_ub_safety/06_strict_aliasing` | Reinterpret object representation with memcpy. | 第四章 4.7.2 *(int*)&p；第五章 内存管理 |
| `11_ub_safety/07_alignment` | Query alignment with alignof and keep members aligned. | 第三章 3.6.8.1 为什么会有内存对齐 |
| `11_ub_safety/08_null_pointer` | Never dereference a null pointer. | 第四章 4.1.3 int *p = NULL 和 *p = NULL 有什么区别 |

## 12_advanced_c - Advanced C Features

| Exercise | Objective | Book reference |
| --- | --- | --- |
| `12_advanced_c/01_variadic` | Read a variable number of int arguments with va_list. | 第六章 函数；C 标准 stdarg.h |
| `12_advanced_c/02_setjmp_longjmp` | Use non-local jumps for a simple error path. | 第六章 函数；C 标准 setjmp.h |
| `12_advanced_c/03_pthreads` | Create threads and protect shared state with a mutex. | 第六章 函数；POSIX threads 资料 |
| `12_advanced_c/04_atomics` | Use atomic_int for lock-free counter updates. | C11 标准 atomics 资料 |
| `12_advanced_c/05_generic` | Choose an expression based on the type of a value. | C11 标准 _Generic 资料 |
| `12_advanced_c/06_static_assert` | Use _Static_assert to enforce assumptions at compile time. | C11 标准 _Static_assert 资料 |
| `12_advanced_c/07_align` | Query and request alignment. | C11 标准 alignof/alignas 资料 |
| `12_advanced_c/08_anonymous_union` | Access anonymous union members directly through the outer struct. | 第一章 1.15 union 关键字；C11 匿名结构体/联合 |
| `12_advanced_c/09_thread_local` | Use _Thread_local to give each thread its own object. | C11 标准 _Thread_local 资料；POSIX threads |
| `12_advanced_c/10_complex` | Use double complex, I, conj, creal, and cimag. | C99 标准 complex.h 资料 |
| `12_advanced_c/11_signal` | Install a signal handler and use a sig_atomic_t flag. | C 标准 signal.h 资料 |

## 13_translation_units - Translation Units, Headers, and Linkage

| Exercise | Objective | Book reference |
| --- | --- | --- |
| `13_translation_units/01_header_source_split` | Compile a program from a main file, a header, and an implementation file. | C Primer Plus 第9章 9.4、第16章 16.5 |
| `13_translation_units/02_extern_linkage` | Declare a global variable in a header and define it in another file. | C Primer Plus 第12章 12.1.7、12.1.9 |
| `13_translation_units/03_static_internal_linkage` | Keep a counter private to one translation unit with static. | C Primer Plus 第12章 12.1.8-12.1.9 |

## 14_character_io - Character I/O and Input Validation

| Exercise | Objective | Book reference |
| --- | --- | --- |
| `14_character_io/01_getc_putc` | Copy a stream one character at a time with getc and putc. | C Primer Plus 第8章 8.1、第13章 13.2.3 |
| `14_character_io/02_eof_ferror` | Read until EOF and distinguish end-of-file from an error. | C Primer Plus 第8章 8.3、第13章 13.7.7 |
| `14_character_io/03_input_validation` | Reject input with trailing characters or out-of-range values. | C Primer Plus 第8章 8.6 |
| `14_character_io/04_iso646` | Use and/or/not from iso646.h. | C Primer Plus 第7章 7.3.1 |

## 15_string_functions - String Functions and Conversion

| Exercise | Objective | Book reference |
| --- | --- | --- |
| `15_string_functions/01_strcat_strncat` | Append a string while respecting the destination size. | C Primer Plus 第11章 11.5.2-11.5.3 |
| `15_string_functions/02_strncpy_bounded` | Copy a string safely and always terminate the destination. | C Primer Plus 第11章 11.5.5 |
| `15_string_functions/03_sprintf_snprintf` | Format text with snprintf and understand truncation. | C Primer Plus 第11章 11.5.6 |
| `15_string_functions/04_fgets_fputs_sort` | Read a line with fgets and sort an array of strings. | C Primer Plus 第11章 11.2.3、11.6 |
| `15_string_functions/05_strtod` | Parse a double with strtod and reject trailing input. | C Primer Plus 第11章 11.9 |

## 16_data_representation - Data Representation and Bit Operations

| Exercise | Objective | Book reference |
| --- | --- | --- |
| `16_data_representation/01_base_conversion` | Parse a hexadecimal string with strtoul. | C Primer Plus 第15章 15.2 |
| `16_data_representation/02_integer_binary_representation` | Count set bits and convert sign-magnitude to two's complement. | C Primer Plus 第15章 15.1 |
| `16_data_representation/03_float_binary_representation` | Inspect and reconstruct an IEEE-754 float with memcpy. | C Primer Plus 第15章 15.1.3 |
| `16_data_representation/04_bitfield_portability` | Pack fields with bitfields and compare them with an explicit mask. | C Primer Plus 第15章 15.4 |

## 17_data_structures - Abstract Data Types and Data Structures

| Exercise | Objective | Book reference |
| --- | --- | --- |
| `17_data_structures/01_queue_adt` | Implement a fixed-capacity circular queue. | C Primer Plus 第17章 17.4 |
| `17_data_structures/02_binary_search_tree` | Insert into and search a binary search tree. | C Primer Plus 第17章 17.7 |
| `17_data_structures/03_dynamic_vector` | Grow a dynamic array and preserve existing elements. | C Primer Plus 第17章 17.2、17.6 |

## 18_file_io_advanced - Advanced File I/O

| Exercise | Objective | Book reference |
| --- | --- | --- |
| `18_file_io_advanced/01_fprintf_fscanf` | Write formatted data to a file and read it back. | C Primer Plus 第13章 13.4.1 |
| `18_file_io_advanced/02_fgets_fputs` | Copy a text file line by line. | C Primer Plus 第13章 13.4.2 |
| `18_file_io_advanced/03_getc_putc_ungetc` | Peek at a character and put it back into the stream. | C Primer Plus 第13章 13.2.3、13.7.1 |
| `18_file_io_advanced/04_fseek_ftell` | Seek to a byte offset and report the resulting position. | C Primer Plus 第13章 13.5 |
| `18_file_io_advanced/05_fflush_setvbuf` | Configure full buffering and flush a stream. | C Primer Plus 第13章 13.7.2-13.7.3 |
| `18_file_io_advanced/06_binary_random_access` | Read a specific struct record from a binary file. | C Primer Plus 第13章 13.7.9 |

## 19_modern_c_library - Modern C Library and Language Features

| Exercise | Objective | Book reference |
| --- | --- | --- |
| `19_modern_c_library/01_noreturn` | Declare a function that never returns and observe its exit status. | C Primer Plus 第16章 16.8 |
| `19_modern_c_library/02_tgmath` | Use sqrt with both double and float arguments through tgmath.h. | C Primer Plus 第16章 16.10.3 |
| `19_modern_c_library/03_atexit` | Register a cleanup function with atexit. | C Primer Plus 第16章 16.11.1 |
| `19_modern_c_library/04_atomic_flag` | Use atomic_flag as a simple test-and-set lock. | C Primer Plus 第12章 12.5.4；C11 stdatomic.h |

## Cross-cutting knowledge checklist

The following C knowledge areas are deliberately covered by the
exercises and supporting documentation:

- Translation units, declarations, definitions, linkage, and the
  preprocessing/compiling/assembling/linking pipeline.
- All standard integer and floating types, `<limits.h>` and
  `<float.h>`, signed/unsigned conversions, overflow, and casts.
- Constants, `const`, `enum`, `#define`, storage classes, scope,
  lifetime, and name lookup.
- Every operator family: arithmetic, relational, logical,
  bitwise, shift, assignment, conditional, comma, `sizeof`,
  address-of, dereference, member access, and casts.
- Sequence points, short-circuit evaluation, precedence,
  associativity, and side effects.
- `if`, `switch`, `for`, `while`, `do-while`, `break`,
  `continue`, `goto`, nested control flow, and state machines.
- Function declarations, definitions, parameters, return values,
  recursion, `static`, `inline`, function pointers, callbacks,
  variadic functions, and scope.
- Arrays, array decay, multidimensional arrays, variable-length
  arrays, string literals, mutable strings, `<string.h>`,
  bounded formatting, tokenization, and UTF-8 basics.
- Pointer representation, `NULL`, pointer arithmetic, arrays vs
  pointers, `const` placement, multi-level pointers, `void *`,
  function pointers, dangling/wild pointers, `restrict`, and
  endianness.
- `malloc`, `calloc`, `realloc`, `free`, ownership, leaks,
  use-after-free, double free, bounds, flexible array members,
  linked lists, dynamic arrays, and basic allocator reasoning.
- Structs, nested structs, padding/alignment, bitfields, unions,
  enums, typedefs, designated initializers, compound literals,
  `offsetof`, and `container_of`.
- Object-like and function-like macros, macro hygiene,
  stringizing, token pasting, conditional compilation, include
  guards, variadic macros, X-macros, and `#pragma`.
- `printf`/`scanf`, `strtol`, `errno`, `qsort`, `bsearch`,
  `math.h`, `time.h`, `rand`, `ctype.h`, environment/exit,
  text and binary file I/O, seeking, and error handling.
- Undefined behavior, implementation-defined behavior, signed
  overflow, uninitialized reads, out-of-bounds access, sequence
  points, strict aliasing, alignment, and null dereference.
- Advanced C11/C17 features: `_Generic`, `_Static_assert`,
  `_Alignof`/`_Alignas`, atomics, POSIX threads, `setjmp`,
  `longjmp`, signals, and variadic functions.

## Suggested learning path

1. `00_getting_started` and `01_types_variables`
2. `02_operators` and `03_control_flow`
3. `04_functions` and `05_arrays_strings`
4. `06_pointers` and `07_dynamic_memory`
5. `08_structs_unions_enums` and `09_preprocessor`
6. `10_stdlib_io` and `11_ub_safety`
7. `12_advanced_c`

Do not read the solutions until you have run the exercise and
looked at the compiler or test output.  The point is to learn the
feedback loop, not to collect green checkmarks.
