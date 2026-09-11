# Curriculum and coverage map

This map connects each topic to the exercises that teach it.

Total exercises: **185** across **20** topics.

## 00_basics - Basics

| Exercise | Objective |
| --- | --- |
| `00_basics/01_printf` | Use printf to print a line of text. |
| `00_basics/02_printf_values` | Use printf with %d to print an integer value. |
| `00_basics/03_scanf` | Read an integer from stdin with scanf. |
| `00_basics/04_char_array` | Store text in a char array and access its characters. |
| `00_basics/05_snprintf` | Write formatted text into a fixed-size buffer. |
| `00_basics/06_sscanf` | Parse values from a string with sscanf. |
| `00_basics/07_include_header` | Include the standard header that declares printf. |
| `00_basics/08_lexical_elements` | Use comments and escape sequences correctly. |
| `00_basics/09_compiler_diagnostics` | Fix a format-string warning that the compiler reports. |

## 01_preprocessor - Preprocessor Directives

| Exercise | Objective |
| --- | --- |
| `01_preprocessor/01_include_standard` | Include the standard header that declares fixed-width integer types. |
| `01_preprocessor/02_include_user` | Include a local header so its macro is visible. |
| `01_preprocessor/03_conditional_compilation` | Select code at preprocessing time based on the language version. |
| `01_preprocessor/04_include_guards` | Prevent multiple inclusion with a preprocessor guard. |
| `01_preprocessor/05_pragma_error_line` | Use diagnostics, line control, and packing pragmas. |
| `01_preprocessor/06_undef_defined` | Undefine a macro and test it with defined(). |

## 02_macros - Macros and Macro Hygiene

| Exercise | Objective |
| --- | --- |
| `02_macros/01_object_macro` | Use a named compile-time constant. |
| `02_macros/02_function_macro` | Protect macro arguments and the whole expansion with parentheses. |
| `02_macros/03_stringize_paste` | Use # to stringize and ## to paste tokens. |
| `02_macros/04_variadic_macros` | Forward a variable argument list to a variadic function. |
| `02_macros/05_x_macros` | Generate an enum and a string table from one list. |
| `02_macros/06_macro_whitespace` | Remember that a space can turn a function-like macro into an object-like macro. |
| `02_macros/07_macro_statement` | Use do { ... } while (0) for a statement-like macro. |
| `02_macros/08_macro_not_typedef` | Use typedef instead of an object-like macro for pointer types. |
| `02_macros/09_macro_side_effects` | See that a function-like macro can evaluate its argument more than once. |
| `02_macros/10_assert_macro` | Use assert for programmer errors and return values for user errors. |
| `02_macros/11_macro_multiline` | Continue a macro definition onto the next line. |

## 03_types_variables - Types, Variables, and Storage

| Exercise | Objective |
| --- | --- |
| `03_types_variables/01_integer_types` | Use sizeof, CHAR_BIT, INT_MIN, and INT_MAX correctly. |
| `03_types_variables/02_signed_unsigned` | Avoid the usual arithmetic conversion trap when comparing. |
| `03_types_variables/03_overflow` | Understand modulo wrap and avoid signed integer overflow. |
| `03_types_variables/04_floating_point` | Compare floating-point values with an epsilon. |
| `03_types_variables/05_char_ascii` | Work with char values and the ctype classification functions. |
| `03_types_variables/06_storage_scope` | Observe the lifetime of a static variable and block scope. |
| `03_types_variables/07_qualifiers` | Use const, volatile, extern, auto, and register. |
| `03_types_variables/08_stdbool_stddef` | Use bool and size_t from the standard headers. |
| `03_types_variables/09_long_double` | Use long double and compare its precision with double. |
| `03_types_variables/10_octal_constants` | Recognize that a leading zero means base 8. |
| `03_types_variables/11_char_signedness` | Use signed char and unsigned char explicitly when the sign matters. |
| `03_types_variables/12_integer_promotions` | See that char operands are promoted to int in arithmetic expressions. |

