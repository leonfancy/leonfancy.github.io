---
title: 密码学-05-中国剩余定理
date: 2021-05-15 23:05:59
categories:
- Math
tags:
- CRT
mathjax: true
---

中国剩余定理（Chinese Remainder Theorem）是一个关于一元线性同余方程组的定理。这是数论中一个很重要的定理，在密码学中经常会用到，可用于破解 DHKE 和 RSA 算法。

<!--more-->

中国剩余定理定义： 设有 $k$ 个正整数：$n_1$，$n_2$，...，$n_k$，并且他们两两互质。对于任意的整数 $a_1$，$a_2$，...，$a_k$，下列一元线性同余方程组有解。 设 $N=\prod_{i=1}^k n_i$，方程组小于 $N$ 的解有且只有一个，且方程组任意两个解 $x_1$，$x_2$ 模 $N$ 同余。

$$\quad \left\{ \begin{matrix} x \equiv a_1 \pmod {n_1} \\ x \equiv a_2 \pmod {n_2} \\ \vdots \qquad\qquad\qquad \\ x \equiv a_k \pmod {n_k} \end{matrix} \right.$$

## 证明

首先证明方程组的任意两个解模 $N$ 同余。

设 $x_1$，$x_2$ 是方程组的两个解，对于任意 $n_i$，它必定整除 $x_1 - x_2$，由于 $n_i$ 两两互质，因此他们的乘积 $N$ 也整除 $x_1 - x_2$。因此方程组的任意两个解模 $N$ 同余，小于 $N$ 的解只有一个。

接下来证明方程组有解。

设 $N_i = N/n_i$，由于 $n_1$，$n_2$，...，$n_k$ 两两互质，因此有 $gcd(N_i, n_i)=1$。对于每一对 $N_i$、$n_i$，根据裴蜀定理（Bézout's identity），存在整数 $t_i$、$k_i$，使得 $t_iN_i + k_in_i=1$。由于 $t_iNi = 1 - k_in_i$，因此有 $t_iN_i \equiv 1 \pmod{n_i}$，$t_i$ 也被称为 $N_i$ 模 $n_i$ 的数论倒数，可以记为 $N_i^{-1} \pmod {n_i}$。

接下来我们证明下面的等式是方程组的一个解：

$$x=\sum_{i=1}^k a_i t_i N_i$$

对任意 $n_i$，只要 $j \ne i$，那么 $n_i$ 整除 $N_j$，因此有 $a_j t_j N_j \equiv 0 \pmod{n_i}$。由此可以得到：

$$x=\sum_{i=1}^k a_i t_i N_i = a_i t_i N_i + \sum_{j \ne i}^k a_j t_j N_j \equiv a_i t_i N_i \pmod{n_i}$$

又因为之前我们得到 $t_iN_i \equiv 1 \pmod{n_i}$，因此有：

$$x \equiv a_i t_i N_i \equiv a_i \pmod{n_i}$$

也就是说 $x=\sum_{i=1}^k a_i t_i N_i$ 满足方程组里面的每一个方程，因此它就是方程组的一个解。之前我们证明了任意两个解模 $N$ 同余。因此方程组的通解可表示为：

$$x=rN + \sum_{i=1}^k a_i t_i N_i$$

其中 $r$ 为任意整数。 通解也可以写作如下形式：

$$x \equiv \sum_{i=1}^k a_i t_i N_i \pmod N$$

## 历史

中国剩余定理出自于中国南北朝时期（公元5世纪）的数学著作《孙子算经》卷下第二十六题，叫做“物不知数”问题，原文如下：

> 有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二。问物几何？

《孙子算经》中首次提到了同余方程组问题，因此在中文数学文献中也会将中国剩余定理称为**孙子定理**。

1801 年，数学家高斯在他出版的《Disquisitiones Arithmeticae》一书中，正式定义了同余的概念，并且发明了同余符号 $\equiv$。在这本书中高斯也写到了中国同余定理，并且给出了一元线性同余方程组的一般解法，上文证明中给出的方程组通解就出自于高斯这本书。

**参考文献**
[1] Bézout's identity: https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity
[2] Chinese remainder theorem: https://en.wikipedia.org/wiki/Chinese_remainder_theorem
