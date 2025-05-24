# JOHN MARY ALOGRITHM
% Facts
likes(mary, food).
likes(mary, wine).
likes(john, wine).
likes(john, mary).

% Rules
likes(john, X) :- likes(mary, X).       % John likes anything Mary likes
likes(john, Y) :- likes(Y, wine).       % John likes anyone who likes wine
likes(john, Y) :- likes(Y, Y).          % John likes anyone who likes themselves

% Queries

% Query 1: Does John like food?
% ?- likes(john, food).

% Query 2: Does John like wine?
% ?- likes(john, wine).

% Query 3: Does John like food if Mary likes food?
% (Already covered by Rule 1 and existing fact)
% ?- likes(john, food).

% Query 4: Who does John like?
% ?- likes(john, Y).

  # MINIMAX ALGORITHM

  % Rule to find the minimum of two numbers
minimum(X, Y, X) :- X =< Y.
minimum(X, Y, Y) :- X > Y.

% Rule to find the maximum of two numbers
maximum(X, Y, X) :- X >= Y.
maximum(X, Y, Y) :- X < Y.

% Example Queries:

% 1. Find the minimum of two numbers
% ?- minimum(5, 10, Min).
% Output: Min = 5.

% 2. Find the maximum of two numbers
% ?- maximum(5, 10, Max).
% Output: Max = 10.

% 3. Find both minimum and maximum of two numbers
% ?- minimum(8, 3, Min), maximum(8, 3, Max).
% Output: Min = 3, Max = 8.
