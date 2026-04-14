## The Knights Who Say Ni

A developer approaches a clearing in the forest. Three tall figures in horned helmets block the path.

"We are the Knights Who Say Ni! And we demand... a precondition!"

The developer, who has been writing functions without contracts for years, shifts uncomfortably.

"A... precondition?"

"A precondition! One that asserts the amount is positive. And we demand it be a single expression, composed with `and` and `or` as needed. No vectors! We are very particular about our syntax."

The developer adds `:pre (> amount 0)`.

"Now — we demand a postcondition!"

The developer adds `:post (>= (get ~ :balance) 0)`.

"Now — we demand another clause! With different arities! And non-overlapping types!"

The developer adds a second clause. The Knights inspect it. They run the overlap checker. No conflicts are found.

"That," says the head Knight, peering at the function through the visor of Maranget's algorithm, "is a nice function. We will accept it."

The developer passes through the clearing, contracts intact. Behind her, the Knights return to their posts, ready to demand preconditions from the next developer who dares to write a function without specifying what it promises.
