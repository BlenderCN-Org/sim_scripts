sentence(S) :-
  nounphrase(S-S1),
  verbphrase(S1-[]).


noun([dog|X]-X).
noun([cat|X]-X).
noun([mouse|X]-X).

verb([ate|X]-X).
verb([chases|X]-X).

adjective([big|X]-X).
adjective([brown|X]-X).
adjective([lazy|X]-X).

determiner([the|X]-X).
determiner([a|X]-X).
