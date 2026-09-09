# Contributing

感谢你愿意改进 `clings`。这个项目的核心原则是：

1. 练习必须能独立编译和运行。
2. 初始状态必须失败；参考答案必须通过。
3. 每个练习只聚焦一个主要概念，但可以覆盖相关细节。
4. 提示应当引导思考，而不是直接给出答案。
5. 练习与参考答案由生成器保持同步。

## 添加一个练习

1. 在 `tools/specs_00_04.py`、`tools/specs_05_08.py` 或
   `tools/specs_09_12.py` 中选择对应主题。
2. 调用 `ex(...)` 添加规格：

```python
ex(
    topic="01_types_variables",
    slug="07_new_exercise",
    title="...",
    objective="...",
    reference="第一章 ...",
    hint="...",
    code=r"""
int answer(void)
{
    return 42;
}
""",
    tests=r"""
CLINGS_CHECK_INT(answer(), 42);
""",
    breaks=[
        (
            "return 42;",
            "/* TODO: return the answer. */\n    return 0;",
        )
    ],
)
```

3. 重新生成：

```sh
python3 tools/generate_exercises.py
```

4. 验证：

```sh
./clings verify
./clings selftest
python3 tools/generate_exercises.py --check
```

## 规格字段

| 字段 | 说明 |
| --- | --- |
| `topic` | 主题目录名，例如 `06_pointers` |
| `slug` | 练习文件名，例如 `03_pointer_arithmetic` |
| `title` | 练习标题 |
| `objective` | 一句话学习目标 |
| `reference` | 《C 语言深度解剖》章节或其他资料 |
| `hint` | 不直接给答案的提示 |
| `code` | 正确代码（包含需要的 `#include`） |
| `tests` | `main` 中执行的测试代码 |
| `breaks` | 将正确代码转成初始练习的替换列表 |
| `compile_fail` | 初始状态是否故意无法编译 |

多文件项目练习使用 `project()`，其中 `files` 是文件名到完整内容的映射，
`file_breaks` 是 `(文件名, 正确片段, 初始片段)` 替换列表。运行器会自动
编译项目目录中的所有 `.c` 文件，并把该目录加入头文件搜索路径。

## 测试框架

练习只需要包含 `include/clings/test.h`，并使用：

- `CLINGS_CHECK(expr)`
- `CLINGS_CHECK_MSG(expr, message)`
- `CLINGS_CHECK_INT(actual, expected)`
- `CLINGS_CHECK_STR(actual, expected)`
- `CLINGS_CHECK_MEM(actual, expected, size)`
- `clings_report()`

## 代码风格

- 使用 C17。
- 缩进 4 个空格，花括号另起一行。
- 默认开启 `-Wall -Wextra -Wpedantic -Werror`。
- 不要依赖未定义行为，除非该练习的目标就是演示未定义行为。
- 优先使用 `snprintf`、`memcpy`、显式边界和错误返回值。

运行共享头文件格式化：

```sh
make format
```

## 提交前检查

```sh
./clings verify
./clings selftest
python3 tools/generate_exercises.py --check
```
