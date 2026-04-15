## The Holy Hand Grenade — The Counting

Brother Maynard opens the Book of Arrays.

"And the Lord spake, saying: 'First shalt thou index from zero. Then, shalt thou count to the length minus one. No more. No less. The length minus one shall be the number thou shalt count, and the number of the counting shall be the length minus one. The length shalt thou not count, neither count thou negative one, excepting that thou then proceed to use `.at()`. The length plus one is right out.'"

Someone tries `(get items 5)` on a three-element array.

"Five is right out!"

"It's `undefined`, actually," observes Brother Maynard. "Which is worse."

The Holy Hand Grenade is lobbed: `(nums:map (fn (:number x) (* x 2)))`. The array is transformed. Nobody had to count anything.

"And there was much rejoicing."

"Yay."
