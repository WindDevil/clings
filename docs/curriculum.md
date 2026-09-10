# Curriculum and coverage map

This map connects each topic to the exercises that teach it.

Total exercises: **179** across **21** topics.

## 00_getting_started - Getting Started

| Exercise | Objective |
| --- | --- |
| `00_getting_started/01_hello_world` | Understand the minimal C program and formatted output. |
| `00_getting_started/02_compilation_model` | Include the standard header that declares INT_MAX. |
| `00_getting_started/03_main_args` | Work with the arguments passed to main. |
| `00_getting_started/04_debug_assert` | Use assert for programmer errors and return values for user errors. |
| `00_getting_started/05_compiler_diagnostics` | Fix a format-string warning that the compiler reports. |
| `00_getting_started/06_lexical_elements` | Recognize comments, backslash-newline continuation, and escape sequences. |
| `00_getting_started/07_main_return_value` | Return a defined success or failure status from a program. |
| `00_getting_started/08_standard_changes` | Detect the C standard version at compile time. |
| `00_getting_started/09_identifier_length` | Use long internal identifiers and rely on the standard minimum. |
| `00_getting_started/10_implementation_defined` | Observe implementation-defined char signedness and packing pragmas. |

## 01_types_variables - Types, Variables, and Storage

| Exercise | Objective |
| --- | --- |
| `01_types_variables/01_integer_types` | Use sizeof, CHAR_BIT, INT_MIN, and INT_MAX correctly. |
| `01_types_variables/02_signed_unsigned` | Avoid the usual arithmetic conversion trap when comparing. |
| `01_types_variables/03_overflow` | Understand modulo wrap and avoid signed integer overflow. |
| `01_types_variables/04_floating_point` | Compare floating-point values with an epsilon. |
| `01_types_variables/05_char_ascii` | Work with char values and the ctype classification functions. |
| `01_types_variables/06_storage_scope` | Observe the lifetime of a static variable and block scope. |
| `01_types_variables/07_qualifiers` | Use const, volatile, restrict, extern, auto, and register. |
| `01_types_variables/08_stdbool_stddef` | Use bool and size_t from the standard headers. |
| `01_types_variables/09_long_double` | Use long double and compare its precision with double. |
| `01_types_variables/10_octal_constants` | Recognize that a leading zero means base 8. |
| `01_types_variables/11_char_signedness` | Use signed char and unsigned char explicitly when the sign matters. |
| `01_types_variables/12_integer_promotions` | See that char operands are promoted to int in arithmetic expressions. |

## 02_operators - Operators and Expressions

| Exercise | Objective |
| --- | --- |
| `02_operators/01_arithmetic` | Practice integer division, modulo, and truncation. |
| `02_operators/02_precedence` | Use parentheses to express intent clearly. |
| `02_operators/03_short_circuit` | Observe that && and || may not evaluate their right operand. |
| `02_operators/04_bitwise` | Use masks and bitwise operators safely. |
| `02_operators/05_shifts` | Build masks and avoid shifting by the width of the type. |
| `02_operators/06_sizeof_incdec` | Distinguish sizeof expressions from increment side effects. |
| `02_operators/07_compound_assignment` | Use +=, -=, *=, /=, %= and the comma operator. |
| `02_operators/08_assignment_vs_equality` | Use == for comparison and recognize the = versus == trap. |
| `02_operators/09_maximal_munch` | Understand how the lexer greedily forms the longest token. |

## 03_control_flow - Control Flow

| Exercise | Objective |
| --- | --- |
| `03_control_flow/01_if_else` | Write clear conditional branches. |
| `03_control_flow/02_switch_case` | Use intentional fallthrough and a default case. |
| `03_control_flow/03_loops` | Get loop bounds and accumulators right. |
| `03_control_flow/04_break_continue` | Use break to stop early and continue to skip one iteration. |
| `03_control_flow/05_goto_cleanup` | Use goto for a clear cleanup path in C. |
| `03_control_flow/06_state_machine` | Track state while scanning a string. |
| `03_control_flow/07_while_do_while` | Distinguish entry-condition and exit-condition loops. |
| `03_control_flow/08_semicolon_pitfalls` | Avoid accidentally ending an if or loop with a semicolon. |
| `03_control_flow/09_dangling_else` | Use braces to make else bind to the intended if. |

