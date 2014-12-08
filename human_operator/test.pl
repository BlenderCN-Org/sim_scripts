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

nounphrase(NP-X):-
  determiner(NP-S1),
  nounexpression(S1-X).
nounphrase(NP-X):-
  nounexpression(NP-X).

nounexpression(NE-X):-
  noun(NE-X).
nounexpression(NE-X):-
  adjective(NE-S1),
  nounexpression(S1-X).

verbphrase(VP-X):-
  verb(VP-S1),
  nounphrase(S1-X).



command([V], InList):- verb(V, InList-[]).


command([V,O], InList) :-
    verb(Object_Type, V, InList-S1),
    object(Object_Type, O, S1-[]).


verb(end, [end|X]-X).
verb(end, [quit|X]-X).
verb(end, [good,bye|X]-X).




verb(place, goto, [go,to|X]-X).
verb(place, goto, [go|X]-X).
verb(place, goto, [move,to|X]-X).

det([the|X]- X).
det([a|X]-X).
det([an|X]-X).
det([that|X]-X).


execute_cmd(L):-
    command(X,L),
    write('fff'),
    call(X).



foo(L) :-
    bar(L).
