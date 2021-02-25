---
title: 密码学-01-数论基础
date: 2021-02-25 16:54:27
categories:
- Math
tags:
- Number Theory  
mathjax: true
---

## 模算术

模算术（Modular Arithmetic）是数论中的一个分支。 最常见的一个例子是 12 小时的时钟，例如当前时间是 7 点，过 8 个小时之后是 3 点。在平常的加法运算中 7 + 8 = 15。但是在12时钟系统中，7 + 8 = 3。

如果两个数 $a$ 和 $b$ 除以 $n$ 有相同的余数，那么 $a$ 和 $b$ 的关系称作**模 $n$ 同余**（congruent modulo n），他们满足这个等式：$a - b = kn$，$k$ 为大于等于 $0$ 的整数。

$a$ 和 $b$ 的**模 $n$ 同余**关系用数学符号表示为

$$ a\equiv b{\pmod {n}} $$

$a$ 和 $b$ 的关系叫做**同余关系**（congruence relation）。$n$ 叫做模数（modulus）。

对于模数 $n$，与数 $a$ 同余的所有整数集合称为**同余类**（congruence class），用符号 $\overline{a}_n$ 表示。

**模算术的性质**

1. 自反性：$a \equiv a \pmod n$
2. 对称性：如果 $a \equiv b \pmod n$，则有 $b \equiv a \pmod n$
3. 传递性：如果 $a \equiv b \pmod n$，$b \equiv c \pmod n$，则有 $a \equiv c \pmod n$

4. 如果 $a \equiv b \pmod n$，$c \equiv d \pmod n$， 则有：
    - $a + c \equiv b + d \pmod n$
    - $a - c \equiv b - d \pmod n$
    - $ac \equiv bd \pmod n$

5. 消去律：如果 $ac \equiv bc \pmod n$，$c \ne 0$，且 $\gcd(c,n)=1$，则有 $a \equiv b \pmod n$

## 费马小定理

费马小定理（Fermat's Little Theorem）：假如 $a$ 是一个整数，$p$ 是一个质数，且 $gcp(a, p)=1$，那么有

$$ a^{p-1}\equiv 1{\pmod {p}} $$

证明：

设集合 $A = \{1, 2, ..., p-1\}$，$A$ 构成 $p$ 的**完全剩余系**，即 $A$ 中不存在两个数同余 $p$。将 $A$ 中的每个元素乘以 $a$ 得到集合 $B = \{1 \cdot a, 2 \cdot a, ..., (p-1) \cdot a\}$。设 $ta$ 与 $sa$ 为 $B$ 中任意两个元素，$0 < t < s < p$，这两个元素的差为 $a(s-t)$，因为 $a$ 与 $p$ 互质，所以 $a(s-t)$ 不可能是 $n$ 的倍数，因此 $B$ 中任意两个元素除以 $p$ 有不同的余数。

设 $B$ 中每个元素除以 $p$ 得到的余数集合是 $R=\{r_1, r_1, ..., r_{p-1}\}$，因为 R 中的元素互不相等，因此$R$ 与 集合$A$ 含有相同的素。

$$
\displaystyle {
\begin{array}{rcrcr}
1 \cdot a & \equiv & r_1 {\pmod p} \\
2 \cdot a & \equiv & r_2 {\pmod p} \\
& ...\\
(p-1) \cdot a & \equiv & r_{p-1} {\pmod p} \\
\end{array}}
$$

将上述等式两边相乘得到：

$$ 1\cdot2 \dots \cdot (p-1)\cdot a^{p-1} \equiv  r_1 \cdot r_2 \dots \cdot r_{p-1} \equiv 1\cdot2 \dots \cdot (p-1) {\pmod p}$$

令 $W = 1\cdot2 \dots \cdot (p-1)$，上述等式简化为

$$ W \cdot a^{p-1} \equiv W {\pmod p}$$

因为 $p$ 为质数，所以 $gcd(W, p) = 1$，因此根据模算数的消除率，等式两边消去 $W$ 得到

$$ a^{p-1}\equiv 1{\pmod {p}} $$

## 欧拉函数

对于正整数 $n$，欧拉函数（Euler's totient function）是小于 $n$ 的正整数中与 $n$ 互质的数的个数。通常表示为：$\varphi (n)$，计算函数表达式如下：

$$ \varphi (n)=n\prod _{p\mid n}\left(1-{\frac {1}{p}}\right) $$

其中 $p | n$ 表示 $p$ 整除 $n$ ，上式的乘积针对的是 $n$ 的所有**不同**质因数。

例如 12 的所有不同质因数为：2，3。那么根据欧拉函数计算得到：
$$ \varphi (12)=12(1 - {\frac {1}{2}})(1 - {\frac {1}{3}}) = 4 $$
也就是说小于 12 的数中有 4 个数与 12 互质，分别是：1，5，7，11。

**性质**

1. 如果 $n$ 为质数
   $$ \varphi (n)=n-1 $$

2. 如果 $m$，$n$ 互质，那么：
   $$ \varphi (mn)=\varphi (m)\varphi (n) $$

3. 如果 $p$ 是一个质数，$k$ 是大于等于1的正整数。那么：
   $$ \varphi (p^k)=p^k-p^{k-1} $$