## 04_operators - Operators and Expressions

| Exercise | Objective |
| --- | --- |
| `04_operators/01_arithmetic` | Practice integer division, modulo, and truncation. |
| `04_operators/02_precedence` | Use parentheses to express intent clearly. |
| `04_operators/03_short_circuit` | Observe that && and || may not evaluate their right operand. |
| `04_operators/04_bitwise` | Use masks and bitwise operators safely. |
| `04_operators/05_shifts` | Build masks and avoid shifting by the width of the type. |
| `04_operators/06_sizeof_incdec` | Distinguish sizeof expressions from increment side effects. |
| `04_operators/07_compound_assignment` | Use +=, -=, *=, /=, %= and the comma operator. |
| `04_operators/08_assignment_vs_equality` | Use == for comparison and recognize the = versus == trap. |
| `04_operators/09_maximal_munch` | Understand how the lexer greedily forms the longest token. |

## 05_control_flow - Control Flow

| Exercise | Objective |
| --- | --- |
| `05_control_flow/01_if_else` | Write clear conditional branches. |
| `05_control_flow/02_switch_case` | Use intentional fallthrough and a default case. |
| `05_control_flow/03_loops` | Get loop bounds and accumulators right. |
| `05_control_flow/04_break_continue` | Use break to stop early and continue to skip one iteration. |
| `05_control_flow/05_while_do_while` | Distinguish entry-condition and exit-condition loops. |
| `05_control_flow/06_semicolon_pitfalls` | Avoid accidentally ending an if or loop with a semicolon. |
| `05_control_flow/07_dangling_else` | Use braces to make else bind to the intended if. |

## 06_functions - Functions and Scope

| Exercise | Objective |
| --- | --- |
| `06_functions/01_declaration_definition` | Use a forward declaration and an internal helper. |
| `06_functions/02_parameters_return` | Return values through parameters and clamp a range. |
| `06_functions/03_recursion` | Write recursive functions with correct base cases. |
| `06_functions/04_static_inline` | Use static functions and file-scope state. |
| `06_functions/05_void_and_return` | Return early from a void function and return values from int functions. |
| `06_functions/06_tail_recursion` | Rewrite a recursive sum using an accumulator. |
| `06_functions/07_main_return_value` | Return a defined success or failure status from a program. |

## 07_pointers - Pointers

| Exercise | Objective |
| --- | --- |
| `07_pointers/01_pointer_basics` | Read and write through pointers. |
| `07_pointers/02_null_and_const` | Check for NULL and respect pointer-to-const. |
| `07_pointers/03_pointer_arithmetic` | Walk an array with pointers and return a pointer into it. |
| `07_pointers/04_pointer_to_pointer` | Let a function allocate and update a caller-owned pointer. |
| `07_pointers/05_void_pointer` | Use void pointers and unsigned char for type-agnostic code. |
| `07_pointers/06_dangling_wild` | Set a freed pointer to NULL to prevent accidental reuse. |
| `07_pointers/07_pointer_to_array` | Distinguish a pointer to an array from a pointer to its first element. |
| `07_pointers/08_null_empty_string` | Distinguish a null pointer, an empty string, and the NUL character. |
| `07_pointers/09_memory_location_zero` | Treat address zero as a null pointer, not as a valid object address. |
| `07_pointers/10_one_past_pointer` | Do not treat a pointer to a single object as an array. |
| `07_pointers/11_restrict_aliasing` | Use restrict to promise that two pointer parameters do not alias. |
| `07_pointers/12_pass_by_pointer` | Modify caller-owned data through pointers. |
| `07_pointers/13_function_pointers` | Store functions in variables and choose one at runtime. |

## 08_arrays_strings - Arrays and Strings

