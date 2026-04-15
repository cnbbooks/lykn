## The Knights Who Say "Ni!" (Preview)

"We are the Knights Who Say 'Ni!'" announces the tallest Knight. "And we demand... a resolved Promise!"

The developer shifts uncomfortably. "I... I can't resolve it right now. It's still pending."

"THEN YOU MUST AWAIT!"

"I am awaiting! But the network—"

"NI!"

The developer wraps the call in `try`/`catch`. The Promise rejects. The Knights flinch.

"NI! NI! NI! An unhandled rejection!"

"It's *handled*," the developer says, showing the catch block. "See? `(catch e (Err e:message))`. The rejection is wrapped in a `Result`. The caller uses `match`."

The Knights examine the error handling. The rejected Promise has been converted to an `(Err ...)`. The caller's `match` covers both `Ok` and `Err`. No unhandled rejections. No silent failures.

"Bring us... ANOTHER Promise!" says the head Knight. "One that resolves with a shrubbery!"

The developer sighs and adds another `await`.