## 04_functions - Functions and Scope

| Exercise | Objective |
| --- | --- |
| `04_functions/01_declaration_definition` | Use a forward declaration and an internal helper. |
| `04_functions/02_parameters_return` | Return values through parameters and clamp a range. |
| `04_functions/03_pass_by_pointer` | Modify caller-owned data through pointers. |
| `04_functions/04_recursion` | Write recursive functions with correct base cases. |
| `04_functions/05_static_inline` | Use static functions and file-scope state. |
| `04_functions/06_function_pointers` | Store functions in variables and choose one at runtime. |
| `04_functions/07_void_and_return` | Return early from a void function and return values from int functions. |
| `04_functions/08_tail_recursion` | Rewrite a recursive sum using an accumulator. |
| `04_functions/09_default_argument_promotions` | Use the promoted types expected by variadic functions. |

## 05_arrays_strings - Arrays and Strings

| Exercise | Objective |
| --- | --- |
| `05_arrays_strings/01_array_basics` | Iterate over an array and compute a sum and maximum. |
| `05_arrays_strings/02_array_decay` | See how an array parameter becomes a pointer. |
| `05_arrays_strings/03_multidimensional` | Transpose a 3x3 matrix with nested loops. |
| `05_arrays_strings/04_string_literals` | Scan a const string and modify a mutable char array. |
| `05_arrays_strings/05_string_ops` | Implement strlen, strcmp, and strcpy with pointers. |
| `05_arrays_strings/06_safe_format` | Format text into a fixed-size buffer without overflow. |
| `05_arrays_strings/07_tokenize` | Split a string without modifying the caller's buffer. |
| `05_arrays_strings/08_vla` | Create an array whose length is a runtime value. |
| `05_arrays_strings/09_compound_literals` | Create a temporary struct value with a compound literal. |
| `05_arrays_strings/10_pointer_compatibility` | Pass a non-const array through a pointer-to-const. |
| `05_arrays_strings/11_asymmetric_bounds` | Use the half-open interval [low, high). |

## 06_pointers - Pointers and Memory Layout

| Exercise | Objective |
| --- | --- |
| `06_pointers/01_pointer_basics` | Read and write through pointers. |
| `06_pointers/02_null_and_const` | Check for NULL and respect pointer-to-const. |
| `06_pointers/03_pointer_arithmetic` | Walk an array with pointers and return a pointer into it. |
| `06_pointers/04_pointer_to_pointer` | Let a function allocate and update a caller-owned pointer. |
| `06_pointers/05_void_pointer` | Use void pointers and unsigned char for type-agnostic code. |
| `06_pointers/06_dangling_wild` | Set a freed pointer to NULL to prevent accidental reuse. |
| `06_pointers/07_pointer_to_array` | Distinguish a pointer to an array from a pointer to its first element. |
| `06_pointers/08_null_empty_string` | Distinguish a null pointer, an empty string, and the NUL character. |
| `06_pointers/09_memory_location_zero` | Treat address zero as a null pointer, not as a valid object address. |
| `06_pointers/10_one_past_pointer` | Do not treat a pointer to a single object as an array. |
| `06_pointers/11_restrict_aliasing` | Use restrict to promise that two pointer parameters do not alias. |

## 07_dynamic_memory - Dynamic Memory and Data Structures

