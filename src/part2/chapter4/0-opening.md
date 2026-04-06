## The Bridge of Death

A JavaScript developer approaches a rickety bridge spanning the Gorge of Eternal `undefined`. A Bridgekeeper in tattered robes blocks the way.

"Stop! Who would cross the Bridge of Death must answer me these questions three, ere the other side he see."

The developer swallows nervously. Behind her, the wreckage of several `var` declarations litter the path, their hoisted corpses rising unbidden to the top of the function scope.

"What... is your declaration keyword?"

"It depends. If I need reassignment, `let`. If I don't, `const`. Unless I'm in a legacy codebase, in which case `var`, but only at function scope, and I need to remember that it hoists to—"

"What... is your scope?"

"Block scope for `let` and `const`. Function scope for `var`. Unless I'm at the top level, in which case `var` creates a property on the global object but `let` doesn't, and—"

"What... is the hoisting behavior of your binding?"

"Well, `var` is hoisted with `undefined`, `let` and `const` have a temporal dead zone where they exist but accessing them throws a `ReferenceError`, and function declarations are fully hoisted but function expressions assigned to `var` are hoisted as `undefined` and—"

The Bridgekeeper's eye twitches. From a distance, a second figure approaches.

"What... is your declaration keyword?"

"`bind`."

"What... is your scope?"

"Lexical."

"What... is the hoisting behavior of your—"

"There isn't one."

A long silence. The Bridgekeeper consults his notes. He finds no further questions. He steps aside.
