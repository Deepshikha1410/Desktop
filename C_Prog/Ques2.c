#include<stdio.h>
void new_func1(void);
void func1(void)
{
    printf("\n Inside func1 \n");
    int i = 0;
    for(;i<0xffffff;i++);
    new_func1();
    return ;
}

static void func2(void)
{
    printf("\n Inside func2 \n");
    int i = 0;
    for(;i<0xffffffaa;i++);
    return;
}


void new_func1(void)
{
    printf("\n Inside new_func1()\n");
    int i = 0;
    for(;i<0xffffffee;i++);
    return;
}
int main(void) 
{
    printf("\nInside main()\n");
    int i = 0;
    for(;i<0xffffff;i++);
    func1();
    func2();
    return 0;
}