# C knowledge coverage map

This map is organized by C language and systems-programming knowledge areas.
Every row points to at least one exercise.

## 1. Program structure, translation, and tooling

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| Minimal C program, `main`, return value | `00_basics/01_printf`, `08_arrays_strings/16_main_args` | A C program is a collection of declarations and definitions. |
| Preprocessing, compiling, assembling, linking | `00_basics/07_include_header`, `01_preprocessor/*` | `#include`, declarations, conditional compilation. |
| `argc`, `argv`, program environment | `08_arrays_strings/16_main_args` | `argv[0]` is the program name; arguments start at `argv[1]`. |
| Assertions and defensive checks | `02_macros/10_assert_macro` | `assert` for programmer errors; return codes for recoverable errors. |
| Reading compiler diagnostics | `00_basics/09_compiler_diagnostics`, `12_standard_library/01_printf_formats` | Format-string diagnostics, `-Wformat`, `-Werror`. |
| Build systems and project layout | README, `Makefile`, `CMakeLists.txt`, `CMakePresets.json` | CLI, Make, CMake, CTest, Docker. |
| Testing workflow | `./clings verify`, `./clings selftest`, `include/clings/test.h` | Dependency-free assertion harness. |

## 2. Lexical elements, types, and objects

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| Comments, identifiers, keywords | all exercises | Lexical and keyword usage across the exercises. |
| Comments, line continuation, escapes | `00_basics/08_lexical_elements` | `/* ... */`, backslash-newline, `\n`, `\t`, `\"`. |
| Character constants and string literals | `03_types_variables/05_char_ascii`, `08_arrays_strings/04_string_literals` | `char`, ASCII, mutable arrays vs immutable literals. |
| Integer types and ranges | `03_types_variables/01_integer_types` | `sizeof`, `CHAR_BIT`, `INT_MIN`, `INT_MAX`. |
| Signed and unsigned | `03_types_variables/02_signed_unsigned`, `15_ub_safety/01_signed_overflow` | Usual arithmetic conversions and overflow. |
| Integer overflow and wraparound | `03_types_variables/03_overflow`, `15_ub_safety/01_signed_overflow` | Unsigned wraps; signed overflow is undefined behavior. |
| Floating-point types | `03_types_variables/04_floating_point` | Epsilon comparison, `fabs`, representation limits. |
| Character classification | `03_types_variables/05_char_ascii` | ASCII assumptions and portable `ctype.h` usage. |
| `const`, `enum`, `#define` constants | `03_types_variables/06_storage_scope`, `01_preprocessor/01_object_macro`, `10_aggregates/06_enum` | Three ways to express named constants. |
| `auto`, `register`, `static`, scope, lifetime | `03_types_variables/06_storage_scope`, `06_functions/05_static_inline` | File scope, block scope, static storage duration. |
| `const`, `volatile`, `restrict`, `extern`, `auto`, `register` | `03_types_variables/07_qualifiers` | Type qualifiers and storage-class specifiers. |
| `stdbool.h` and `stddef.h` | `03_types_variables/08_stdbool_stddef` | `bool`, `size_t`, and standard typedefs. |
| `typedef` and type aliases | `10_aggregates/07_typedef_designated` | `typedef` is not a macro. |
| `sizeof` and object size | `04_operators/06_sizeof_incdec`, `10_aggregates/03_padding_alignment` | `sizeof` is an operator, not a function. |

## 3. Expressions and operators

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| Arithmetic operators | `04_operators/01_arithmetic` | Integer division truncates toward zero; `%` is remainder. |
| Precedence and associativity | `04_operators/02_precedence` | Parentheses document intent and prevent surprises. |
| Logical operators and short-circuiting | `04_operators/03_short_circuit` | `&&` and `||` may skip the right operand. |
| Bitwise operators | `04_operators/04_bitwise`, `04_operators/05_shifts` | Set, clear, toggle, test, masks. |
| Shift operators and undefined behavior | `04_operators/05_shifts`, `15_ub_safety/05_sequence_points` | Shifting by the type width is undefined. |
| `sizeof` and increment/decrement | `04_operators/06_sizeof_incdec` | Post-increment vs pre-increment; `sizeof` does not evaluate its operand (except VLAs). |
| Conditional operator | `05_control_flow/01_if_else` | `a ? b : c` selects one expression. |
| Sequence points and side effects | `15_ub_safety/05_sequence_points` | Avoid unsequenced reads/writes of the same object. |
| Conversions and casts | `03_types_variables/02_signed_unsigned`, `15_ub_safety/06_strict_aliasing` | Explicit casts do not make undefined behavior defined. |

