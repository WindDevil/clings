# 《C 语言接口与实现》覆盖核对

原 PDF 是扫描版，本轮已用 Tesseract `chi_sim+eng` 完成 399 页 OCR：

- 原始 PDF：`.ref/books/C/C语言接口与实现.pdf`
- OCR 文本：`.ref/ocr/C/C语言接口与实现.txt`
- OCR 后 Markdown：`.ref/markdown/C/C语言接口与实现.md`
- 提取字符数：约 510,561

这本书的重点不是 C 语法，而是**接口设计、实现分离、ADT 和可复用软件
工程**。因此现有练习能覆盖一部分语言/数据结构基础，但书中的 24 个接口
和大量工程模式大部分还没有对应练习。

## 逐章覆盖

| 章 | 书中的主题 | 状态 | 现有练习 | 说明 |
| --- | --- | --- | --- | --- |
| 1 | 简介、literate 程序、编程风格、效率 | 部分覆盖 | `docs/architecture.md`、`CONTRIBUTING.md`、代码风格文档 | 有工程风格文档，没有 literate programming 练习 |
| 2 | 接口与实现、ADT、客户调用程序的责任 | 部分覆盖 | `13_translation_units/01`-`04`、`17_data_structures/01_queue_adt`、`17_data_structures/03_dynamic_vector` | 有头文件/源文件、extern、静态链接和两个 ADT，但没有不透明类型、客户契约、迭代器接口等完整方法 |
| 3 | 原子（Atoms） | 未覆盖 | 无 | 缺少字符串驻留/原子表接口 |
| 4 | 异常与断言 | 部分覆盖 | `00_getting_started/04_debug_assert`、`12_advanced_c/02_setjmp_longjmp`、`12_advanced_c/06_static_assert` | 有 assert/setjmp/static_assert，没有 TRY/EXCEPT/FINALLY 宏和异常栈 |
| 5 | 内存管理 | 部分覆盖 | `07_dynamic_memory/01`-`08` | 有 malloc/calloc/realloc/free、泄漏、越界、free 后 realloc，没有 Mem 接口、分配器抽象、检查和统计 |
| 6 | 进一步内存管理 | 未覆盖 | 无 | 缺少 arena、free list、pool/slab 分配器 |
| 7 | 链表（Lists） | 部分覆盖 | `07_dynamic_memory/07_linked_list` | 只有单向链表，没有 List ADT、双向链表、迭代器、所有权约定 |
| 8 | 表（Tables） | 未覆盖 | 无 | 缺少 Table ADT、哈希表、键值接口和迭代器 |
| 9 | 集合（Sets） | 未覆盖 | 无 | 缺少 Set ADT、成员操作、并/交/差 |
| 10 | 动态数组 | 部分覆盖 | `17_data_structures/03_dynamic_vector` | 有动态数组增长，没有 Array 接口、容量策略、迭代器和异常语义 |
| 11 | 序列（Sequences） | 未覆盖 | 无 | 缺少 Sequence ADT、高层列表操作和迭代器 |
| 12 | 环（Rings） | 未覆盖 | 无 | 缺少环形缓冲区/ring buffer |
| 13 | 位向量 | 部分覆盖 | `02_operators/04_bitwise`、`16_data_representation/04_bitfield_portability` | 有位运算和位域，没有 Bit vector ADT、集合运算和迭代器 |
| 14 | 格式化 | 部分覆盖 | `10_stdlib_io/01`、`10_stdlib_io/13`、`15_string_functions/03` | 有 printf/snprintf，没有 Fmt 接口和自定义格式转换 |
| 15 | 低级输入/输出 | 部分覆盖 | `18_file_io_advanced/01`-`07` | 有 stdio 文件 I/O，没有低级 read/write 包装、File/Fmt 接口 |
| 16 | 文本（Text） | 未覆盖 | 无 | 缺少 Text ADT、字符串盒、文本拼接/切片/格式化 |
| 17 | 扩展精度算法 | 未覆盖 | 无 | 缺少大整数/扩展精度算术 |
| 18 | 任意精度算法 | 未覆盖 | 无 | 缺少任意精度整数接口和计算器示例 |
| 19 | 多精度算法 | 未覆盖 | 无 | 缺少多精度算术、模运算和高级算法 |
| 20 | 线程 | 部分覆盖 | `12_advanced_c/03_pthreads`、`04_atomics`、`09_thread_local` | 有 pthread、atomic、thread-local，没有书中的 Thread 接口、线程安全内存和同步抽象 |

## 结论

现有 167 个练习覆盖了这本书的**语言基础和部分数据结构基础**，但没有覆盖
这本书真正的主体：**接口设计方法、ADT 工程化、24 个可复用接口**。

如果按这本书补齐，最值得新增的主题是：

1. `interfaces_and_adts`：不透明类型、接口契约、客户责任、迭代器。
2. `allocators`：Mem/Arena/Free-list/Pool 分配器。
3. `containers`：List、Table、Set、Sequence、Ring、Bit vector。
4. `text_and_format`：Text、Fmt、低级 I/O。
5. `big_integers`：扩展/任意/多精度算术。
6. `thread_abstraction`：Thread 接口、线程安全内存和同步。

本轮只做 OCR 和覆盖核对，没有把上述练习加入项目。
