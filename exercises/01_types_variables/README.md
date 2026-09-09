# Types, Variables, and Storage

Run an exercise with:

```sh
./clings run 01_integer_types
```

| Exercise | Objective | Reference |
| --- | --- | --- |
| `01_integer_types` | Use sizeof, CHAR_BIT, INT_MIN, and INT_MAX correctly. | 第一章 1.4 基本数据类型 |
| `02_signed_unsigned` | Avoid the usual arithmetic conversion trap when comparing. | 第一章 1.4 signed、unsigned 关键字 |
| `03_overflow` | Understand modulo wrap and avoid signed integer overflow. | 第一章 1.4 基本数据类型；第五章 内存管理 |
| `04_floating_point` | Compare floating-point values with an epsilon. | 第一章 1.6.2 float 与零值比较 |
| `05_char_ascii` | Work with char values and the ctype classification functions. | 第一章 1.4 基本数据类型 |
| `06_storage_scope` | Observe the lifetime of a static variable and block scope. | 第一章 1.1-1.3 auto、register、static |
| `07_qualifiers` | Use const, volatile, restrict, extern, auto, and register. | 第一章 1.1-1.3 auto、register、static；1.11 const；1.12 volatile；1.13 extern |
| `08_stdbool_stddef` | Use bool and size_t from the standard headers. | 第一章 1.4 基本数据类型；C99/C11 标准库 |
| `09_long_double` | Use long double and compare its precision with double. | C Primer Plus 第3章 3.4.6 |
| `10_octal_constants` | Recognize that a leading zero means base 8. | C 陷阱与缺陷 1.4 |
| `11_char_signedness` | Use signed char and unsigned char explicitly when the sign matters. | C 陷阱与缺陷 7.4 |
| `12_integer_promotions` | See that char operands are promoted to int in arithmetic expressions. | C 专家编程 第8章 |