| Exercise | Objective |
| --- | --- |
| `08_arrays_strings/01_array_basics` | Iterate over an array and compute a sum and maximum. |
| `08_arrays_strings/02_array_decay` | See how an array parameter becomes a pointer. |
| `08_arrays_strings/03_multidimensional` | Transpose a 3x3 matrix with nested loops. |
| `08_arrays_strings/04_string_literals` | Scan a const string and modify a mutable char array. |
| `08_arrays_strings/05_string_ops` | Implement strlen, strcmp, and strcpy with pointers. |
| `08_arrays_strings/06_tokenize` | Split a string without modifying the caller's buffer. |
| `08_arrays_strings/07_vla` | Create an array whose length is a runtime value. |
| `08_arrays_strings/08_compound_literals` | Create a temporary struct value with a compound literal. |
| `08_arrays_strings/09_pointer_compatibility` | Pass a non-const array through a pointer-to-const. |
| `08_arrays_strings/10_asymmetric_bounds` | Use the half-open interval [low, high). |
| `08_arrays_strings/11_strcat_strncat` | Append a string while respecting the destination size. |
| `08_arrays_strings/12_strncpy_bounded` | Copy a string safely and always terminate the destination. |
| `08_arrays_strings/13_sprintf_snprintf` | Format text with snprintf and understand truncation. |
| `08_arrays_strings/14_fgets_fputs_sort` | Read a line with fgets and sort an array of strings. |
| `08_arrays_strings/15_strtod` | Parse a double with strtod and reject trailing input. |
| `08_arrays_strings/16_main_args` | Work with the arguments passed to main. |
| `08_arrays_strings/17_state_machine` | Track state while scanning a string. |
| `08_arrays_strings/18_escaped_strings` | Use escape sequences inside a string literal and continue lines explicitly. |

## 09_dynamic_memory - Dynamic Memory

| Exercise | Objective |
| --- | --- |
| `09_dynamic_memory/01_malloc_free` | Use malloc and free for a dynamically sized array. |
| `09_dynamic_memory/02_calloc` | Use calloc when every byte must start as zero. |
| `09_dynamic_memory/03_realloc` | Use realloc safely and initialize only the new elements. |
| `09_dynamic_memory/04_memory_leak` | Pair every allocation with a matching free. |
| `09_dynamic_memory/05_buffer_bounds` | Copy at most dest_size - 1 bytes and always terminate. |
| `09_dynamic_memory/06_flexible_array` | Allocate a struct plus trailing data in one block. |
| `09_dynamic_memory/07_linked_list` | Build, traverse, and free a linked list. |
| `09_dynamic_memory/08_free_then_realloc` | Use realloc directly instead of freeing before growing an allocation. |
| `09_dynamic_memory/09_arena_allocator` | Implement a simple bump allocator with aligned allocations. |
| `09_dynamic_memory/10_allocation_stats` | Track outstanding allocations with wrapped malloc and free. |
| `09_dynamic_memory/11_goto_cleanup` | Use goto for a clear cleanup path in C. |

## 10_aggregates - Structs, Unions, Enums, and Bitfields

| Exercise | Objective |
| --- | --- |
| `10_aggregates/01_struct_basics` | Create a struct value and access its members through a pointer. |
| `10_aggregates/02_nested_structs` | Access a nested member through an outer struct pointer. |
| `10_aggregates/03_padding_alignment` | Observe padding and member offsets with offsetof. |
| `10_aggregates/04_bitfields` | Store several small flags in one struct. |
| `10_aggregates/05_union` | Compare union size with the size of its largest member. |
| `10_aggregates/06_enum` | Use an enum for a small closed set of values. |
| `10_aggregates/07_typedef_designated` | Use a typedef and initialize members by name. |
| `10_aggregates/08_container_of` | Recover an outer struct from a pointer to one of its members. |
| `10_aggregates/09_struct_array` | Traverse an array of structs and find the best element. |
| `10_aggregates/10_struct_pass` | Compare struct value parameters with struct pointer parameters. |
| `10_aggregates/11_struct_file` | Store a struct with fwrite and read it back with fread. |
| `10_aggregates/12_complex_declarations` | Read and use a typedef for a function pointer and an array of function pointers. |
| `10_aggregates/13_declaration_grammar` | Read a typedef for an array of function pointers. |

