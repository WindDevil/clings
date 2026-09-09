# C knowledge coverage map

This map is organized by C language and systems-programming knowledge areas.
Every row points to at least one exercise.

## 1. Program structure, translation, and tooling

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| Minimal C program, `main`, return value | `00_getting_started/01_hello_world`, `00_getting_started/03_main_args` | A C program is a collection of declarations and definitions. |
| Preprocessing, compiling, assembling, linking | `00_getting_started/02_compilation_model` | `__STDC__`, `__STDC_VERSION__`, conditional compilation. |
| `argc`, `argv`, program environment | `00_getting_started/03_main_args` | `argv[0]` is the program name; arguments start at `argv[1]`. |
| Assertions and defensive checks | `00_getting_started/04_debug_assert` | `assert` for programmer errors; return codes for recoverable errors. |
| Reading compiler diagnostics | `00_getting_started/05_compiler_diagnostics`, `10_stdlib_io/01_printf_formats` | Format-string diagnostics, `-Wformat`, `-Werror`. |
| Build systems and project layout | README, `Makefile`, `CMakeLists.txt`, `CMakePresets.json` | CLI, Make, CMake, CTest, Docker. |
| Testing workflow | `./clings verify`, `./clings selftest`, `include/clings/test.h` | Dependency-free assertion harness. |

## 2. Lexical elements, types, and objects

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| Comments, identifiers, keywords | all exercises | Lexical and keyword usage across the exercises. |
| Comments, line continuation, escapes | `00_getting_started/06_lexical_elements` | `/* ... */`, backslash-newline, `\n`, `\t`, `\"`. |
| Character constants and string literals | `01_types_variables/05_char_ascii`, `05_arrays_strings/04_string_literals` | `char`, ASCII, mutable arrays vs immutable literals. |
| Integer types and ranges | `01_types_variables/01_integer_types` | `sizeof`, `CHAR_BIT`, `INT_MIN`, `INT_MAX`. |
| Signed and unsigned | `01_types_variables/02_signed_unsigned`, `11_ub_safety/01_signed_overflow` | Usual arithmetic conversions and overflow. |
| Integer overflow and wraparound | `01_types_variables/03_overflow`, `11_ub_safety/01_signed_overflow` | Unsigned wraps; signed overflow is undefined behavior. |
| Floating-point types | `01_types_variables/04_floating_point` | Epsilon comparison, `fabs`, representation limits. |
| Character classification | `01_types_variables/05_char_ascii` | ASCII assumptions and portable `ctype.h` usage. |
| `const`, `enum`, `#define` constants | `01_types_variables/06_storage_scope`, `09_preprocessor/01_object_macro`, `08_structs_unions_enums/06_enum` | Three ways to express named constants. |
| `auto`, `register`, `static`, scope, lifetime | `01_types_variables/06_storage_scope`, `04_functions/05_static_inline` | File scope, block scope, static storage duration. |
| `const`, `volatile`, `restrict`, `extern`, `auto`, `register` | `01_types_variables/07_qualifiers` | Type qualifiers and storage-class specifiers. |
| `stdbool.h` and `stddef.h` | `01_types_variables/08_stdbool_stddef` | `bool`, `size_t`, and standard typedefs. |
| `typedef` and type aliases | `08_structs_unions_enums/07_typedef_designated` | `typedef` is not a macro. |
| `sizeof` and object size | `02_operators/06_sizeof_incdec`, `08_structs_unions_enums/03_padding_alignment` | `sizeof` is an operator, not a function. |

## 3. Expressions and operators

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| Arithmetic operators | `02_operators/01_arithmetic` | Integer division truncates toward zero; `%` is remainder. |
| Precedence and associativity | `02_operators/02_precedence` | Parentheses document intent and prevent surprises. |
| Logical operators and short-circuiting | `02_operators/03_short_circuit` | `&&` and `||` may skip the right operand. |
| Bitwise operators | `02_operators/04_bitwise`, `02_operators/05_shifts` | Set, clear, toggle, test, masks. |
| Shift operators and undefined behavior | `02_operators/05_shifts`, `11_ub_safety/05_sequence_points` | Shifting by the type width is undefined. |
| `sizeof` and increment/decrement | `02_operators/06_sizeof_incdec` | Post-increment vs pre-increment; `sizeof` does not evaluate its operand (except VLAs). |
| Conditional operator | `03_control_flow/01_if_else` | `a ? b : c` selects one expression. |
| Sequence points and side effects | `11_ub_safety/05_sequence_points` | Avoid unsequenced reads/writes of the same object. |
| Conversions and casts | `01_types_variables/02_signed_unsigned`, `11_ub_safety/06_strict_aliasing` | Explicit casts do not make undefined behavior defined. |

