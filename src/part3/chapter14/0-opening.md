## The Killer Rabbit

"It's just a `this` keyword," says the developer, peering into the cave of the JavaScript API. "How bad can it be?"

The `this` keyword lunges. The method loses its binding. The callback silently rebinds to `undefined`. An event handler that worked in one context produces `TypeError: Cannot read properties of undefined` in another.

"I *warned* you!" shouts Tim the Enchanter from a safe distance. "But did you listen? 'Oh, it's just a little keyword,' you said. 'It's just a binding mechanism,' you said."

The developer retreats to surface Lykn, where `this` doesn't exist. The cave mouth — JavaScript's entire ecosystem — still glitters with treasure: DOM APIs, third-party libraries, framework hooks, server runtimes. How do you get the treasure without the rabbit?

"Bring forth the Holy Hand Grenade of Antioch!"

"The `js:` namespace, sire."

"Right. First thou pullest the colon. Then thou typest `js`. Then, the interop namespace being reached, thou invokest."