| Exercise | Objective |
| --- | --- |
| `07_dynamic_memory/01_malloc_free` | Use malloc and free for a dynamically sized array. |
| `07_dynamic_memory/02_calloc` | Use calloc when every byte must start as zero. |
| `07_dynamic_memory/03_realloc` | Use realloc safely and initialize only the new elements. |
| `07_dynamic_memory/04_memory_leak` | Pair every allocation with a matching free. |
| `07_dynamic_memory/05_buffer_bounds` | Copy at most dest_size - 1 bytes and always terminate. |
| `07_dynamic_memory/06_flexible_array` | Allocate a struct plus trailing data in one block. |
| `07_dynamic_memory/07_linked_list` | Build, traverse, and free a linked list. |
| `07_dynamic_memory/08_free_then_realloc` | Use realloc directly instead of freeing before growing an allocation. |
| `07_dynamic_memory/09_arena_allocator` | Implement a simple bump allocator with aligned allocations. |
| `07_dynamic_memory/10_allocation_stats` | Track outstanding allocations with wrapped malloc and free. |

## 08_structs_unions_enums - Structs, Unions, Enums, and Bitfields

| Exercise | Objective |
| --- | --- |
| `08_structs_unions_enums/01_struct_basics` | Create a struct value and access its members through a pointer. |
| `08_structs_unions_enums/02_nested_structs` | Access a nested member through an outer struct pointer. |
| `08_structs_unions_enums/03_padding_alignment` | Observe padding and member offsets with offsetof. |
| `08_structs_unions_enums/04_bitfields` | Store several small flags in one struct. |
| `08_structs_unions_enums/05_union` | Compare union size with the size of its largest member. |
| `08_structs_unions_enums/06_enum` | Use an enum for a small closed set of values. |
| `08_structs_unions_enums/07_typedef_designated` | Use a typedef and initialize members by name. |
| `08_structs_unions_enums/08_container_of` | Recover an outer struct from a pointer to one of its members. |
| `08_structs_unions_enums/09_struct_array` | Traverse an array of structs and find the best element. |
| `08_structs_unions_enums/10_struct_pass` | Compare struct value parameters with struct pointer parameters. |
| `08_structs_unions_enums/11_struct_file` | Store a struct with fwrite and read it back with fread. |
| `08_structs_unions_enums/12_complex_declarations` | Read and use a typedef for a function pointer and an array of function pointers. |
| `08_structs_unions_enums/13_declaration_grammar` | Read a typedef for an array of function pointers. |

## 09_preprocessor - Preprocessor Directives

| Exercise | Objective |
| --- | --- |
| `09_preprocessor/01_include_standard` | Include the standard header that declares fixed-width integer types. |
| `09_preprocessor/02_include_user` | Include a local header so its macro is visible. |
| `09_preprocessor/03_conditional_compilation` | Select code at preprocessing time based on the language version. |
| `09_preprocessor/04_include_guards` | Prevent multiple inclusion with a preprocessor guard. |
| `09_preprocessor/05_pragma_error_line` | Use diagnostics, line control, and packing pragmas. |
| `09_preprocessor/06_undef_defined` | Undefine a macro and test it with defined(). |

## 10_stdlib_io - Standard Library and File I/O

| Exercise | Objective |
| --- | --- |
| `10_stdlib_io/01_printf_formats` | Match each conversion specifier to its argument type. |
| `10_stdlib_io/02_scanf_parse` | Parse a comma-separated pair with sscanf. |
| `10_stdlib_io/03_strtol_errno` | Use strtol, errno, and the end pointer to validate input. |
| `10_stdlib_io/04_qsort_bsearch` | Use comparison callbacks for sorting and searching. |
| `10_stdlib_io/05_math_functions` | Use hypot and other functions from math.h. |
| `10_stdlib_io/06_time_functions` | Use time_t and difftime. |
| `10_stdlib_io/07_random` | Seed the generator and bound its output. |
| `10_stdlib_io/08_file_io` | Write and read a text file with fopen, fputs, and fread. |
| `10_stdlib_io/09_memory_functions` | Use the byte-oriented memory functions correctly. |
| `10_stdlib_io/10_string_search` | Use strchr, strrchr, and strstr. |
| `10_stdlib_io/11_stdint_inttypes` | Use uint64_t and PRIu64 from stdint.h and inttypes.h. |
| `10_stdlib_io/12_environment` | Read and write environment variables with getenv and setenv. |
| `10_stdlib_io/13_printf_advanced` | Use width, zero padding, precision, and the * width argument. |
| `10_stdlib_io/14_scanf_advanced` | Use field width and a scanset in sscanf. |
| `10_stdlib_io/15_ctype_full` | Use isalnum and toupper with unsigned char casts. |
| `10_stdlib_io/16_rand_max` | Do not assume rand() returns a value below a fixed small bound. |

