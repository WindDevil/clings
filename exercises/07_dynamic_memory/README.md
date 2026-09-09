# Dynamic Memory and Data Structures

Run an exercise with:

```sh
./clings run 01_malloc_free
```

| Exercise | Objective | Reference |
| --- | --- | --- |
| `01_malloc_free` | Use malloc and free for a dynamically sized array. | 第五章 5.3.5 内存泄漏；如何使用 malloc 函数 |
| `02_calloc` | Use calloc when every byte must start as zero. | 第五章 5.3.5.3 用 malloc 函数申请 0 字节内存 |
| `03_realloc` | Use realloc safely and initialize only the new elements. | 第五章 5.3.5 内存泄漏；malloc/realloc 资料 |
| `04_memory_leak` | Pair every allocation with a matching free. | 第五章 5.3.5 内存泄漏 |
| `05_buffer_bounds` | Copy at most dest_size - 1 bytes and always terminate. | 第五章 5.3.4 内存越界；5.3.2 为指针分配的内存太小 |
| `06_flexible_array` | Allocate a struct plus trailing data in one block. | 第一章 1.14.2 柔性数组 |
| `07_linked_list` | Build, traverse, and free a linked list. | 第五章 内存管理；结构体与指针综合 |
| `08_free_then_realloc` | Use realloc directly instead of freeing before growing an allocation. | C 陷阱与缺陷 7.10 |
