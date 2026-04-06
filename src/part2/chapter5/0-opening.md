## The Black Knight

JavaScript's type coercion system guards a bridge.

"None shall pass," it announces, despite having no clear policy on what constitutes passing or, for that matter, what constitutes a type.

A number approaches. `"5" + 3`. The coercion system considers this, performs an internal calculation of baroque complexity, and produces `"53"`.

"Tis but a concatenation," it says.

`"5" - 3`. This time, the result is `2`.

"Just a numeric conversion."

`[] + {}` steps forward. The coercion system examines it, converts the array to an empty string, converts the object to `"[object Object]"`, concatenates them, and presents the result with quiet pride: `"[object Object]"`.

"I've had worse."

`[] + []` produces `""`. `{} + []` produces `0` — or possibly `"[object Object]"`, depending on whether JavaScript interprets the first `{}` as an empty block or an empty object, a decision it makes based on context and, one suspects, mood.

The coercion system stands its ground, armless, legless, bleeding type errors from every stump. "Come back here! I'll coerce you! I'll turn your integers into strings! I'll concatenate your `undefined`! It's just a flesh wound!"

From behind it, a Lykn developer walks up with `:number`.

"That's a number," she says. "Not a string. Not NaN. Not `undefined` concatenated with a prayer. A number."

The Black Knight opens his mouth to argue. The type check fires. He has no comeback.