## 4. Control flow

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| `if`, `else`, nested conditions | `05_control_flow/01_if_else` | Compare booleans, floating values, and pointers correctly. |
| `switch`, `case`, `default`, fallthrough | `05_control_flow/02_switch_case` | Intentional fallthrough should be visible. |
| `for`, `while`, `do-while` | `05_control_flow/03_loops` | Loop bounds and accumulator initialization. |
| `break` and `continue` | `05_control_flow/04_break_continue` | Early exit vs skipping one iteration. |
| `goto` and single-exit cleanup | `05_control_flow/05_goto_cleanup` | A common C resource-cleanup pattern. |
| State machines | `05_control_flow/06_state_machine` | Track a small amount of state while scanning input. |

## 5. Functions, linkage, and scope

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| Declarations and definitions | `06_functions/01_declaration_definition` | A prototype and a definition can be separated. |
| Parameters and return values | `06_functions/02_parameters_return` | Output parameters, `void`, and range clamping. |
| Pass by value vs pass by pointer | `06_functions/03_pass_by_pointer` | C passes everything by value; pointers let you modify caller storage. |
| Recursion and base cases | `06_functions/04_recursion` | Factorial and Fibonacci. |
| Internal linkage, `static`, `inline` | `06_functions/05_static_inline` | File-scope state and helper functions. |
| Function pointers and callbacks | `06_functions/06_function_pointers`, `12_standard_library/03_qsort_bsearch` | Dispatch tables and `qsort` comparators. |
| Variadic functions | `18_advanced_c/01_variadic`, `02_macros/04_variadic_macros` | `stdarg.h`, `va_list`, variadic macros. |
| Non-local jumps | `18_advanced_c/02_setjmp_longjmp` | `setjmp`/`longjmp` error paths. |
| `void` functions and `return` | `06_functions/07_void_and_return` | Bare `return;`, early return, and value return. |

## 6. Arrays and strings

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| Array declaration, indexing, traversal | `08_arrays_strings/01_array_basics` | Contiguous objects and bounds. |
| Array-to-pointer decay | `08_arrays_strings/02_array_decay` | An array parameter is a pointer parameter. |
| Multidimensional arrays | `08_arrays_strings/03_multidimensional` | Row-major layout and nested indexing. |
| String literals vs `char` arrays | `08_arrays_strings/04_string_literals` | Literals are not modifiable; arrays are. |
| `strlen`, `strcmp`, `strcpy` | `08_arrays_strings/05_string_ops` | Reimplement the classic pointer algorithms. |
| Bounded formatting | `00_basics/05_snprintf` | `snprintf` writes formatted text into a fixed-size buffer. |
| Tokenization | `08_arrays_strings/06_tokenize` | `strtok_r` and non-destructive splitting. |
| Buffer bounds | `09_dynamic_memory/05_buffer_bounds` | Always reserve space for the terminating NUL. |

## 7. Pointers and the object model

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| Address-of and dereference | `07_pointers/01_pointer_basics` | `&` and `*`; writing through a pointer. |
| `NULL` and pointer checks | `07_pointers/02_null_and_const`, `15_ub_safety/08_null_pointer` | Never dereference a null pointer. |
| Pointer arithmetic | `07_pointers/03_pointer_arithmetic` | `p + n` moves by `n` elements, not bytes. |
| Pointers to pointers | `07_pointers/04_pointer_to_pointer` | Allocating and updating caller-owned pointers. |
| `void *` and generic byte access | `07_pointers/05_void_pointer` | Byte-wise swap with `unsigned char *`. |
| Dangling and wild pointers | `07_pointers/06_dangling_wild`, `15_ub_safety/04_use_after_free` | Set pointers to `NULL` after `free`. |
| Pointer-to-`const` vs `const` pointer | `07_pointers/02_null_and_const` | Read-only pointed-to data. |
| Array/pointer equivalence and limits | `08_arrays_strings/02_array_decay`, `08_arrays_strings/03_multidimensional` | `sizeof` differs for arrays and pointers. |
| Pointers to arrays, `a` vs `&a` | `07_pointers/07_pointer_to_array` | `int (*)[4]` advances by a whole row/array. |
| Strict aliasing | `15_ub_safety/06_strict_aliasing` | Use `memcpy` for type punning. |
| Alignment | `15_ub_safety/07_alignment`, `18_advanced_c/07_align` | `alignof`, `alignas`, padding. |

