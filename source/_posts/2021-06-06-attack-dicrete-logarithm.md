---
title: 密码学-06-针对离散对数的攻击
date: 2021-06-06 23:48:21
categories:
- Math
tags:
- Discrete Logarithm
mathjax: true
---

许多公钥密码系统都依赖于离散对数计算十分困难的特性，离散对数越难计算，那么密码系统就越安全。离散对数的安全性跟它所基于的群关系非常大，通常来说群的阶越高，计算离散对数越困难。但是除了阶的大小，群本身的结构也会影响离散对数的安全性。

<!--more-->

为了安全性，离散对数通常定义在模 $p$ 乘法群 $\mathbb Z_p^*$ 上，其中 $p$ 为质数。针对离散对数密码系统的攻击，表示找到一种高效的算法，求解 $x$ 使其满足 $g^x \equiv h$，其中 $g$ 为 $\mathbb Z_p^*$ 的生成元，$h \in \mathbb Z_p^*$。本文我们讲解的攻击方法都基于这个群。


## 暴力破解法

将 $x$ 穷举 1 到 $\varphi(p)$，直到找到一个数使 $g^x \equiv h \pmod p$ 成立。由于 $\varphi(p) = p-1$，因此这种算法的复杂度为 $O(p)$。

看起来 $O(p)$ 是一个可以接受的复杂度，但是在密码学中 $p$ 一般会取一个很大的数字，因此我们一般用 $p$ 的二进制位数来衡量复杂度，假如 $p$ 有 $n$ 个二进制位，那么复杂度为 $O(2^n)$，这就是一个指数级的复杂度了。因此暴力破解法是个很低效的办法。对于大于 100 位的数就已经很难解了，对于大于上千位的数，暴力破解法消耗的时间甚至超过了太阳的寿命，因此认为不可解。

## 大步小步法

大步小步法（Baby-Step Giant-Step）是对暴力破解法的一个改进，是算法如下：

1. 计算 $m = \lceil \sqrt{\varphi(p)} \rceil$。
2. 假设 $x=im+j$，其中 $0 \leq i < m$， $0 \leq j < m$。
3. 因此有 $g^x \equiv g^{im+j} \equiv h$，有 $g^j \equiv (g^{-m})^ih$。
4. 对于在 $0 \leq j < m$ 范围内的每个 $j$，计算 $g^j$，并且存储起来。
5. 计算 $g^{-m}$ 的值。
6. 将 $i$ 从 $0$ 到 $m$ 循环，计算 $(g^{-m})^ih$，每计算一次，就查找第 4 步中有没有相等的 $g^j$。如果找到，则退出循环，离散对数的解为 $im+j$。

该算法的时间复杂度和空间复杂度为$O(\sqrt{\varphi(p)})$，也即 $O(\sqrt p)$。虽然比暴力算法快很多，但是当 $p$ 足够大时，该算法也不可解。

算法中对 $j$ 循环一次相当于走了一小步，对 $i$ 循环一次相当于一大步，**大步小步法**因此而得名。

## Pohlig-Hellman 算法

前面两种算法对群的阶没有要求，适用于任何群，但是效率不高，对于阶太大的群不适用。密码学家 Pohlig 与 Hellman 在 1978 年发明一种算法，可以用于破解群的阶为光滑数的离散对数，这个算法以两位作者的名字命名为 **Pohlig-Hellman 算法**。

在理解这个算法之前，先要理解什么是光滑数（Smooth Integer）。

### 光滑数

在数论中，如果一个数的所有质因数都小于等于 B，就称这个数为**B-光滑数**（B-Smooth Integer）。例如 $15750 = 2 × 3^2 × 5^3 × 7$，因此 $15750$ 是一个 7-光滑数。

需要注意的是，一个数被称作是**B-光滑数**，并不需要 B 是这个数的质因数，只需要 B 大于或等于这个数的每一个质因数就行。例如上面的 15750 也可以被叫做 8-光滑数、9-光滑数、11-光滑数，等等。

### 算法思想

设群 $\mathbb Z_p^*$ 的阶为 $n$，根据群的性质可知 $n = \varphi(p) = p - 1$，设其质因数分解为如下形式：

$$n = q_1^{e_1}q_2^{e_2} \dots q_k^{e_k}$$