## 4. Control flow

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| `if`, `else`, nested conditions | `03_control_flow/01_if_else` | Compare booleans, floating values, and pointers correctly. |
| `switch`, `case`, `default`, fallthrough | `03_control_flow/02_switch_case` | Intentional fallthrough should be visible. |
| `for`, `while`, `do-while` | `03_control_flow/03_loops` | Loop bounds and accumulator initialization. |
| `break` and `continue` | `03_control_flow/04_break_continue` | Early exit vs skipping one iteration. |
| `goto` and single-exit cleanup | `03_control_flow/05_goto_cleanup` | A common C resource-cleanup pattern. |
| State machines | `03_control_flow/06_state_machine` | Track a small amount of state while scanning input. |

## 5. Functions, linkage, and scope

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| Declarations and definitions | `04_functions/01_declaration_definition` | A prototype and a definition can be separated. |
| Parameters and return values | `04_functions/02_parameters_return` | Output parameters, `void`, and range clamping. |
| Pass by value vs pass by pointer | `04_functions/03_pass_by_pointer` | C passes everything by value; pointers let you modify caller storage. |
| Recursion and base cases | `04_functions/04_recursion` | Factorial and Fibonacci. |
| Internal linkage, `static`, `inline` | `04_functions/05_static_inline` | File-scope state and helper functions. |
| Function pointers and callbacks | `04_functions/06_function_pointers`, `10_stdlib_io/04_qsort_bsearch` | Dispatch tables and `qsort` comparators. |
| Variadic functions | `12_advanced_c/01_variadic`, `09_preprocessor/06_variadic_macros` | `stdarg.h`, `va_list`, variadic macros. |
| Non-local jumps | `12_advanced_c/02_setjmp_longjmp` | `setjmp`/`longjmp` error paths. |
| `void` functions and `return` | `04_functions/07_void_and_return` | Bare `return;`, early return, and value return. |

## 6. Arrays and strings

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| Array declaration, indexing, traversal | `05_arrays_strings/01_array_basics` | Contiguous objects and bounds. |
| Array-to-pointer decay | `05_arrays_strings/02_array_decay` | An array parameter is a pointer parameter. |
| Multidimensional arrays | `05_arrays_strings/03_multidimensional` | Row-major layout and nested indexing. |
| String literals vs `char` arrays | `05_arrays_strings/04_string_literals` | Literals are not modifiable; arrays are. |
| `strlen`, `strcmp`, `strcpy` | `05_arrays_strings/05_string_ops` | Reimplement the classic pointer algorithms. |
| Bounded formatting | `05_arrays_strings/06_safe_format` | `snprintf` returns the full length even when truncated. |
| Tokenization | `05_arrays_strings/07_tokenize` | `strtok_r` and non-destructive splitting. |
| Buffer bounds | `07_dynamic_memory/05_buffer_bounds` | Always reserve space for the terminating NUL. |

## 7. Pointers and the object model

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| Address-of and dereference | `06_pointers/01_pointer_basics` | `&` and `*`; writing through a pointer. |
| `NULL` and pointer checks | `06_pointers/02_null_and_const`, `11_ub_safety/08_null_pointer` | Never dereference a null pointer. |
| Pointer arithmetic | `06_pointers/03_pointer_arithmetic` | `p + n` moves by `n` elements, not bytes. |
| Pointers to pointers | `06_pointers/04_pointer_to_pointer` | Allocating and updating caller-owned pointers. |
| `void *` and generic byte access | `06_pointers/05_void_pointer` | Byte-wise swap with `unsigned char *`. |
| Dangling and wild pointers | `06_pointers/06_dangling_wild`, `11_ub_safety/04_use_after_free` | Set pointers to `NULL` after `free`. |
| Pointer-to-`const` vs `const` pointer | `06_pointers/02_null_and_const` | Read-only pointed-to data. |
| Array/pointer equivalence and limits | `05_arrays_strings/02_array_decay`, `05_arrays_strings/03_multidimensional` | `sizeof` differs for arrays and pointers. |
| Pointers to arrays, `a` vs `&a` | `06_pointers/07_pointer_to_array` | `int (*)[4]` advances by a whole row/array. |
| Strict aliasing | `11_ub_safety/06_strict_aliasing` | Use `memcpy` for type punning. |
| Alignment | `11_ub_safety/07_alignment`, `12_advanced_c/07_align` | `alignof`, `alignas`, padding. |

