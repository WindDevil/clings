# Structs, Unions, Enums, and Bitfields

Run an exercise with:

```sh
./clings run 01_struct_basics
```

| Exercise | Objective | Reference |
| --- | --- | --- |
| `01_struct_basics` | Create a struct value and access its members through a pointer. | 第一章 1.14 struct 关键字 |
| `02_nested_structs` | Access a nested member through an outer struct pointer. | 第一章 1.14 struct 关键字 |
| `03_padding_alignment` | Observe padding and member offsets with offsetof. | 第一章 1.14.1 空结构体多大；第三章 3.6.8 #pragma pack |
| `04_bitfields` | Store several small flags in one struct. | 第一章 1.14 struct 关键字；2.5 位运算符 |
| `05_union` | Compare union size with the size of its largest member. | 第一章 1.15 union 关键字 |
| `06_enum` | Use an enum for a small closed set of values. | 第一章 1.16 enum 关键字 |
| `07_typedef_designated` | Use a typedef and initialize members by name. | 第一章 1.17 typedef 关键字 |
| `08_container_of` | Recover an outer struct from a pointer to one of its members. | 第一章 1.14 struct 关键字；1.5 sizeof |
