# Undefined Behavior, Safety, and Portability

Run an exercise with:

```sh
./clings run 01_signed_overflow
```

| Exercise | Objective | Reference |
| --- | --- | --- |
| `01_signed_overflow` | Detect overflow before performing signed addition. | 第一章 1.4 signed、unsigned 关键字；第五章 内存管理 |
| `02_uninitialized` | Give every local variable a defined initial value. | 第五章 5.3.3 内存分配成功，但并未初始化 |
| `03_out_of_bounds` | Reject indices outside the logical array length. | 第五章 5.3.4 内存越界 |
| `04_use_after_free` | Clear a pointer after freeing its target. | 第五章 5.3.6 内存已经被释放了，但是继续通过指针来使用 |
| `05_sequence_points` | Avoid unsequenced reads and writes of the same object. | 第二章 2.7 ++、--操作符 |
| `06_strict_aliasing` | Reinterpret object representation with memcpy. | 第四章 4.7.2 *(int*)&p；第五章 内存管理 |
| `07_alignment` | Query alignment with alignof and keep members aligned. | 第三章 3.6.8.1 为什么会有内存对齐 |
| `08_null_pointer` | Never dereference a null pointer. | 第四章 4.1.3 int *p = NULL 和 *p = NULL 有什么区别 |
