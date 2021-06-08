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

$A = \{a: 1 \leq a \leq mn, \gcd(a, mn)=1 \}$
$B = \{(b, c): 1 \leq b \leq m, \gcd(b, m)=1; 1 \leq c \leq n, \gcd(c, n)=1\}$

其中集合 $B$ 里面的元素是一个二元组。$m = 3$，$n = 4$，那么集合 $A$ 和 $B$ 分别是：

$A = \{1, 5, 7, 11\}$
$B = \{(1, 1), (1, 3), (2, 1), (2, 3)\}$





