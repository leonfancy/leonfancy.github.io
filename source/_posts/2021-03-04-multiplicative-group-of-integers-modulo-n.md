---
title: 密码学-03-整数模 n 乘法群
date: 2021-03-04 22:59:12
categories:
- Math
tags:
- Group Theory  
mathjax: true
---

在同余理论中，模 $n$ 的互质同余类构成一个乘法群，称为**整数模 n 乘法群**（multiplicative group of integers modulo n）。表示为 $\mathbb Z _n^*$，或者 $\mathbb Z _n^\times$、$(\mathbb{Z}/n\mathbb{Z})^*$、$(\mathbb{Z}/n\mathbb{Z})^\times$。这个群是数论的基石，在密码学、整数分解和素性测试中均有运用。

<!--more-->

## 整数模 n 乘法群的元素

$\mathbb Z _n^*$ 是一个有限群。其集合中每个元素不是一个单一整数，而是一个同余类，整数 $a$ 模 $n$ 的同余类表示为 $\overline{a}_n$ 或者 $[a]_n$。

如果 $a\equiv b{\pmod {n}}$，那么 $gcd(a, n) = gcd(b, n)$。也就是说一个数 $a$ 如果与 $n$ 互质，那么 $[a]_n$ 里面所有的数都与 $n$ 互质。因此我们可以从 $\mathbb Z _n^*$ 中的每个同余类里面抽出一个数来代表对应的同余类。例如 $n = 8$，我们可以将 $\mathbb Z _n^*$ 写成下面任意一种形式

$\mathbb Z _8^* = \{1, 3, 5, 7\}$
$\mathbb Z _8^* = \{9, 11, 13, 15\}$
$\mathbb Z _8^* = \{1, 3, 29, 87\}$

通常我们用每个同余类中最小的正整数来表示那个类，这样形成的集合也叫做**最小简约余数系**。上面提到的 $\mathbb Z _8^* = \{1, 3, 5, 7\}$ 就是这样一个例子。

后面我们都用模 $n$ 的**最小简约余数系**来代表群 $\mathbb Z _n^*$ 的集合。

## 证明

只要证明 $\mathbb Z _n^*$ 是一个群，只需要证明它满足群的四大公理即可。

**封闭性**：如果 $ gcd(a, n) = 1 $ 和 $ gcd(b, n) = 1 $，那么 $ gcd(ab, n) = 1 $，因此封闭性成立。

**结合性**：由于整数乘法的属性，群的结合性自然成立。

**存在单位元**：1 与任何数互质，$\mathbb Z _n^*$ 总是包含 1 的同余类，因此 1 的同余类为**单位元**。

**存在逆元**：整数模 $n$ 乘法群的逆元定义为对于给定集合中的整数 $a$，逆元 $x$ 满足 $ ax\equiv 1{\pmod {n}} $。找出逆元 $x$ 等价于求解方程 $ax + kn = 1$。根据裴蜀定理，因为$gcd(a,n)=1$，所以一定存在$x$，$k$ 使改方程成立。且 $x$ 与 $n$ 互质，所以 $a$ 的逆元 $x$ 也属于该群。

##当 $\mathbb Z _n^*$ 为循环群

$\mathbb Z _n^*$ 不一定是循环群。$\mathbb Z _n^*$ 为循环群的条件为：$n$ 等于 $1$、$2$、$4$、$p^k$ 或者 $2p^k$，其中 $p$ 是奇质数，$k$ 为正整数。

当 $\mathbb Z _n^*$ 为循环群时，其生成元的个数为 $\varphi (\varphi (n))$，也就是说模 $n$ 的本原根的个数为 $\varphi (\varphi (n))$。

证明：

在前一篇文章中我们证明了，有限循环群 $G$ 中的任一元素 $g^k$ 的阶可表示为

$$ ord(g^k) = \frac{|G|}{gcd(k, |G|)}  $$

因此要使 $g^k$ 为生成元，必须满足 $gcd(k, |G|)=1$。因此 $G$ 中生成元的个数为 $\varphi (|G|)$。