## 11_ub_safety - Undefined Behavior, Safety, and Portability

| Exercise | Objective |
| --- | --- |
| `11_ub_safety/01_signed_overflow` | Detect overflow before performing signed addition. |
| `11_ub_safety/02_uninitialized` | Give every local variable a defined initial value. |
| `11_ub_safety/03_out_of_bounds` | Reject indices outside the logical array length. |
| `11_ub_safety/04_use_after_free` | Clear a pointer after freeing its target. |
| `11_ub_safety/05_sequence_points` | Avoid unsequenced reads and writes of the same object. |
| `11_ub_safety/06_strict_aliasing` | Reinterpret object representation with memcpy. |
| `11_ub_safety/07_alignment` | Query alignment with alignof and keep members aligned. |
| `11_ub_safety/08_null_pointer` | Never dereference a null pointer. |

## 12_advanced_c - Advanced C Features

| Exercise | Objective |
| --- | --- |
| `12_advanced_c/01_variadic` | Read a variable number of int arguments with va_list. |
| `12_advanced_c/02_setjmp_longjmp` | Use non-local jumps for a simple error path. |
| `12_advanced_c/03_pthreads` | Create threads and protect shared state with a mutex. |
| `12_advanced_c/04_atomics` | Use atomic_int for lock-free counter updates. |
| `12_advanced_c/05_generic` | Choose an expression based on the type of a value. |
| `12_advanced_c/06_static_assert` | Use _Static_assert to enforce assumptions at compile time. |
| `12_advanced_c/07_align` | Query and request alignment. |
| `12_advanced_c/08_anonymous_union` | Access anonymous union members directly through the outer struct. |
| `12_advanced_c/09_thread_local` | Use _Thread_local to give each thread its own object. |
| `12_advanced_c/10_complex` | Use double complex, I, conj, creal, and cimag. |
| `12_advanced_c/11_signal` | Install a signal handler and use a sig_atomic_t flag. |
| `12_advanced_c/12_stack_frame` | Observe that nested function calls use distinct activation records. |

## 13_translation_units - Translation Units, Headers, and Linkage

| Exercise | Objective |
| --- | --- |
| `13_translation_units/01_header_source_split` | Compile a program from a main file, a header, and an implementation file. |
| `13_translation_units/02_extern_linkage` | Declare a global variable in a header and define it in another file. |
| `13_translation_units/03_static_internal_linkage` | Keep a counter private to one translation unit with static. |
| `13_translation_units/04_external_type_check` | Keep declarations and definitions consistent across translation units. |
| `13_translation_units/05_dynamic_linking` | Load a symbol from a shared library at runtime. |

## 14_character_io - Character I/O and Input Validation

| Exercise | Objective |
| --- | --- |
| `14_character_io/01_getc_putc` | Copy a stream one character at a time with getc and putc. |
| `14_character_io/02_eof_ferror` | Read until EOF and distinguish end-of-file from an error. |
| `14_character_io/03_input_validation` | Reject input with trailing characters or out-of-range values. |
| `14_character_io/04_iso646` | Use and/or/not from iso646.h. |
| `14_character_io/05_getchar_putchar` | Use the standard input/output character macros directly. |