## 8. Dynamic memory and data structures

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| `malloc` and `free` | `07_dynamic_memory/01_malloc_free` | Allocate, initialize, release. |
| `calloc` | `07_dynamic_memory/02_calloc` | Zero-initialized allocation. |
| `realloc` | `07_dynamic_memory/03_realloc` | Grow while preserving existing elements. |
| Memory leaks | `07_dynamic_memory/04_memory_leak` | Track allocations and free every path. |
| Buffer bounds | `07_dynamic_memory/05_buffer_bounds` | Logical bounds vs allocated size. |
| Flexible array members | `07_dynamic_memory/06_flexible_array` | One allocation for a header plus payload. |
| Linked lists | `07_dynamic_memory/07_linked_list` | Nodes, traversal, and full cleanup. |
| Ownership and cleanup paths | `03_control_flow/05_goto_cleanup`, `07_dynamic_memory/04_memory_leak` | Single-exit cleanup and leak detection. |

## 9. Structs, unions, enums, and bitfields

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| Struct definition and member access | `08_structs_unions_enums/01_struct_basics` | `.` for values, `->` for pointers. |
| Nested structs | `08_structs_unions_enums/02_nested_structs` | Access through outer and inner members. |
| Padding and alignment | `08_structs_unions_enums/03_padding_alignment` | `offsetof`, `sizeof`, alignment requirements. |
| Bitfields | `08_structs_unions_enums/04_bitfields` | Packed flags and implementation-defined layout. |
| Unions | `08_structs_unions_enums/05_union` | Members share storage; size is at least the largest member. |
| Anonymous structs and unions | `12_advanced_c/08_anonymous_union` | Access anonymous members directly through the outer struct. |
| Enums | `08_structs_unions_enums/06_enum` | Named integer constants and validity checks. |
| `typedef` and designated initializers | `08_structs_unions_enums/07_typedef_designated` | Named field initialization. |
| `offsetof` and `container_of` | `08_structs_unions_enums/08_container_of` | Recover an outer object from a member pointer. |

## 10. Preprocessor

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| Object-like macros | `09_preprocessor/01_object_macro` | Text substitution before compilation. |
| Function-like macros | `09_preprocessor/02_function_macro` | Parenthesize parameters and the whole expansion. |
| Stringizing `#` | `09_preprocessor/03_stringize_paste` | Use a helper macro for expansion. |
| Token pasting `##` | `09_preprocessor/03_stringize_paste` | Build identifiers at preprocessing time. |
| Conditional compilation | `09_preprocessor/04_conditional_compilation`, `00_getting_started/02_compilation_model` | `#if`, `#ifdef`, `__STDC_VERSION__`. |
| Include guards | `09_preprocessor/05_include_guards` | Prevent repeated declarations. |
| Variadic macros | `09_preprocessor/06_variadic_macros` | `__VA_ARGS__` and variadic functions. |
| X-macros | `09_preprocessor/07_x_macros` | Generate enums and string tables from one list. |
| `#error`, `#line`, `#pragma pack` | `09_preprocessor/08_pragma_error_line` | Diagnostics, line control, and packing. |
| Predefined macros | `09_preprocessor/09_std_macros` | `__FILE__`, `__LINE__`, `__func__`, `__STDC_VERSION__`. |

