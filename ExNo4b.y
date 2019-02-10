%{
#include<stdio.h>
%}
%token IDENTIFIER
%%
start: E {}
E: IDENTIFIER {$$=$1;}
;
%%
void main()
{
printf("\nEnter identifier :\n");
if(yyparse()==0)
printf("valid identifier \n");
}
yyerror()
{
printf("Invalid identifier\n");
}
