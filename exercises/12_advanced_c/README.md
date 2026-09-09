# Advanced C Features

Run an exercise with:

```sh
./clings run 01_variadic
```

| Exercise | Objective | Reference |
| --- | --- | --- |
| `01_variadic` | Read a variable number of int arguments with va_list. | 第六章 函数；C 标准 stdarg.h |
| `02_setjmp_longjmp` | Use non-local jumps for a simple error path. | 第六章 函数；C 标准 setjmp.h |
| `03_pthreads` | Create threads and protect shared state with a mutex. | 第六章 函数；POSIX threads 资料 |
| `04_atomics` | Use atomic_int for lock-free counter updates. | C11 标准 atomics 资料 |
| `05_generic` | Choose an expression based on the type of a value. | C11 标准 _Generic 资料 |
| `06_static_assert` | Use _Static_assert to enforce assumptions at compile time. | C11 标准 _Static_assert 资料 |
| `07_align` | Query and request alignment. | C11 标准 alignof/alignas 资料 |
| `08_anonymous_union` | Access anonymous union members directly through the outer struct. | 第一章 1.15 union 关键字；C11 匿名结构体/联合 |
| `09_thread_local` | Use _Thread_local to give each thread its own object. | C11 标准 _Thread_local 资料；POSIX threads |
| `10_complex` | Use double complex, I, conj, creal, and cimag. | C99 标准 complex.h 资料 |
| `11_signal` | Install a signal handler and use a sig_atomic_t flag. | C 标准 signal.h 资料 |
| `12_stack_frame` | Observe that nested function calls use distinct activation records. | C 专家编程 第6章 |
