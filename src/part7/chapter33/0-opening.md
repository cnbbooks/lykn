## And Now for Something Completely Analytical

"You've met the kernel compiler. It reads and dispatches."

"Who are you?"

"I do everything else."

"Such as?"

"Type checking. Contract verification. Exhaustiveness analysis. Macro expansion. Scope tracking. Unused binding detection. Destructuring pattern validation. Multi-clause overlap detection."

"How long have you been doing this?"

"Since Chapter 4."

The reader realizes: every safety guarantee in the book — every type check that fired, every exhaustiveness error that caught a missing variant, every contract that blamed the caller — was this compiler's work. The kernel compiler produces JavaScript. The surface compiler makes sure the JavaScript is *correct*.