## 11_data_representation - Data Representation

| Exercise | Objective |
| --- | --- |
| `11_data_representation/01_base_conversion` | Parse a hexadecimal string with strtoul. |
| `11_data_representation/02_integer_binary_representation` | Count set bits and convert sign-magnitude to two's complement. |
| `11_data_representation/03_float_binary_representation` | Inspect and reconstruct an IEEE-754 float with memcpy. |
| `11_data_representation/04_bitfield_portability` | Pack fields with bitfields and compare them with an explicit mask. |
| `11_data_representation/05_endianness` | Detect byte order and inspect an integer's first byte. |

## 12_standard_library - Standard Library

| Exercise | Objective |
| --- | --- |
| `12_standard_library/01_printf_formats` | Match each conversion specifier to its argument type. |
| `12_standard_library/02_strtol_errno` | Use strtol, errno, and the end pointer to validate input. |
| `12_standard_library/03_qsort_bsearch` | Use comparison callbacks for sorting and searching. |
| `12_standard_library/04_math_functions` | Use hypot and other functions from math.h. |
| `12_standard_library/05_time_functions` | Use time_t and difftime. |
| `12_standard_library/06_random` | Seed the generator and bound its output. |
| `12_standard_library/07_file_io` | Write and read a text file with fopen, fputs, and fread. |
| `12_standard_library/08_memory_functions` | Use the byte-oriented memory functions correctly. |
| `12_standard_library/09_string_search` | Use strchr, strrchr, and strstr. |
| `12_standard_library/10_stdint_inttypes` | Use uint64_t and PRIu64 from stdint.h and inttypes.h. |
| `12_standard_library/11_environment` | Read and write environment variables with getenv and setenv. |
| `12_standard_library/12_printf_advanced` | Use width, zero padding, precision, and the * width argument. |
| `12_standard_library/13_scanf_advanced` | Use field width and a scanset in sscanf. |
| `12_standard_library/14_ctype_full` | Use isalnum and toupper with unsigned char casts. |
| `12_standard_library/15_rand_max` | Do not assume rand() returns a value below a fixed small bound. |
| `12_standard_library/16_default_argument_promotions` | Use the promoted types expected by variadic functions. |

## 13_character_io - Character I/O

| Exercise | Objective |
| --- | --- |
| `13_character_io/01_getc_putc` | Copy a stream one character at a time with getc and putc. |
| `13_character_io/02_eof_ferror` | Read until EOF and distinguish end-of-file from an error. |
| `13_character_io/03_input_validation` | Reject input with trailing characters or out-of-range values. |
| `13_character_io/04_iso646` | Use and/or/not from iso646.h. |
| `13_character_io/05_getchar_putchar` | Use the standard input/output character macros directly. |
| `13_character_io/06_include_ctypes` | Call toupper after including the header that declares it. |

## 14_file_io - File I/O

| Exercise | Objective |
| --- | --- |
| `14_file_io/01_fprintf_fscanf` | Write formatted data to a file and read it back. |
| `14_file_io/02_fgets_fputs` | Copy a text file line by line. |
| `14_file_io/03_getc_putc_ungetc` | Peek at a character and put it back into the stream. |
| `14_file_io/04_fseek_ftell` | Seek to a byte offset and report the resulting position. |
| `14_file_io/05_fflush_setvbuf` | Configure full buffering and flush a stream. |
| `14_file_io/06_binary_random_access` | Read a specific struct record from a binary file. |
| `14_file_io/07_buffered_output_memory` | Combine malloc, setvbuf, output, fclose, and free. |

## 15_ub_safety - Undefined Behavior, Safety, and Portability

