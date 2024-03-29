---
title: 密码学-02-群论基础
date: 2021-02-26 23:25:46
categories:
- Math
tags:
- Number Theory  
mathjax: true
---

群论（Group  Theory）研究名为**群**的代数结构，群论是抽象代数（Abstract Algebra）中的核心概念，它是其它代数结构的基础，例如：环、域、向量空间等，可以看成是在群之上，增加运算符和公理约束而产生的。

<!--more-->

## 群的定义

群（Group）是由一个集合以及一个二元运算所组成。集合和二元运算必须符合 4 个**群公理**才能被称之为群。

假设有一个二元运算符"$·$"，符号"$·$"并不代表乘法，它只是一个符号，可以代表任何二元运算，例如加、减、乘、除。它结合任何两个元素 $a$ 和 $b$ 而形成另一个元素，记为$a · b$。

对于一个集合 $G$，以及二元运算符"$·$"，如果满足以下四个**群公理**：

1. **封闭性（Closure）**：对于所有 $G$ 中的 $a$、$b$，运算 $a·b$ 的结果也在G中。
2. **结合性（Associativity）**：对于所有 $G$ 中的 $a$、$b$、$c$，等式 $(a·b)·c = a·(b·c)$ 成立。
3. **存在单位元（Identity element）**：$G$ 中存在一个元素 $e$，使得对于 $G$ 中的任意元素 $a$，等式 $e·a = a·e = a$ 成立。
4. **存在逆元（Inverse element）**：对于每个 $G$ 中的 $a$，存在 $G$ 中的一个元素 $b$ 使得 $a·b = b·a = e$，这里的 $e$ 是单位元。

则称集合 $G$，以及二元运算符"$·$"，构成一个群，用符号表示为 $(G, ·)$。也可以简写成 $G$，通过上下文来区分 $G$ 到底代表群还是集合。

例子：所有整数的集合  $\mathbb Z$ 与加法运算构成一个群。因为：

- 封闭性：对于任何两个整数 $a$ 和 $b$，它们的和 $a + b$ 也是整数。满足封闭性。
- 结合性：对于任何整数 $a$, $b$ 和 $c$，$(a + b) + c = a+(b + c)$。满足结合性。
- 存在单位元：如果 $a$ 是任何整数，那么 $0 + a = a + 0 = a$。因此单位元为 $0$。
- 存在逆元：对于任何整数 $a$，与 $-a$ 相加等于单位元 $0$。$-a$ 就是 $a$ 的逆元。

## 群的阶

群 $G$ 的**阶**（order）定义为群所含元素的个数，用符号表示为： $|G|$ 或 $ord(G)$。

如果 $G$ 的元素为无限个，则称为**无限群**，其阶为无限大。如果元素为有限个，则称为**有限群**。

群里面的元素也定义了阶，群里面任意元素 $a$ 的阶定义为最小的正整数 $m$，使得 $a^m=e$，其中 $e$ 为群的单位元。如果这样的正整数 $m$ 不存在，则表示 $a$ 的阶为无限大。元素 $a$ 的阶用符号表示为：$|a|$ 或 $ord(a)$。

## 子群

给定群 $G$，如果集合 $H \subseteq G$，且 $H$ 中包含了单位元，$H$ 中每个元素的逆元也在 $H$ 中，则称 $H$ 为 $G$ 的**子群**（subgroup）。

因为 $H$ 存在单元和逆元，其封闭性和结合性直接继承了$G$，它满足了群的四个公理，因此它就是一个群。

## 求幂
给定群 $(G, ·)$，对任意一个元素 $a$ 应用 $n$ 次运算符“$·$”，表示为

$$a^n = \underbrace {a·a·a \dots · a} _{n 次}$$

$a^n$ 叫做 $a$ 的 $n$ 次幂。注意定义在群 $(G, ·)$ 上的 $a^n$ 不能单纯的理解为平时所见的乘方。它表示在一个元素上对抽象的二元运算的重复多次使用。

例如当 $G$ 表示定义在加法上的群时，$a^n = a + a + \dots + a$。

## 阿贝尔群

阿贝尔群（abelian group）是一种特殊的群，除了满足普通群的四个公理，阿贝尔群还需要满足一个额外的公理：交换性。

**交换性（Commutativity）**：对于 $G$ 中任意两个元素 $a$，$b$ 满足 $a·b = b·a$。

## 循环群

循环群（cyclic group）是指能由群中的某个元素做幂运算而生成的群。

定义：设 $(G, ·)$ 为一个群，若存在一个 $G$ 内的元素 $g$，使得 ${G=\{g^{k}; k\in \mathbb {Z}\}}$，则称 $G$ 关于运算 “$·$” 形成一个**循环群**。$g$ 叫做群的**生成元**。

循环群也分为有**限循环群**和**无限循环群**。若 $G$ 为 $g$ 生成的 $n$ 阶有限循环群，那么集合 $G$ 可以写成 $\{e, g, g^2, g^3, \dots , g^{n-1}\}$。其中 $e=g^0=g^n$，$e$ 为群的单位元。

