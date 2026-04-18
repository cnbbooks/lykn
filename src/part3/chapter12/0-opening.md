## The Emporium

A developer walks into the National Property Access Emporium.

"I'd like some property access, please."

"Certainly, sir. What kind?"

"Do you have any dot notation? `obj.prop`?"

"No sir. We use colon syntax here. `obj:prop`."

"Bracket notation? `obj['prop']`?"

"That would be `(get obj :prop)`, sir."

"Optional chaining? `obj?.nested?.deep`?"

"For nil-safe access, might I recommend `some->` from Chapter 13, sir?"

"How about `Reflect.get`?"

"We don't stock that, sir. Never much call for it around here."

"But it's the single-most popular usage in the WORLD!"

"Sorry, sir."

Astonished, the developer looks at the menu. Two items: `obj:prop` for static access, `(get obj key)` for dynamic access. Both are in stock. Both work. Neither requires a seventeen-page specification document to understand.

"That's... actually all I need," the developer says, with the slightly dazed expression of someone who has visited a property access establishment and actually found what they were looking for.
