# Pointers and Memory Layout

Run an exercise with:

```sh
./clings run 01_pointer_basics
```

| Exercise | Objective | Reference |
| --- | --- | --- |
| `01_pointer_basics` | Read and write through pointers. | 第四章 4.1 指针 |
| `02_null_and_const` | Check for NULL and respect pointer-to-const. | 第四章 4.1.3 int *p = NULL 和 *p = NULL |
| `03_pointer_arithmetic` | Walk an array with pointers and return a pointer into it. | 第四章 4.3.1 以指针的形式访问和以下标的形式访问 |
| `04_pointer_to_pointer` | Let a function allocate and update a caller-owned pointer. | 第四章 4.5.2 二级指针 |
| `05_void_pointer` | Use void pointers and unsigned char for type-agnostic code. | 第四章 4.1.6 如何达到手中无剑、胸中也无剑的地步 |
| `06_dangling_wild` | Set a freed pointer to NULL to prevent accidental reuse. | 第五章 5.1 什么是野指针；5.3.5 内存泄漏 |
| `07_pointer_to_array` | Distinguish a pointer to an array from a pointer to its first element. | 第四章 4.3.2 a 和 &a 的区别；4.4 指针数组和数组指针 |