欧拉函数 $\varphi (n)$ 给出了小于 $n$ 且与 $n$ 互质的数的个数。因此可知 $\mathbb Z _n^*$ 的阶就为 $\varphi (n)$。由此可以得到 $\mathbb Z _n^*$ 生成元的个数为 $\varphi (\varphi(n))$。

## 当 n 为质数

当 $n$ 为质数时，我们通常用 $p$ 来表示 $n$。可以证明 $\mathbb Z _p^*$ 总是循环群。其生成元的个数为 $\varphi (\varphi (p)) = \varphi (p-1)$。

如果 $d$ 能整除 $p-1$，那么 $\mathbb Z _p^*$ 中存在 $\varphi (d)$ 个 $d$ 阶的生成器。

**例子：当 $p = 13$ 时。**

当 $p = 13$ 时，我们可以求出 $\mathbb Z_{11}^*$  的阶为 $\varphi (13)=12$。

由于 $\mathbb Z_{13}^*$ 的阶 $12=2 \times 2 \times 3$，因此能整除 12 的数有：1，2，3，4，6，12。$\mathbb Z_{13}^*$ 一定存在子群的阶等于这些数。而且 $\mathbb Z_{13}^*$ 子群的阶只可能是这些数中的一个。我们可以计算出对于每个阶，有几个生成元：

- 1 阶：$\varphi (1)=1$，有 1 个。
- 2 阶：$\varphi (2)=1$，有 1 个。
- 3 阶：$\varphi (3)=2$，有 2 个。
- 4 阶：$\varphi (4)=2$，有 2 个。
- 6 阶：$\varphi (6)=2$，有 2 个。
- 12 阶：$\varphi (12)=4$，有 4 个。

其中 $\varphi (12)$ 为 $\mathbb Z_{13}^*$ 生成元的个数。

把各阶的生成元个数加起来，$1 + 1 + 2 + 2 + 2 + 4$ 正好等于 $12$。这是因为 $\mathbb Z_{13}^*$ 中每个元素的阶是唯一的，因此每个子群的生成元个数加起来恰好等于 $\mathbb Z_{13}^*$ 元素的个数。这也从侧面证明了欧拉函数的一个性质：**所有能整除 $n$ 的数的欧拉函数和为 $n$**。表示为：

$$ \sum _{d\mid n}\varphi (d)=n $$

其中 $d$ 为所有能整除 $n$ 的数。

为了验证我们的结果，下面给出了 $\mathbb Z_{13}^*$ 中每个元素生成的子群和阶：

|  $a$ |   $\langle a\rangle$             | $ord(a)$ |
| :----| :--------------------------------| :------- |
| 1    |   { 1 }                          |  1       |
| 2    |   { 2,4,8,3,6,12,11,9,5,10,7,1 } |  12      |
| 3    |   { 3,9,1 }                      |  3       |
| 4    |   { 4,3,12,9,10,1 }              |  6       |
| 5    |   { 5,12,8,1 }                   |  4       |
| 6    |   { 6,10,8,9,2,12,7,3,5,4,11,1 } |  12      |
| 7    |   { 7,10,5,9,11,12,6,3,8,4,2,1 } |  12      |
| 8    |   { 8,12,5,1 }                   |  4       |
| 9    |   { 9,3,1 }                      |  3       |
| 10   |   { 10,9,12,3,4,1 }              |  6       |
| 11   |   { 11,4,5,3,7,12,2,9,8,10,6,1}  |  12      |
| 12   |   { 12,1 }                       |  2       |


另外可以看到一个有意思的性质：**元素 $p-1$ 的阶始终为 2**。这是因为 $(p-1)^2 = p^2 - 2p + 1 \equiv 1\pmod{p}$。

由于质数 p 的 $\mathbb Z _p^*$在密码学中更为常用，因此我们后面着重讨论这个群。

## 寻找生成元

