## What This Book Is

This is a book about JavaScript. It is also a book about lykn. These are not two subjects wearing the same dust jacket — they are, like the language itself, a symbiosis.

Every chapter in this book maps to a set of concept cards drawn from four major JavaScript references: *Exploring JavaScript*, *Deep JavaScript*, *Eloquent JavaScript*, and *JavaScript: The Definitive Guide*. Over 1,500 concept cards have been catalogued, categorized, and distributed across the chapters that follow. When you learn about `bind` in lykn, you are learning about `const` and `let` in JavaScript — their scoping rules, their hoisting behaviour (or deliberate lack thereof), their relationship to the temporal dead zone. When you learn about `func`, you are learning about JavaScript functions, parameter handling, closures, and the `this` binding problem that `func` quietly eliminates by not having `this` at all.

The surface language is how you will *write*. JavaScript is what you will *understand*.

Chapter 2 will explain the two-layer architecture in detail — how surface forms compile to kernel forms, how kernel forms compile to ESTree, and how ESTree becomes the JavaScript you deploy. Until then, trust that the mechanism works and focus on the idioms.

A note about the voice. You will have noticed that this book does not read like a typical technical manual. The chapter you are reading opened with an adaptation of Monty Python's Dead Parrot Sketch, and subsequent chapters will open with similarly adapted sketches: the Spanish Inquisition, the Ministry of Silly Walks, the Cheese Shop, the Lumberjack Song, and others. This is not decoration. Each sketch dramatizes the chapter's core tension — the conceptual problem that the technical content resolves.

Every joke in this book, if you look closely, contains a technical insight. Every technical insight, if you look closely, is structured like a joke. A reader who skips every humorous passage will still learn everything they need. A reader who reads only the humorous passages will, surprisingly, learn quite a lot. But the intended experience is both at once, because programming is difficult enough without also being dull, and parentheses are long enough without the prose around them being dry.

There is one more thing to know before you begin. lykn is a young language. Its surface compiler is in active development. The features described in this book are the features that exist and work, not aspirational features on a roadmap. Where a feature is planned but not yet implemented, this book says so. Where a design decision is settled but the code is still being written, this book says that too. Honesty about the state of things is a form of respect for the reader, and this book aims to be respectful — even when it is, simultaneously, being somewhat ridiculous.