对如下等式：

$$h \equiv g^x \pmod p$$

我们将两边同时求 $n/q_i^{e_i}$ 次幂得到：

$$h^{\frac{n}{q_i^{e_i}}} \equiv (g^x)^{\frac{n}{q_i^{e_i}}} \pmod p$$

交换一下右边的指数得到：

$$h^{\frac{n}{q_i^{e_i}}} \equiv (g^{\frac{n}{q_i^{e_i}}})^x \pmod p$$

设 $h_i = h^{\frac{n}{q_i^{e_i}}}$，$g_i = g^{\frac{n}{q_i^{e_i}}}$，则有：

$$h_i \equiv g_i^x \pmod p$$

因为 $g_i$ 的阶为 $q_i^{e_i}$，所以上述等式是在一个 $q_i^{e_i}$ 阶的子群上求离散对数，满足等式的解都模$q_i^{e_i}$ 同余，设其中一个解为 $a_i$，则解可以表示为：

$$x \equiv a_i \pmod {q_i^{e_i}}$$

对于 $1 \leq i \leq k$ 的每个 $i$ 都做如上操作，可以得到如下方程组：

$$\left\{ \begin{matrix} 
x \equiv a_1 \pmod {q_1^{e_1}} \\ 
x \equiv a_2 \pmod {q_2^{e_2}} \\ 
\vdots  \\ 
x \equiv a_k \pmod {q_k^{e_k}} 
\end{matrix} \right.$$

利用中国剩余定理，可以求得满足上诉线性方程组的解，方程组的每个解都模所有 $q_i^{e_i}$ 的乘积同余，也即模 $n$ 同余，设其某一个解为 $a$，则通解可以表示如下：

$$x \equiv a \pmod n$$

通过这种方式我们就求得了 $h \equiv g^x \pmod p$ 的解。

在求解 $h_i \equiv g_i^x \pmod p$ 时可以利用大步小步法，时间复杂度为 $O(\sqrt{q_i^{e_i}})$，但是如果$q_i^{e_i}$ 太大，算法效率还是不够高。

好在对于阶为一个质数的幂的情况，有一个效率很高的算法。为了简化符号，令 $q=q_i$，$e=e_i$。将 $x$ 做 $q$ 进制展开：

$$x = x_0 + x_1q + x_2q^2 + \dots + x_{e-1}q^{e-1}$$

其中任意 $x_j$ 满足 $0 \leq x_j < q$。只要想办法求出每个 $x_j$，我们就可以得到 $x$。

令

$$h_j \equiv hg^{-(x_0+x_1q+x_2q^2+ \dots + x_{j-1}q^{j-1})} \pmod p$$

其中 $1 \leq j \leq e - 1$。当 $j = 0$ 时，令

$$h_0=h$$

由此我们可以看到 $h_j$ 满足一个递推的关系：

$$h_{j+1} \equiv h_jg^{-x_jq_j} \pmod p$$

下面我们对 $h_j$ 求 $\frac{n}{q^{j+1}}$ 次幂：

$$
\begin{aligned} 
(h_j) ^ {\frac{n}{q^{j+1}}} &\equiv (hg^{-(x_0+x_1q+x_2q^2+ \dots + x_{j-1}q^{j-1})}) ^ {\frac{n}{q^{j+1}}} \\
& \equiv (g^xg^{-(x_0+x_1q+x_2q^2+ \dots + x_{j-1}q^{j-1})}) ^  {\frac{n}{q^{j+1}}} \\
& \equiv (g^{x_jq^j + x_{j+1}q^{j+1} + \dots + x_{e-1}q^{e-1}}) ^  {\frac{n}{q^{j+1}}} \\
& \equiv (g^{x_jq^j + K_jq^{j+1}}) ^  {\frac{n}{q^{j+1}}}  \qquad (其中 K_j 为一个整数)\\
& \equiv g^{x_j\frac{n}{q}} g^{nK_j} \\
& \equiv g^{x_j\frac{n}{q}} \\
& \equiv (g^{\frac{n}{q}})^{x_j}
\end{aligned}
$$

最终我们得到如下等式

$$(h_j) ^ {\frac{n}{q^{j+1}}} \equiv (g^{\frac{n}{q}})^{x_j} \pmod p$$

其中 $g^{\frac{n}{q}}$ 的阶为 $q$。因此通过上述等式求 $x_j$ 相当于在一个 $q$ 阶的群上求解离散对数，利用大步小步法，其时间复杂度为 $O(\sqrt{q})$。求出所有 $x_j$ 的复杂度为 $O(e\sqrt{q})$，这比之前的复杂度 $O(\sqrt{q^e})$ 要好太多。另外由于计算 $(h_j) ^ {\frac{n}{q^{j+1}}}$ 涉及到升幂操作，可以利用逐次平方，其复杂度为 $O(\log{n})$。

对于 $n$ 的每个因子 $q_i^{e_i}$ 都用上诉算法求解，最终 Pohlig-Hellman 的算法复杂度为

$$O(\sum_i{e_i(\log{n} + \sqrt{q_i}))}$$

从这个复杂度可以看出，只要 $\mathbb Z_p^*$ 的阶是一个 B 足够小的 B-光滑数，使用 Pohlig-Hellman 算法求解离散对数问题将会变得非常简单。

## 防范针对离散对数的攻击

要使离散对数是安全的，首先要保证 $\mathbb Z_p^*$ 的阶足够大。其次，根据 Pohlig-Hellman 算法，$\mathbb Z_p^*$ 的阶还需要至少有一个很大的质因数，也就是在上面的描述中，$q_i$ 中至少有一个数非常大。从群论的角度讲，$\mathbb Z_p^*$ 需要有一个阶非常大的子群。

$\mathbb Z_p^*$ 的阶为 $p-1$，假设它有一个非常大的质因数 $q$，设 $p-1 = cq$，$c$ 为一个整数，且根据质数的性质，$c$ 一定为偶数，这样 $p$ 可以表示为 $p=cq+1$。在设计离散对数的时候，需要精心挑选 $x$，计算 $h = g^x$，使得 $h$ 落入阶为 $q$ 的子群中。这样根据 $g$ 和 $h$，求离散对数 $x$ 才会很困难。有时候为了方便，我们选择的生成元 $g$ 甚至不是 $\mathbb Z_p^*$ 的生成元，而是 $q$ 阶子群的生成元。

### 安全质数

对于 $p=cq+1$ 这种形式的质数，当 $c = 2$ 时，称为**安全质数（Safe Prime）**，也就是质数 $p$ 可以写成 $p=2q+1$ 的形式，其中 $q$ 也为质数，$q$ 也被称为**Sophie Germain 质数（Sophie Germain prime）**。

使用安全质数的群 $\mathbb Z_p^*$，其子群结构非常简单，其子群的阶只可能为：$1$、$2$、$q$、或者 $2q$，其中 $2q$ 实际上为 $\mathbb Z_p^*$ 本身的阶。$2$ 阶子群的生成元只有一个，就是 $p-1$，因为 $(p-1)^2=p^2-2p+1 \equiv 1 \pmod p$。因此，只要随机从 $[2, p-2]$ 选一个数，其要么是 $q$ 阶子群的生成元，要么是 $2q$ 阶子群的生成元。在实际工程应用中，通常选择 $g=2$ 作为生成元，这会使计算 $h=g^x$ 变得很简单。求解离散对数将会是在 $q$ 阶子群或者 $2q$ 阶子群上求解，如果是在 $2q$ 阶子群上求解，攻击者最多只能知道 $x \mod 2$ 的值，能泄露的信息非常少，不足以求解离散对数。

因此使用非常大的安全质数（通常大于1024比特位）将会使离散对数变得十分安全。

**参考文献**
[1] Baby-step giant-step: https://en.wikipedia.org/wiki/Baby-step_giant-step
[2] An Improved Algorithm for Computing Logarithms over GP(p) and Its Cryptographic Significance: https://ee.stanford.edu/~hellman/publications/28.pdf
[3] Smooth number: https://en.wikipedia.org/wiki/Smooth_number
[4] The Pohlig-Hellman Algorithm: http://anh.cs.luc.edu/331/notes/PohligHellmanp_k2p.pdf
[5] Safe and Sophie Germain primes: https://en.wikipedia.org/wiki/Safe_and_Sophie_Germain_primes
[6] How to Backdoor Diffie-Hellman: https://eprint.iacr.org/2016/644.pdf
