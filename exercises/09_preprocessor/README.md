# Preprocessor and Macros

Run an exercise with:

```sh
./clings run 01_object_macro
```

| Exercise | Objective | Reference |
| --- | --- | --- |
| `01_object_macro` | Use a named compile-time constant. | 第三章 3.1.1 数值宏常量 |
| `02_function_macro` | Protect macro arguments and the whole expansion with parentheses. | 第三章 3.1.4 用 define 宏定义表达式 |
| `03_stringize_paste` | Use # to stringize and ## to paste tokens. | 第三章 3.7 #运算符；3.8 ##运算符 |
| `04_conditional_compilation` | Select code at preprocessing time based on the language version. | 第三章 3.2 条件编译 |
| `05_include_guards` | Prevent multiple inclusion with a preprocessor guard. | 第三章 3.3 文件包含 |
| `06_variadic_macros` | Forward a variable argument list to a variadic function. | 第三章 3.1 宏定义；第六章 函数 |
| `07_x_macros` | Generate an enum and a string table from one list. | 第三章 3.1 宏定义；3.7 #运算符 |
| `08_pragma_error_line` | Use diagnostics, line control, and packing pragmas. | 第三章 3.4 #error；3.5 #line；3.6.8 #pragma pack |
| `09_std_macros` | Use __FILE__, __LINE__, __func__, and __STDC_VERSION__. | 第三章 3.1 宏定义；编译器预定义宏 |
| `10_undef_defined` | Undefine a macro and test it with defined(). | C Primer Plus 第16章 16.6.1-16.6.2 |
