---
title: 密码学-07-欧拉函数乘积公式推导
categories:
- Math
tags:
- Eluer's totient function
mathjax: true
---

之前[《数论基础》](https://chenliang.org/2021/02/25/foundations-of-number-theory/) 一文介绍了欧拉函数，并且给出了欧拉函数的乘积公式，但是并没有给出推导过程。本文主要讲解如何一步一步推导出欧拉函数的乘积公式。

<!--more-->

在推导之前，我们先来回顾一下欧拉函数的乘积公式。对于正整数 $n$，设其质因数分解为如下形式：

$$n = p_1^{e_1}p_2^{e_2} \dots p_k^{e_k}$$

则 $\varphi (n)$ 可通过如下乘积公式计算：

$$ \varphi (n)=n\prod_{i=1}^{k}\left(1-{\frac {1}{p_i}}\right) $$

推导这个公式，需要用到欧拉函数的几个性质。

**性质1**：如果整数 $m$，$n$ 互质，那么 $\varphi(mn) = \varphi(m)\varphi(n)$。

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
r_1 & = a \bmod m \\
r_2 & = a \bmod n
\end{aligned}
$$

> 小知识："$x \bmod y$" 表示 $x$ 除以 $y$ 求余数。例如 $3 = 11 \bmod 4$。

由于 $gcd(a, mn)=1$，因此有 $gcd(a, m)=1$，以及 $gcd(a, n)=1$。由此可以得到 $gcd(r_1, m)=1$，以及 $gcd(r_2, n)=1$。如果把 $r_1$ 和 $r_2$ 组成一个二元组 $(r_1, r_2)$，那么这个二元组是集合 $B$ 中的一个元素。

因此由集合 $A$ 中任一元素 $a$ 通过上述方式生成的二元组 $(r_1, r_2)$ 是集合 $B$ 中的一个元素。

下面我们需要证明两点：

1. 集合 $A$ 中的每个元素，都对应着 $B$ 中的不同的元素。
2. 集合 $B$ 中的每个元素，在 $A$ 中都有对应的元素。





