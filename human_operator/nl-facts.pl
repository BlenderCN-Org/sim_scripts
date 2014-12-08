%sentence(S) :-
%  nounphrase(S-S1),
%  verbphrase(S1-[]).


%noun([dog|X]-X).
%noun([cat|X]-X).
%noun([mouse|X]-X).

%verb([ate|X]-X).
%verb([chases|X]-X).

%adjective([big|X]-X).
%adjective([brown|X]-X).
%adjective([lazy|X]-X).

%determiner([the|X]-X).
%determiner([a|X]-X).

%nounphrase(NP-X):-
%  determiner(NP-S1),
%  nounexpression(S1-X).
%nounphrase(NP-X):-
%  nounexpression(NP-X).

%nounexpression(NE-X):-
%  noun(NE-X).
%nounexpression(NE-X):-
%  adjective(NE-S1),
%  nounexpression(S1-X).

%verbphrase(VP-X):-
%  verb(VP-S1),
%  nounphrase(S1-X).



%command([V], InList):- verb(V, InList-[]).


%command([V,O], InList) :-
%    verb(Object_Type, V, InList-S1),
%    object(Object_Type, O, S1-[]).


command([Pred,Arg]) --> verb(Type,Pred),nounphrase(Type,Arg).
command([Pred]) --> verb(direct,Pred).
%command([goto,Arg]) --> noun(go_position,Arg).%%There are different position types


%nounphrase(Type,Args):-
%    noun(Type,Args).




nounphrase(Type,Noun) --> quant,noun(Type,Noun).
nounphrase(Type,Noun) --> noun(Type,Noun).

obj(tree).
obj(rock).
obj(robot).

isObj(L1):- obj(L1).
    
quant --> [the].
quant --> [a].
quant --> [an].
quant --> [that].


goto(Obj):-
    obj(Obj),
    moveTo(Obj).

goto(Obj):-
    goto(a,Obj).
%goto(Quant, Obj):-
%    obj(Obj),
%    moveTo(Obj).


verb(direct,V) --> direct_verb(V).
verb(go_position, goto) --> nav_verb.

direct_verb(end) --> [end].
direct_verb(end) --> [quit].
direct_verb(end) --> [good,bye].

direct_verb(help) --> [help].
direct_verb(help) --> [help,me].


noun(go_position,R) --> [R], {isObj(R)}.

nav_verb --> [go,to].
nav_verb --> [go].
nav_verb --> [move,to].
nav_verb --> [navigate,to].




get_command(C,L):-
    command(X,L,[]),
    C =.. X, !.

get_command(_,L):-
    write('I don''t understand '),write(L), nl, fail.
execute_cmd(L):-
    get_command(X,L),
    call(X).


