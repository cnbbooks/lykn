## How Not To Be Seen

"And now for something completely different: How Not To Be Seen."

"In this picture there is a kernel compiler. It has been compiling Lykn code since Chapter 1. Can you see it?"

No. You cannot. The reader has been using it for twenty-nine chapters without once needing to think about it. It reads s-expressions, produces JavaScript, and disappears. No runtime artifacts. No evidence it was ever there.

"Mr. Kernel Compiler, would you stand up please?"

The compiler stands up. It's a reader (320 lines), a dispatch table (1,671 lines), and a vendored pretty-printer. That's it. No explosion. No dramatic reveal. Just a small, clean pipeline that has been doing its job invisibly since the first `(bind greeting "Hello, World!")`.

"That's the whole thing?"

"That's the whole thing."
