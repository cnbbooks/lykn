## The Knights Who Say ... _What?_

A developer approaches a clearing in the forest. Three tall figures in horned helmets block the path.

"We are the Knights Who Say NaN! And we demand... a _precondition!_"

The developer, who has been writing functions without contracts for years, shifts uncomfortably.

"A... precondition?"

"A precondition! One that asserts the amount is positive. And we demand it be a single expression, composed with `and` and `or` as needed. No vectors! We are very particular about our syntax."

The developer asks "What about `:pre (> amount 0)`?"

"Now — we demand a _postcondition!_"

The developer shifts nervously from foot to foot, eventually summoning enough courage to venture a muttered "So ... `:post (>= (get ~ :balance) 0)`?"

"Now — we demand another clause! With different arities! And non-overlapping types!"

The developer, starting to get the hang of this, adds another clause. The Knights inspect it. They run the overlap checker. No conflicts are found.

"That," says the head Knight, peering at the function through the visor of Maranget's algorithm, "is a nice function. We will accept it."
