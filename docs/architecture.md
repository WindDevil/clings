# Architecture

`clings` 由四个互相独立的层次组成：

```text
规格层 (tools/specs_*.py)
        │
        ▼
生成层 (tools/generate_exercises.py)
        │
        ├── exercises/   初始练习
        ├── templates/   原始练习，用于 reset
        ├── solutions/   参考答案
        └── docs/        课程映射
        │
        ▼
运行层 (./clings)
        │
        ├── 发现练习
        ├── 编译单个练习
        ├── 运行内置测试
        ├── 记录进度
        └── verify / selftest
        │
        ▼
测试层 (include/clings/test.h)
```

## 为什么不用第三方测试框架

C 练习的第一个障碍往往是环境配置。`clings` 只依赖一个 C 编译器和
Python 标准库，因此学习者可以在最小环境中开始。内置测试框架只提供
断言、整数比较、字符串比较和内存比较，足以覆盖本项目的练习。

## 规格驱动生成

每个练习的正确版本和初始版本来自同一份规格。生成器对正确代码应用
`breaks` 替换，得到初始练习。这样做的好处是：

- 修改正确代码时，初始练习自动同步。
- 参考答案和练习的测试代码完全一致。
- `./clings selftest` 可以自动检查“初始失败、答案通过”这一不变量。

`tools/generate_exercises.py --check` 用于 CI：如果生成文件与规格不一致，
CI 会失败。

## 运行器

`./clings` 是一个零依赖 Python CLI。它的主要命令：

| 命令 | 作用 |
| --- | --- |
| `list` | 按主题列出练习和完成状态 |
| `next` | 显示下一个未完成练习 |
| `run [exercise]` | 编译并运行练习 |
| `run --all` | 按顺序运行所有练习 |
| `hint` | 显示目标、参考章节和提示 |
| `solution` | 打印或应用参考答案 |
| `reset` | 从 `templates/` 恢复初始练习 |
| `watch` | 文件变化后自动重跑 |
| `verify` | 编译并运行全部参考答案 |
| `selftest` | 检查全部练习初始失败、答案通过 |
| `doctor` | 打印 Python、编译器和编译参数 |
| `clean` | 删除 `build/clings/` |

进度保存在 `.clings/progress.json`，该文件已被 `.gitignore` 忽略。

## 编译策略

练习按需编译，每个练习是一个独立的可执行文件：

```text
build/clings/<topic>/<exercise>.exercise
build/clings/<topic>/<exercise>.solution
```

默认参数见 `clings` 文件中的 `DEFAULT_CFLAGS`。`-D_POSIX_C_SOURCE`
和 `-D_DEFAULT_SOURCE` 用于启用 `strtok_r`、`pthread` 等 POSIX 接口。

CMake 路径只默认构建 `solutions/`，并把它们注册为 CTest 测试；
`exercises/` 使用 `EXCLUDE_FROM_ALL`，因为部分初始练习故意无法编译。

## 目录约定

- `exercises/`：学习者实际编辑的文件。
- `solutions/`：参考答案，不要在这里练习。
- `templates/`：初始练习的只读副本，由 `reset` 使用。
- `docs/reference/`：PDF 转换后的参考书。
- `tools/specs_*.py`：唯一的练习事实来源。

如果只想修改一个练习的提示或参考章节，应修改对应的规格文件，然后
运行生成器，而不是直接编辑生成的文件。