## 8. Dynamic memory and data structures

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| `malloc` and `free` | `09_dynamic_memory/01_malloc_free` | Allocate, initialize, release. |
| `calloc` | `09_dynamic_memory/02_calloc` | Zero-initialized allocation. |
| `realloc` | `09_dynamic_memory/03_realloc` | Grow while preserving existing elements. |
| Memory leaks | `09_dynamic_memory/04_memory_leak` | Track allocations and free every path. |
| Buffer bounds | `09_dynamic_memory/05_buffer_bounds` | Logical bounds vs allocated size. |
| Flexible array members | `09_dynamic_memory/06_flexible_array` | One allocation for a header plus payload. |
| Linked lists | `09_dynamic_memory/07_linked_list` | Nodes, traversal, and full cleanup. |
| Ownership and cleanup paths | `05_control_flow/05_goto_cleanup`, `09_dynamic_memory/04_memory_leak` | Single-exit cleanup and leak detection. |

## 9. Structs, unions, enums, and bitfields

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| Struct definition and member access | `10_aggregates/01_struct_basics` | `.` for values, `->` for pointers. |
| Nested structs | `10_aggregates/02_nested_structs` | Access through outer and inner members. |
| Padding and alignment | `10_aggregates/03_padding_alignment` | `offsetof`, `sizeof`, alignment requirements. |
| Bitfields | `10_aggregates/04_bitfields` | Packed flags and implementation-defined layout. |
| Unions | `10_aggregates/05_union` | Members share storage; size is at least the largest member. |
| Anonymous structs and unions | `18_advanced_c/08_anonymous_union` | Access anonymous members directly through the outer struct. |
| Enums | `10_aggregates/06_enum` | Named integer constants and validity checks. |
| `typedef` and designated initializers | `10_aggregates/07_typedef_designated` | Named field initialization. |
| `offsetof` and `container_of` | `10_aggregates/08_container_of` | Recover an outer object from a member pointer. |

## 10. Preprocessor

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| Object-like macros | `01_preprocessor/01_object_macro` | Text substitution before compilation. |
| Function-like macros | `01_preprocessor/02_function_macro` | Parenthesize parameters and the whole expansion. |
| Stringizing `#` | `01_preprocessor/03_stringize_paste` | Use a helper macro for expansion. |
| Token pasting `##` | `01_preprocessor/03_stringize_paste` | Build identifiers at preprocessing time. |
| Conditional compilation | `01_preprocessor/03_conditional_compilation`, `01_preprocessor/04_include_guards` | `#if`, `#ifdef`, `#ifndef`. |
| Include guards | `01_preprocessor/04_include_guards` | Prevent repeated declarations. |
| Variadic macros | `02_macros/04_variadic_macros` | `__VA_ARGS__` and variadic functions. |
| X-macros | `02_macros/05_x_macros` | Generate enums and string tables from one list. |
| `#error`, `#line`, `#pragma pack` | `01_preprocessor/05_pragma_error_line` | Diagnostics, line control, and packing. |
| Macros and macro hygiene | `02_macros/01`-`10` | Object-like macros, function-like macros, parentheses, `#`, `##`, variadic macros, X-macros, macro statements, macro-vs-typedef, macro side effects, `assert`. |