对群 $G$ 里面的任一元素 $a$ 不断求幂都可以生成一个群，用符号 $\langle a\rangle$ 表示。$\langle a\rangle$ 既可能是有限群，也有可能是无限群。

性质 1：$\langle a\rangle$ 一定是 $G$ 的子群。因为根据群运算的封闭性，$\langle a\rangle$ 中的每个元素都属于 $G$。

性质 2：$\langle a\rangle$ 一定是循环群，$a$ 就是它的一个生成元，元素 $a$ 的阶等于 $\langle a\rangle$ 的阶。

性质 3：当 $\langle a\rangle$ 是有限群时，$\langle a\rangle$ 可以写成 $\{e, a, a^2, a^3, \dots , a^{m-1}\}$，其中 $m=ord(a)=ord(\langle a\rangle)$。当 $m = ord(G)$ 时，有 $\langle a\rangle = G$，此时 $a$ 就是 $G$ 的生成元。

性质 4：循环群的每个子群一定也是循环群。

性质 5：所有循环群都是阿贝尔群。

## 循环群元素的阶

设 $G$ 为 $g$ 生成的 $n$ 阶有限循环群。 $G$ 的任一元素可以表示为 $g^k$（$0 \leq k \leq {n-1}$），$g^k$ 的阶由以下公式给出：

$$ ord(g^k) = \frac{n}{gcd(k, n)}  $$

证明：

设 $ord(g^k)=m$，根据元素阶的定义有 $e=(g^k)^m=g^{km}$。由于 $g$ 为 $G$ 的生成元，因此 $km$ 必须为 $n$ 的倍数，即 $n \mid km$。

求 $ord(g^k)$ 的问题，变成了求最小的 $m$，使得 $n \mid km$。

设 $t=gcd(k, n)$，如果 $n \mid km$，那么消去公约数 $t$ 后，左右两个数依然是倍数关系，也即是 $\frac{n}{t} \mid \frac{k}{t}m$。由于 $gcd(\frac{k}{t}, \frac{n}{t})=1$，即两个数互质，那么要使 $\frac{n}{t} \mid \frac{k}{t}m$ 成立，$m$ 必须是 $\frac{n}{t}$ 的倍数，所以 $m$ 最小值为 $\frac{n}{t}$，也就是 $m=ord(g^k)=\frac{n}{gcd(k, n)}$。证毕。

## 有限循环群生成元的个数

$n$ 阶有限循环群生成元的个数为 $\varphi(n)$。

证明：

设 $g^k$（$0 \leq k \leq {n-1}$）为 $n$ 阶有限循环群 $G$ 的任一元素。要使 $g^k$ 为 $G$ 的生成元。需要满足 $ord(g^k) = ord(G) = n$。由于 $ord(g^k)=\frac{n}{gcd(k, n)}$，因此需要满足

$$ ord(g^k) = \frac{n}{gcd(k, n)}=n  $$

那么有 $gcd(k, n)=1$，也就是说 $k$ 与 $n$ 互质。由于 $k < n$，小于 $n$ 且与 $n$ 互质的数个数由欧拉函数 $\varphi(n)$ 给出。

## 拉格朗日定理

拉格朗日定理（lagrange's theorem）给出了群与子群之间阶的关系：设 $H$ 是有限群 $G$ 的一个子群，则 $H$ 的阶整除 $G$ 的阶。也可以表示为 $ord(H) \mid ord(G)$。

推论1：设 $g$ 是有限群 $G$ 的一个元素，则 $g$ 的阶整除 $G$ 的阶。

证明：

因为由 $g$ 生成的循环群是 $G$ 的子群，且这个循环子群的阶就是 $g$ 的阶。所以 $g$ 的阶整除 $G$ 的阶。

推论2：阶为质数的群都是循环群。

证明：

因为质数不可分解，因此群元素的阶要么等于1，要么等于群的阶。如果群的阶大于1，那么除了单位元以外，其它元素的阶都等于群的阶。只要存在元素的阶等于群的阶，那么这个群就是循环群。因此阶为质数的群都是循环群，除了单位元的所有元素都是这个群的生成器。

推论3：费马小定理是拉格朗日定理的一个简单推论。

证明：

质数 $p$ 互质同余类，构成一个整数模 $p$ 乘法群 $\mathbb Z _p^*$，$\mathbb Z _p^*$ 的阶为 $p-1$。

设 $a \in \mathbb Z _p^*$，且 $a$ 的阶为 $m$，根据元素阶的定义有 $a^m \equiv 1$。

根据拉格朗日定理，$a$ 的阶 $m$ 可以整除 $\mathbb Z _n^*$ 的阶 $p-1$。设 $p-1 = km$，$k$ 为正整数。则有
$$ a^{p-1} \equiv a^{km} \equiv (a^m)^k \equiv 1^k \equiv 1 \pmod{p} $$
