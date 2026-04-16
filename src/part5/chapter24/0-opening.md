## We Use... REGEXP!

*(dramatic chord)*

Someone needs to validate an email address. The room goes quiet.

"We must use... REGEXP!"

*(dramatic chord)*

Everyone flinches. An old developer steps forward.

"It's just pattern matching. Watch."

```lisp
(bind pattern (regex "\\S+@\\S+" "i"))
```

*(dramatic chord)*

"Stop that. It's a string, a few special characters, and a flag. That's all regex is."

"What about the backslashes?"

"Character class escapes. `\\S` means non-whitespace."

*(chord, quieter)*

"And the `i`?"

"Case-insensitive. It's a flag."

*(chord, barely audible)*

"See? Not so scary."

The dramatic chord will return throughout this chapter. By the end, nobody will flinch.
