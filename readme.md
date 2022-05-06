将 c 的声明转换成空的宏定义，避免编译报错

大概效果是这样的

输入

```c
// comments
void test();
void test1(void);
void test2(int i, char c);
void test3(int i);
void *test4(int i);
int test5(int i);
bool test6(int i);
```

输出

```c
#define test(...) 
#define test1(...) 
#define test2(...) 
#define test3(...) 
#define test4(...) NULL
#define test5(...) 0
#define test6(...) false
```