## 11. Standard library and I/O

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| Formatted output | `12_standard_library/01_printf_formats` | Match specifiers to argument types. |
| Formatted input | `00_basics/06_sscanf` | `sscanf`, return value, literal separators. |
| Numeric parsing | `12_standard_library/02_strtol_errno` | `strtol`, `errno`, `endptr`, range checks. |
| Sorting and searching | `12_standard_library/03_qsort_bsearch` | Comparison callbacks. |
| Math library | `12_standard_library/04_math_functions` | `hypot`, floating-point functions, `-lm`. |
| Time library | `12_standard_library/05_time_functions` | `time_t`, `difftime`. |
| Random numbers | `12_standard_library/06_random` | `srand`, `rand`, bounded ranges. |
| Text file I/O | `12_standard_library/07_file_io` | `fopen`, `fputs`, `fread`, `fclose`. |
| `ctype.h` | `03_types_variables/05_char_ascii` | Character classification. |
| `memcpy`, `memmove`, `memset`, `memcmp` | `12_standard_library/08_memory_functions` | Byte-oriented memory operations and overlap. |
| `strchr`, `strrchr`, `strstr` | `12_standard_library/09_string_search` | Character and substring search. |
| Fixed-width integers and format macros | `12_standard_library/10_stdint_inttypes` | `uint64_t`, `PRIu64`, `inttypes.h`. |
| Environment variables | `12_standard_library/11_environment` | `getenv`, `setenv`, and cleanup. |
| `errno` and error reporting | `12_standard_library/02_strtol_errno`, `12_standard_library/07_file_io` | Check return values and error state. |

## 12. Undefined behavior, safety, and portability

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| Signed integer overflow | `15_ub_safety/01_signed_overflow` | Undefined behavior; check before adding. |
| Uninitialized variables | `15_ub_safety/02_uninitialized` | Initialize every object before use. |
| Out-of-bounds access | `15_ub_safety/03_out_of_bounds`, `09_dynamic_memory/05_buffer_bounds` | Bounds are logical and allocated. |
| Use-after-free | `15_ub_safety/04_use_after_free`, `07_pointers/06_dangling_wild` | Clear pointers after `free`. |
| Double free | `09_dynamic_memory/04_memory_leak`, `15_ub_safety/04_use_after_free` | Ownership must be unambiguous. |
| Sequence points | `15_ub_safety/05_sequence_points` | Avoid unsequenced side effects. |
| Strict aliasing | `15_ub_safety/06_strict_aliasing` | Use `memcpy` for object representation. |
| Alignment | `15_ub_safety/07_alignment`, `18_advanced_c/07_align` | Misaligned access may be undefined or slow. |
| Null pointer dereference | `15_ub_safety/08_null_pointer` | Check before dereferencing. |
| Endianness and object representation | `07_pointers/05_void_pointer`, `15_ub_safety/06_strict_aliasing` | Byte-level operations make representation explicit. |

## 13. C11/C17 advanced features

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| Variadic functions | `18_advanced_c/01_variadic` | `stdarg.h`. |
| `setjmp` / `longjmp` | `18_advanced_c/02_setjmp_longjmp` | Non-local jumps and error handling. |
| POSIX threads | `18_advanced_c/03_pthreads` | `pthread_create`, `pthread_join`, mutexes. |
| C11 atomics | `18_advanced_c/04_atomics` | `atomic_int`, `atomic_fetch_add`, `atomic_load`. |
| `_Generic` | `18_advanced_c/05_generic` | Type-generic expression selection. |
| `_Static_assert` | `18_advanced_c/06_static_assert` | Compile-time invariants. |
| `alignof` / `alignas` | `18_advanced_c/07_align`, `15_ub_safety/07_alignment` | Alignment queries and requests. |
| `_Thread_local` | `18_advanced_c/09_thread_local` | Per-thread storage duration. |
| `_Complex` and `<complex.h>` | `18_advanced_c/10_complex` | Complex arithmetic and conjugate. |
| Signals and `sig_atomic_t` | `18_advanced_c/11_signal` | `signal`, `raise`, and asynchronous flags. |

## 14. Engineering habits

| Skill | Where it is practiced |
| --- | --- |
| Reading compiler diagnostics | Every exercise; especially `00_basics/09_compiler_diagnostics` |
| Writing small tests | Every exercise's `main` |
| Debugging with GDB | README, `make doctor`, `./clings watch` |
| Using sanitizers | README, `CFLAGS="-fsanitize=address,undefined"` |
| Memory checking | README, `valgrind` examples |
| Build reproducibility | `Makefile`, `CMakePresets.json`, `Dockerfile`, CI |
| Formatting and style | `.clang-format`, `.editorconfig`, `make format` |
| Keeping code and answers in sync | `tools/generate_exercises.py`, `--check` in CI |
