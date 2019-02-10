%{
#include<stdio.h>
#include"y.tab.h"
extern yylval;
%}
%%
[_]?[a-zA-Z_][a-zA-z0-9_]* {return IDENTIFIER;}
[\t]+;
[\n] {return 0;}
. {return yytext[0];}
%%
int yywrap()
{
return 1;
}
