---
title: 密码学-07-欧拉函数乘积公式推导
tags:
  - Eluer's totient function
categories:
  - Math
mathjax: true
date: 2021-06-10 14:48:15
---


之前[《数论基础》](https://chenliang.org/2021/02/25/foundations-of-number-theory/) 一文介绍了欧拉函数，并且给出了欧拉函数的乘积公式，但是并没有给出推导过程。本文主要讲解如何一步一步推导出欧拉函数的乘积公式。

<!--more-->

在推导之前，我们先来回顾一下欧拉函数的乘积公式。对于正整数 $n$，设其质因数分解为如下形式：

$$n = p_1^{e_1}p_2^{e_2} \dots p_k^{e_k}$$

则 $\varphi (n)$ 可通过如下乘积公式计算：

$$ \varphi(n) = n\prod_{i=1}^{k}\left(1-{\frac {1}{p_i}}\right) $$

推导这个公式，需要用到欧拉函数的几个性质。

**性质1：如果整数 $m$，$n$ 互质，那么 $\varphi(mn) = \varphi(m)\varphi(n)$。**

证明：

首先我们构造两个集合。

$$
\begin{aligned}
A & = \{a: 1 \leq a \leq mn, \gcd(a, mn)=1 \} \\
B & = \{(b, c): 1 \leq b \leq m, \gcd(b, m)=1; 1 \leq c \leq n, \gcd(c, n)=1\}
\end{aligned}
$$

其中集合 $B$ 里面的元素是一个二元组。例如 $m = 3$，$n = 4$，那么集合 $A$ 和 $B$ 分别是：

$$
\begin{aligned}
A & = \{1, 5, 7, 11\} \\
B & = \{(1, 1), (1, 3), (2, 1), (2, 3)\}
\end{aligned}
$$

取 $A$ 中的任一元素 $a$，分别除以 $m$ 和 $n$ 求余数：

$$
\begin{aligned}
a & \bmod m = r_1 \\
a & \bmod n = r_2
\end{aligned}
$$

> **小知识**："$x \bmod y$" 表示 $x$ 除以 $y$ 求余数。例如 $11 \bmod 4 = 3$。

由于 $gcd(a, mn)=1$，因此有 $gcd(a, m)=1$，以及 $gcd(a, n)=1$。由此可以得到 $gcd(r_1, m)=1$，以及 $gcd(r_2, n)=1$。如果把 $r_1$ 和 $r_2$ 组成一个二元组 $(r_1, r_2)$，那么这个二元组是集合 $B$ 中的一个元素。

因此由集合 $A$ 中任一元素 $a$ 通过上述方式生成的二元组 $(r_1, r_2)$ 是集合 $B$ 中的一个元素。

下面我们需要证明两点：

1. 集合 $A$ 中的每个元素，都对应着 $B$ 中的不同的元素。
2. 集合 $B$ 中的每个元素，在 $A$ 中都有对应的元素。

先来证明第 1 点，假设集合 $A$ 两个不同的元素 $a_1$、$a_2$ 对应着集合 $B$ 中的同一个二元组 $(b, c)$。那么有

$$
\begin{aligned}
a_1 & \equiv a_2 \pmod m \\
a_1 & \equiv a_2 \pmod n
\end{aligned}
$$

根据同余性质有：$m \mid (a_1 - a_2)$，以及 $n \mid (a_1 - a_2)$。 又因为 $gcd(m, n)=1$，所以有：$mn \mid (a_1 - a_2)$。

根据集合 $A$ 的定义，其中所有的元素都小于 $mn$。因此只有当$a_1 = a_2$ 时，才能满足 $mn \mid (a_1 - a_2)$。这与 $a_1 \neq a_2$ 的假设相矛盾。

因此可以证明: 集合 $A$ 中的每个元素，都对应着 $B$ 中的不同的元素。

下面我们来证明第 2 点。

任取集合 $B$ 中的一个元素 $(b, c)$。找到一个数 $x$, 模 $m$ 与 $b$ 同余，模 $n$ 与 $c$ 同余。写成同余方程组如下所示。

$$
\left\{ \begin{aligned} 
x & \equiv b \pmod m \\ 
x & \equiv c \pmod n
\end{aligned} \right.
$$

由于 $gcd(m, n)=1$，根据[中国剩余定理](https://chenliang.org/2021/05/15/chinese-remainder-theorem/)，该方程组有解，且在小于 $mn$ 的范围内只有一个解。由于 $gcd(b, m)=1$， $gcd(c, n)=1$，根据同余关系有 $gcd(x, m)=1$， $gcd(x, n)=1$，因此有 $gcd(x, mn)=1$。因此方程的解 $x$ 一定是集合 $A$ 中的一个元素。

因此可以证明: 集合 $B$ 中的每个元素，在 $A$ 中都有对应的元素。

通过上述证明，可以知道集合 $A$ 与集合 $B$ 的元素个数相同。根据上诉集合的定义，集合 $A$ 的元素个数为 $\varphi(mn)$，集合 $B$ 的元素个数为 $\varphi(m)\varphi(n)$。因此我们就证明了 $\varphi(mn) = \varphi(m)\varphi(n)$。

通过这个性质可以看出欧拉函数是一个**乘性函数**（Multiplicative Function）。可以扩展这个性质到更一般的场景，假设有 $k$ 个两两互质的数：$n_1, n_2, \dots, n_k$，那么有$\varphi(n_1 n_2 \dots n_k) = \varphi(n_1)\varphi(n_2) \dots \varphi(n_k)$。

**性质2：设 $p$ 是质数，则 $\varphi(p^k) = p^k - p^{k-1}$。**

证明：

小于等于 $p^k$ 且与 $p^k$ 不互质的数一定是 $p$ 的倍数，他们是

$$1p, 2p, 3p, \dots, p^2, (p+1)p, \dots, (p^{k-1})p$$

一共有 $p^{k-1}$ 个。因此小于 $p^k$ 且与 $p^k$ 互质的数的个数，也就是 $\varphi(p^k) = p^k - p^{k-1}$。

根据前面这两个性质，我们就可以推导欧拉函数的乘积公式了。假设整数 $n$ 的质因数分解为如下形式 

$$n = p_1^{e_1}p_2^{e_2} \dots p_k^{e_k}$$

根据上面两个性质可得

$$
\begin{aligned}
\varphi(n) & = \varphi(p_1^{e_1}p_2^{e_2} \dots p_k^{e_k}) \\
           & = \varphi(p_1^{e_1})\varphi(p_2^{e_2}) \dots \varphi(p_k^{e_k}) \\
           & = (p_1^{e_1} - p_1^{e_1-1})(p_2^{e_2} - p_2^{e_2-1}) \dots (p_k^{e_k} - p_k^{e_k-1}) \\
           & = p_1^{e_1}(1 - \frac{1}{p_1})p_2^{e_2}(1 - \frac{1}{p_2}) \dots p_k^{e_k}(1 - \frac{1}{p_k}) \\
           & = p_1^{e_1}p_2^{e_2} \dots p_k^{e_k}(1 - \frac{1}{p_1})(1 - \frac{1}{p_2}) \dots (1 - \frac{1}{p_k}) \\
           & = n\prod_{i=1}^{k}\left(1-{\frac {1}{p_i}}\right)
\end{aligned}
$$

由此我们得到了欧拉函数的乘积公式。为了计算方便，我们通常使用下列两种形式的乘积公式：

$$\varphi(n) = (p_1^{e_1} - p_1^{e_1-1})(p_2^{e_2} - p_2^{e_2-1}) \dots (p_k^{e_k} - p_k^{e_k-1})$$

或者

$$\varphi(n) = n\prod_{i=1}^{k}\left(1-{\frac {1}{p_i}}\right)$$

可以看出，要计算 $\varphi(n)$ 的值，必须对 $n$ 做质因数分解。当 $n$ 含有特别大的质因数时，分解 $n$ 将会十分困难，此时求解 $\varphi(n)$ 也会十分困难。RSA 密码正是利用了 $\varphi(n)$ 的这一性质，从而十分安全。

**参考文献**
[1] Multiplicative Function：https://en.wikipedia.org/wiki/Multiplicative_function
[2] 数论概论（原书第4版），约瑟夫H.西尔弗曼: https://book.douban.com/subject/26863822/
