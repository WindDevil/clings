# Standard Library and File I/O

Run an exercise with:

```sh
./clings run 01_printf_formats
```

| Exercise | Objective | Reference |
| --- | --- | --- |
| `01_printf_formats` | Match each conversion specifier to its argument type. | 第一章 1.5 sizeof；标准库 printf 资料 |
| `02_scanf_parse` | Parse a comma-separated pair with sscanf. | 第一章 1.6 条件判断；标准库 scanf 资料 |
| `03_strtol_errno` | Use strtol, errno, and the end pointer to validate input. | 第五章 5.3.1 函数的入口校验；标准库 strtol 资料 |
| `04_qsort_bsearch` | Use comparison callbacks for sorting and searching. | 第四章 4.7 函数指针；标准库 qsort 资料 |
| `05_math_functions` | Use hypot and other functions from math.h. | 第一章 1.4 基本数据类型；标准库 math.h 资料 |
| `06_time_functions` | Use time_t and difftime. | 标准库 time.h 资料 |
| `07_random` | Seed the generator and bound its output. | 标准库 stdlib.h 资料 |
| `08_file_io` | Write and read a text file with fopen, fputs, and fread. | 第五章 5.3.5 内存泄漏；标准库 stdio.h 资料 |
| `09_memory_functions` | Use the byte-oriented memory functions correctly. | 第四章 指针与数组；标准库 string.h 资料 |
| `10_string_search` | Use strchr, strrchr, and strstr. | 第五章 内存管理；标准库 string.h 资料 |
| `11_stdint_inttypes` | Use uint64_t and PRIu64 from stdint.h and inttypes.h. | 第一章 1.4 基本数据类型；C99 标准库 |
| `12_environment` | Read and write environment variables with getenv and setenv. | 第五章 5.3.1.3 函数的入口校验；标准库 stdlib.h 资料 |
| `13_printf_advanced` | Use width, zero padding, precision, and the * width argument. | C Primer Plus 第4章 4.4.3-4.4.6 |
| `14_scanf_advanced` | Use field width and a scanset in sscanf. | C Primer Plus 第4章 4.4.5、第11章 11.2.4 |
| `15_ctype_full` | Use isalnum and toupper with unsigned char casts. | C Primer Plus 第7章 7.2.2、第11章 11.7 |
| `16_rand_max` | Do not assume rand() returns a value below a fixed small bound. | C 陷阱与缺陷 7.8 |
