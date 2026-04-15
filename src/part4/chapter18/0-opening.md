## The Knights Who Say "Ni!" — The Demands Begin

"We are the Knights Who Say 'Ni!'" announces the tallest Knight, "and we demand... an Object!"

Someone constructs one.

```lisp
(obj :name "Ni" :demand "shrubbery")
```

The Knights examine it. Keywords as property names. Values after each keyword. Clean, no braces, no commas.

"That was... surprisingly straightforward," says the tallest Knight.

"NI!"

"We also demand property access!"

`user:name`

"And immutable updates!"

`(assoc user :age 43)`

"And structural pattern matching!"

`(match response ((obj :ok true :data d) (process d)) ...)`

The Knights look at each other. Each demand has been met with a single form. They are — briefly — satisfied.

"Bring us... the DETAILS!"