## 15_string_functions - String Functions and Conversion

| Exercise | Objective |
| --- | --- |
| `15_string_functions/01_strcat_strncat` | Append a string while respecting the destination size. |
| `15_string_functions/02_strncpy_bounded` | Copy a string safely and always terminate the destination. |
| `15_string_functions/03_sprintf_snprintf` | Format text with snprintf and understand truncation. |
| `15_string_functions/04_fgets_fputs_sort` | Read a line with fgets and sort an array of strings. |
| `15_string_functions/05_strtod` | Parse a double with strtod and reject trailing input. |

## 16_data_representation - Data Representation and Bit Operations

| Exercise | Objective |
| --- | --- |
| `16_data_representation/01_base_conversion` | Parse a hexadecimal string with strtoul. |
| `16_data_representation/02_integer_binary_representation` | Count set bits and convert sign-magnitude to two's complement. |
| `16_data_representation/03_float_binary_representation` | Inspect and reconstruct an IEEE-754 float with memcpy. |
| `16_data_representation/04_bitfield_portability` | Pack fields with bitfields and compare them with an explicit mask. |
| `16_data_representation/05_endianness` | Detect byte order and inspect an integer's first byte. |

## 17_data_structures - Abstract Data Types and Data Structures

| Exercise | Objective |
| --- | --- |
| `17_data_structures/01_queue_adt` | Implement a fixed-capacity circular queue. |
| `17_data_structures/02_binary_search_tree` | Insert into and search a binary search tree. |
| `17_data_structures/03_dynamic_vector` | Grow a dynamic array and preserve existing elements. |

## 18_file_io_advanced - Advanced File I/O

| Exercise | Objective |
| --- | --- |
| `18_file_io_advanced/01_fprintf_fscanf` | Write formatted data to a file and read it back. |
| `18_file_io_advanced/02_fgets_fputs` | Copy a text file line by line. |
| `18_file_io_advanced/03_getc_putc_ungetc` | Peek at a character and put it back into the stream. |
| `18_file_io_advanced/04_fseek_ftell` | Seek to a byte offset and report the resulting position. |
| `18_file_io_advanced/05_fflush_setvbuf` | Configure full buffering and flush a stream. |
| `18_file_io_advanced/06_binary_random_access` | Read a specific struct record from a binary file. |
| `18_file_io_advanced/07_buffered_output_memory` | Combine malloc, setvbuf, output, fclose, and free. |

## 19_modern_c_library - Modern C Library and Language Features

| Exercise | Objective |
| --- | --- |
| `19_modern_c_library/01_noreturn` | Declare a function that never returns and observe its exit status. |
| `19_modern_c_library/02_tgmath` | Use sqrt with both double and float arguments through tgmath.h. |
| `19_modern_c_library/03_atexit` | Register a cleanup function with atexit. |
| `19_modern_c_library/04_atomic_flag` | Use atomic_flag as a simple test-and-set lock. |

## 20_macros - Macros and Macro Hygiene

| Exercise | Objective |
| --- | --- |
| `20_macros/01_object_macro` | Use a named compile-time constant. |
| `20_macros/02_function_macro` | Protect macro arguments and the whole expansion with parentheses. |
| `20_macros/03_stringize_paste` | Use # to stringize and ## to paste tokens. |
| `20_macros/04_variadic_macros` | Forward a variable argument list to a variadic function. |
| `20_macros/05_x_macros` | Generate an enum and a string table from one list. |
| `20_macros/06_macro_whitespace` | Remember that a space can turn a function-like macro into an object-like macro. |
| `20_macros/07_macro_statement` | Use do { ... } while (0) for a statement-like macro. |
| `20_macros/08_macro_not_typedef` | Use typedef instead of an object-like macro for pointer types. |
| `20_macros/09_macro_side_effects` | See that a function-like macro can evaluate its argument more than once. |

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