4. $n$ 的所有质因数的欧拉函数和为 $n$。
   $$ \sum _{d\mid n}\varphi (d)=n $$

## 数论中的欧拉定理

欧拉定理有很多个，在数论中，欧拉定理（Euler's theorem）给出了两个互质数 $n$ 和 $a$ 之间拥有如下关系：

$$ a^{\varphi (n)} \equiv 1 \pmod{n} $$

证明：

在证明欧拉定理之前，我们要证明：如果 $ a \equiv b \pmod n $，且 $gcd(a, n) = 1$，则有 $gcd(b, n)=1$。也就是说**如果 $a$ 与 $b$ 模 $n$ 同余，且 $a$ 与 $n$ 互质，那么 $b$ 与 $n$ 也互质**。

采用反正法，假设 $gcd(b, n)=t$，且 $t>1$。那么存在整数 $r$ 和 $s$，使 $b = rt$，$n= st$。因为 $ a \equiv b \pmod n $，则存在整数 $k$，使
$$a=kn+b=kst+rt=(ks+r)t$$
因此，$a$ 与 $n$ 都能被 $t$ 整除，且 $t>1$。这与条件 $gcd(a, n) = 1$ 相矛盾，因此 $gcd(b, n)=1$。

下面开始证明欧拉定理：

假设小于 $n$ 且与 $n$ 互质的数的集合为 $A=\{t_1, t_2 \dots, t_{\varphi(n)}\}$，这个集合也叫做模 $n$ 的**简化剩余系**（reduced residue system）。将集合中的每个元素乘以 $a$ 得到$B=\{at_1, at_2 \dots, at_{\varphi(n)}\}$，因为 $n$ 和 $a$ 互质，所以集合 $B$ 中每个元素都与 $n$ 互质。

设 $at_i$ 与 $at_j$ 为 $B$ 中任意两个元素（$0 < i < j \leq \varphi(n)$），这两个元素的差为 $a(t_j-t_i)$，因为 $a$ 与 $p$ 互质，所以 $a(t_j-t_i)$ 不可能是 $n$ 的倍数，因此 $B$ 中任意两个元素除以 $p$ 有不同的余数。

设 $B$ 中每个元素除以 $p$ 得到的余数集合是 $R=\{r_1, r_1, ..., r_{\varphi(n)}\}$，因为 $B$ 中的每个元素与 $n$ 互质，按照开始证明的结论，可知 $R$ 中的每个元素也与 $n$ 互质，而且 $R$ 中的每个元素都小于 $n$，因此集合 $R$ 与 $A$ 含有相同的元素。

$$
\displaystyle {
\begin{array}{rcrcr}
t_1\cdot a & \equiv & r_1 {\pmod p} \\
t_2 \cdot a & \equiv & r_2 {\pmod p} \\
& ...\\
t_{\varphi(n)} \cdot a & \equiv & r_{\varphi(n)} {\pmod p} \\
\end{array}}
$$

将上述等式两边相乘得到：

$$ t_1\cdot t_2 \dots \cdot t_{\varphi(n)} \cdot a^{\varphi(n)} \equiv  r_1 \cdot r_2 \dots \cdot r_{\varphi(n)} \equiv  t_1\cdot t_2 \dots \cdot t_{\varphi(n)} {\pmod p}$$

令 $W = t_1\cdot t_2 \dots \cdot t_{\varphi(n)} {\pmod p}$，上述等式简化为

$$ W \cdot a^{\varphi(n)} \equiv W {\pmod p}$$

因为 $p$ 为质数，所以 $gcd(W, p) = 1$，因此根据模算数的消除率，等式两边消去 $W$ 得到

$$ a^{\varphi(n)}\equiv 1{\pmod {p}} $$

上面的证明过程与费马小定理的证明过程非常相似。实际上当 n 为质数时，因为 $\varphi (n)=n-1$，所以有：

$$ a^{n-1}\equiv 1{\pmod {n}} $$

这就是费马小定理的公式，因此费马小定理其实就是欧拉定理的特殊情况。

## 模 n 的本原根
对于模数 $n$ 的每一个互质数 $a$ ，都存在一个整数 $k$ 满足

$$ g^k\equiv a{\pmod {n}} $$

那么就称 $g$ 为**模 $n$ 的本原根** (primitive root modulo n)。

例子：
3 是模 7 的本原根。
$$
\displaystyle {
\begin{array}{rcrcr}
3^1 & = & 3 & \equiv & 3 {\pmod 7} \\
3^2 & = & 9  & \equiv & 2 {\pmod 7} \\
3^3 & = & 27 & \equiv & 6 {\pmod 7} \\
3^4 & = & 81 & \equiv & 4 {\pmod 7} \\
3^5 & = & 243 & \equiv & 5 {\pmod 7} \\
3^6 & = & 729 & \equiv & 1 {\pmod 7} \\
3^7 & = & 2187 & \equiv & 3 {\pmod 7} \\
\end{array}}
$$

不是每个数都有本原根。只有当 $n$ 等于 $2, 4, p^k, 2p^k$，其中 $p$ 为奇质数时，$n$ 才有本原根。

当 $n$ 有本原根时，本原根的个数为 $\varphi (\varphi(n))$。这个后面可以通过群论来证明。

没有一个公式可以直接求出模 $n$ 的本原根，只有一些算法可以加快寻找本原根的速度。