| Exercise | Objective |
| --- | --- |
| `15_ub_safety/01_signed_overflow` | Detect overflow before performing signed addition. |
| `15_ub_safety/02_uninitialized` | Give every local variable a defined initial value. |
| `15_ub_safety/03_out_of_bounds` | Reject indices outside the logical array length. |
| `15_ub_safety/04_use_after_free` | Clear a pointer after freeing its target. |
| `15_ub_safety/05_sequence_points` | Avoid unsequenced reads and writes of the same object. |
| `15_ub_safety/06_strict_aliasing` | Reinterpret object representation with memcpy. |
| `15_ub_safety/07_alignment` | Query alignment with alignof and keep members aligned. |
| `15_ub_safety/08_null_pointer` | Never dereference a null pointer. |
| `15_ub_safety/09_standard_changes` | Detect the C standard version at compile time. |
| `15_ub_safety/10_identifier_length` | Use long internal identifiers and rely on the standard minimum. |
| `15_ub_safety/11_implementation_defined` | Observe implementation-defined char signedness and packing pragmas. |

## 16_data_structures - Data Structures

| Exercise | Objective |
| --- | --- |
| `16_data_structures/01_queue_adt` | Implement a fixed-capacity circular queue. |
| `16_data_structures/02_binary_search_tree` | Insert into and search a binary search tree. |
| `16_data_structures/03_dynamic_vector` | Grow a dynamic array and preserve existing elements. |

## 17_translation_units - Translation Units and Linkage

| Exercise | Objective |
| --- | --- |
| `17_translation_units/01_header_source_split` | Compile a program from a main file, a header, and an implementation file. |
| `17_translation_units/02_extern_linkage` | Declare a global variable in a header and define it in another file. |
| `17_translation_units/03_static_internal_linkage` | Keep a counter private to one translation unit with static. |
| `17_translation_units/04_external_type_check` | Keep declarations and definitions consistent across translation units. |
| `17_translation_units/05_dynamic_linking` | Load a symbol from a shared library at runtime. |

## 18_advanced_c - Advanced C

| Exercise | Objective |
| --- | --- |
| `18_advanced_c/01_variadic` | Read a variable number of int arguments with va_list. |
| `18_advanced_c/02_setjmp_longjmp` | Use non-local jumps for a simple error path. |
| `18_advanced_c/03_pthreads` | Create threads and protect shared state with a mutex. |
| `18_advanced_c/04_atomics` | Use atomic_int for lock-free counter updates. |
| `18_advanced_c/05_generic` | Choose an expression based on the type of a value. |
| `18_advanced_c/06_static_assert` | Use _Static_assert to enforce assumptions at compile time. |
| `18_advanced_c/07_align` | Query and request alignment. |
| `18_advanced_c/08_anonymous_union` | Access anonymous union members directly through the outer struct. |
| `18_advanced_c/09_thread_local` | Use _Thread_local to give each thread its own object. |
| `18_advanced_c/10_complex` | Use double complex, I, conj, creal, and cimag. |
| `18_advanced_c/11_signal` | Install a signal handler and use a sig_atomic_t flag. |
| `18_advanced_c/12_stack_frame` | Observe that nested function calls use distinct activation records. |

## 19_modern_c_library - Modern C Library

| Exercise | Objective |
| --- | --- |
| `19_modern_c_library/01_noreturn` | Declare a function that never returns and observe its exit status. |
| `19_modern_c_library/02_tgmath` | Use sqrt with both double and float arguments through tgmath.h. |
| `19_modern_c_library/03_atexit` | Register a cleanup function with atexit. |
| `19_modern_c_library/04_atomic_flag` | Use atomic_flag as a simple test-and-set lock. |

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

1. `00_basics` and `01_preprocessor`
2. `02_macros` and `03_types_variables`
3. `04_operators` and `05_control_flow`
4. `06_functions` and `07_pointers`
5. `08_arrays_strings` and `09_dynamic_memory`
6. `10_aggregates` and `11_data_representation`
7. `12_standard_library`, `13_character_io`, and `14_file_io`
8. `15_ub_safety` and `16_data_structures`
9. `17_translation_units` and `18_advanced_c`
10. `19_modern_c_library`

Do not read the solutions until you have run the exercise and
looked at the compiler or test output.  The point is to learn the
feedback loop, not to collect green checkmarks.