通过上述分析，给我们寻找 $\mathbb Z_p^*$ 的生成元一些启发。一个简单的想法是，从 $a = 2$ 开始，到 $a = p - 2$ 结束，对每个数 $a$，测试对于每个小于且能整除 $p-1$ 的数 $d$，如果都满足 $a^d \not\equiv 1$，那么就认为这个数 $a$ 是生成元。

但是这种方法中找出每个小于且能整除 $p-1$ 的数 $d$ 比较麻烦，需要先将 $p-1$ 做质因数分解，再将这些质因数排列组合求乘积，还要考虑去重。

有一个更简单的方式是将 $p-1$ 做质因数分解得到 $p-1={q_1}^{k_1}{q_2}^{k_2}\dots {q_r}^{k_r}$，其中$q_1, q_2, \dots, q_r$ 是 $p-1$ 的所有不同质因数。对于元素 $a$，我们只需要测试

$$a^\frac{p-1}{q_i} \not\equiv 1，其中1 \leq i \leq r$$

对于每个不同质因数 $q$ 都满足上述条件的话，元素 $a$ 就是生成元。虽然这个算法，对每个数的测试变少了。但是这个算法的难点在于**对于一个很大的数 $p$，分解 $p-1$ 的质因数将会非常困难**。

### 如何挑选数来测试

如果我们的任务是只需要找到一个生成元，那么该如何从 $\mathbb Z_p^*$ 挑选数来做上面提到的测试呢。一个简单的办法是从 2 开始，一个一个测试，直到找到一个为止。

还有一种方法是随机从 $\mathbb Z_p^*$ 里面挑选一个。那么随机挑中一个的概率有多大呢？我们知道生成元的个数为 $\varphi (p-1)$，而 $\mathbb Z_p^*$ 元素的总个数为 $p-1$。因此选中的概率为：

$$P = \frac{\varphi (p-1)}{p-1}$$

设 $p-1$ 做质因数分解得到 $p-1={q_1}^{k_1}{q_2}^{k_2}\dots {q_r}^{k_r}$，根据欧拉函数的乘法公式得到：

$$P = (1-\frac{1}{q_1})(1-\frac{1}{q_2}) \dots (1-\frac{1}{q_r})$$

从上述公式可以观察到，如果 $p-1$ 的质因数 $q$ 越大，那么随机选中生成元的概率就越大。

例如 $p = 13$，$p - 1 = 12 =2^2 \times 3$，因此随机挑选到生成元的概率为 $(1-\frac{1}{2})(1-\frac{1}{3})=\frac{1}{3}$。

### 找到余下的生成元

只要找到一个生成元，我们可以通过另一种方法来找到剩下的生成元。假如我们找到 $a$ 为生成元，根据循环群的性质，其它的生成元一定可以表示为 $a^k$，根据前面的公式我们可以得到 $a^k$ 的阶为

$$ ord(a^k) = \frac{|\mathbb Z_p^*|}{gcd(k, |\mathbb Z_p^*|)} = \frac{p-1}{gcd(k, p-1)} $$

因此 $a^k$ 要想为生成元，它的阶 $ord(a^k)$ 必须等于 $p-1$，那么 $k$ 与 $p-1$ 必须互质，也就是 $gcd(k, p-1)=1$。

对于 $p = 13$ 的例子来说，当我们测试得到 2 为生成元后，我们找出所有与 12 互质的数为：5、7、11，由此可以求出其它 3 个生成元：

$2^5=32 \equiv 6$
$2^7=32 \equiv 11$
$2^{11}=32 \equiv 7$

虽然这个方法看起来很简单，但是找出所有小于且与 $p-1$ 互质的数还是很困难。

**参考文献**

[1] The multiplicative group modulo p: https://www.di-mgt.com.au/multiplicative-group-mod-p.html
[2] CYCLICITY OF $(\mathbb{Z}/p\mathbb{Z})^\times$: https://kconrad.math.uconn.edu/blurbs/grouptheory/cyclicmodp.pdf
