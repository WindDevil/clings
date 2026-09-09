# Undefined Behavior, Safety, and Portability

Run an exercise with:

```sh
./clings run 01_signed_overflow
```

| Exercise | Objective |
| --- | --- |
| `01_signed_overflow` | Detect overflow before performing signed addition. |
| `02_uninitialized` | Give every local variable a defined initial value. |
| `03_out_of_bounds` | Reject indices outside the logical array length. |
| `04_use_after_free` | Clear a pointer after freeing its target. |
| `05_sequence_points` | Avoid unsequenced reads and writes of the same object. |
| `06_strict_aliasing` | Reinterpret object representation with memcpy. |
| `07_alignment` | Query alignment with alignof and keep members aligned. |
| `08_null_pointer` | Never dereference a null pointer. |