## 11. Standard library and I/O

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| Formatted output | `10_stdlib_io/01_printf_formats` | Match specifiers to argument types. |
| Formatted input | `10_stdlib_io/02_scanf_parse` | `sscanf`, return value, literal separators. |
| Numeric parsing | `10_stdlib_io/03_strtol_errno` | `strtol`, `errno`, `endptr`, range checks. |
| Sorting and searching | `10_stdlib_io/04_qsort_bsearch` | Comparison callbacks. |
| Math library | `10_stdlib_io/05_math_functions` | `hypot`, floating-point functions, `-lm`. |
| Time library | `10_stdlib_io/06_time_functions` | `time_t`, `difftime`. |
| Random numbers | `10_stdlib_io/07_random` | `srand`, `rand`, bounded ranges. |
| Text file I/O | `10_stdlib_io/08_file_io` | `fopen`, `fputs`, `fread`, `fclose`. |
| `ctype.h` | `01_types_variables/05_char_ascii` | Character classification. |
| `memcpy`, `memmove`, `memset`, `memcmp` | `10_stdlib_io/09_memory_functions` | Byte-oriented memory operations and overlap. |
| `strchr`, `strrchr`, `strstr` | `10_stdlib_io/10_string_search` | Character and substring search. |
| Fixed-width integers and format macros | `10_stdlib_io/11_stdint_inttypes` | `uint64_t`, `PRIu64`, `inttypes.h`. |
| Environment variables | `10_stdlib_io/12_environment` | `getenv`, `setenv`, and cleanup. |
| `errno` and error reporting | `10_stdlib_io/03_strtol_errno`, `10_stdlib_io/08_file_io` | Check return values and error state. |

## 12. Undefined behavior, safety, and portability

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| Signed integer overflow | `11_ub_safety/01_signed_overflow` | Undefined behavior; check before adding. |
| Uninitialized variables | `11_ub_safety/02_uninitialized` | Initialize every object before use. |
| Out-of-bounds access | `11_ub_safety/03_out_of_bounds`, `07_dynamic_memory/05_buffer_bounds` | Bounds are logical and allocated. |
| Use-after-free | `11_ub_safety/04_use_after_free`, `06_pointers/06_dangling_wild` | Clear pointers after `free`. |
| Double free | `07_dynamic_memory/04_memory_leak`, `11_ub_safety/04_use_after_free` | Ownership must be unambiguous. |
| Sequence points | `11_ub_safety/05_sequence_points` | Avoid unsequenced side effects. |
| Strict aliasing | `11_ub_safety/06_strict_aliasing` | Use `memcpy` for object representation. |
| Alignment | `11_ub_safety/07_alignment`, `12_advanced_c/07_align` | Misaligned access may be undefined or slow. |
| Null pointer dereference | `11_ub_safety/08_null_pointer` | Check before dereferencing. |
| Endianness and object representation | `06_pointers/05_void_pointer`, `11_ub_safety/06_strict_aliasing` | Byte-level operations make representation explicit. |

## 13. C11/C17 advanced features

| Knowledge point | Exercises | Notes |
| --- | --- | --- |
| Variadic functions | `12_advanced_c/01_variadic` | `stdarg.h`. |
| `setjmp` / `longjmp` | `12_advanced_c/02_setjmp_longjmp` | Non-local jumps and error handling. |
| POSIX threads | `12_advanced_c/03_pthreads` | `pthread_create`, `pthread_join`, mutexes. |
| C11 atomics | `12_advanced_c/04_atomics` | `atomic_int`, `atomic_fetch_add`, `atomic_load`. |
| `_Generic` | `12_advanced_c/05_generic` | Type-generic expression selection. |
| `_Static_assert` | `12_advanced_c/06_static_assert` | Compile-time invariants. |
| `alignof` / `alignas` | `12_advanced_c/07_align`, `11_ub_safety/07_alignment` | Alignment queries and requests. |
| `_Thread_local` | `12_advanced_c/09_thread_local` | Per-thread storage duration. |
| `_Complex` and `<complex.h>` | `12_advanced_c/10_complex` | Complex arithmetic and conjugate. |
| Signals and `sig_atomic_t` | `12_advanced_c/11_signal` | `signal`, `raise`, and asynchronous flags. |

## 14. Engineering habits

| Skill | Where it is practiced |
| --- | --- |
| Reading compiler diagnostics | Every exercise; especially `00_getting_started/05_compiler_diagnostics` |
| Writing small tests | Every exercise's `main` |
| Debugging with GDB | README, `make doctor`, `./clings watch` |
| Using sanitizers | README, `CFLAGS="-fsanitize=address,undefined"` |
| Memory checking | README, `valgrind` examples |
| Build reproducibility | `Makefile`, `CMakePresets.json`, `Dockerfile`, CI |
| Formatting and style | `.clang-format`, `.editorconfig`, `make format` |
| Keeping code and answers in sync | `tools/generate_exercises.py`, `--check` in CI |
