---
title: 密码学-04-离散对数问题与Diffie-Hellman密钥交换
date: 2021-05-09 22:30:09
categories:
- Math
tags:
- DHKE
mathjax: true
---

在现代密码学中，许多算法都利用了数学上的难题。**离散对数问题**与**大数分解问题**这两个数学难题是非对称密码学的两块基石。本文着重介绍离散对数问题，以及它在 Diffie-Hellman 密钥交换协议当中的应用。

<!--more-->

## 离散对数问题

在实数中**对数** $x=\log_a b$ 是指对于给定的实数 $a$ 和 $b$，有一个数 $x$，使得$a^x = b$。**离散对数**与此类似，但是它是定义在群（Group）上的。

**定义**：给定群 $G$，设 $g, h \in G$，且有等式 $h = g^x$，那么求解 $x$，就是离散对数问题（Discrete Logarithm Problem）。$x$ 称为 $h$ 以 $g$ 为底的离散对数，用符号表示为 $\log_g h$，或者 $DL_g(h)$。

设元素 $g$ 的生成子群表示为 $\langle g \rangle$，那么当 $h \in \langle g \rangle$ 时，离散对数问题才有解。

> 注意这里 $g^x$，代表定义在 $G$ 上的群运算对元素 $g$ 作用 $x$ 次。

离散对数问题在一些群上很容易计算，例如在整数加法群上，求解离散对数相当于做整数除法。但是在一些特殊的群上，求解离散对数相当困难。

密码学中离散对数问题常用的群是基于质数 $p$ 的**整数模 $p$ 乘法群** $\mathbb Z_p^*$（或者写作 $(\mathbb{Z}/p\mathbb{Z})^*$）。求解离散对数的难度，跟 $p$ 的大小以及 $\mathbb Z_p^*$ 的子群结构有关系。

> 如果对群论和 $\mathbb Z_p^*$ 不熟悉，可以参考我之前写的两篇文章：
> 1. [密码学-02-群论基础](https://chenliang.org/2021/02/26/group-theory)
> 2. [密码学-03-整数模 n 乘法群](https://chenliang.org/2021/03/04/multiplicative-group-of-integers-modulo-n)

## 快速幂模运算

幂模运算有一种快速计算方法，叫做**逐次平方法**（Exponentiation by squaring 或者 binary exponentiation），或者直接叫做**快速幂模运算**。

计算 $g^x \pmod p$，其算法如下：

1. 将指数 $x$ 做二进制展开，其中每个 $x_i$ 要么是 0 要么是 1：
$$x = x_0 + x_1·2^1 + x_2·2^2 + \dots + x_r·2^r$$

2. 使用逐次平方求出做模 $p$ 的 $g$ 的幂次表。
$$
\displaystyle {
\begin{array}{rclcl}
g^1 & \equiv & & & G_0 \pmod p \\
g^2 & \equiv & G_0^2 & \equiv & G_1 \pmod p \\
g^4 & \equiv & G_1^2 & \equiv & G_2 \pmod p \\
& ...\\
g^{2^r} & \equiv & G_{r-1}^2 & \equiv & G_r \pmod p \\
\end{array}
}
$$
   可以看到，在计算 $G_i$ 的时候，是用之前计算出的 $G_{i-1}$ 求平方，再对 $p$ 取模，参与计算的数始终不会大于 $p$，这大大简化了计算。这一步的算法复杂度是 $O(\log p)$。

3. 最终计算下列乘积得到 $g^x$
$$g^x \equiv G_0^{x_0} \cdot G_1^{x_1} \cdot G_2^{x_2} \cdots  G_r^{x_r} \pmod p$$
   因为 $x_i$ 可以能为 0 或 1，上面这个乘积实际上是所有 $x_i$ 为 1 的哪些 $G_i$ 的乘积。这一步的算法复杂度也是 $O(\log p)$。

使用逐次平方法平方法可以使幂模运算的时间复杂度达到 $O(\log p)$，因此幂模运算使用经典计算机可以很高效的计算。

基于离散对数的非对称密码系统，利用了如下性质：给定 $g$ 和 $x$，做**幂模运算**（modular exponentiation）很快，即计算 $h=g^x \pmod p$ 很简单，但是给定 $g$ 和 $h$，求解**离散对数** $x=\log_gh$ 却很困难。所以一般将 $x$ 作为私钥，将 $h$ 作为公钥，即便别人知道了 $h$ 和 $g$，也无法求出 $x$。

## Diffie-Hellman 密钥交换

离散对数问题一个典型的应用就是 Diffie-Hellman 密钥交换协议（Diffie-Hellman Key Exchange），简称 DHKE。使用这个协议，通信双方可以在完全没有对方任何预先信息的条件下，通过不安全信道创建起一个密钥。这个密钥只有通信双方知道，其他人无法获得，可以在后续的通信中作为对称密钥来加密通信内容。

下面我们来看看基于 $\mathbb Z_p^*$ 的 DHKE 是如何工作的。假设通信双方叫做 Alice 与 Bob，并且 Alice 作为通信的发起方。

第一步：Alice 告诉 Bob，她选取的群 $\mathbb Z_p^*$ 的参数：$p$ 和 $g$。其中 $g$ 为 $\mathbb Z_p^*$ 某个子群的生成元。为了安全性，子群 $\langle g \rangle$ 的阶要尽可能为一个大质数。

第二步：Alice 选取一个整数 $a$，计算 $A \equiv g^a \pmod p$，并将 $A$ 发送给 Bob。同时，Bob 选取一个整数 $b$，计算 $B \equiv g^b \pmod p$，并将 $B$ 发送给 Alice。

第三步：Bob 收到 $A$ 之后，计算 $S \equiv A^b \equiv (g^a)^b \equiv g^{ab}$。同样 Alice 收到 $B$ 之后，计算 $S \equiv B^a \equiv (g^b)^a \equiv g^{ab}$。这个 $S$ 就是通过 DHKE 协议建立起来的密钥。

下图详细展示了 DHKE 的协议流程。

![DHKE 协议流程](/images/discrete_logarithm_problem_and_dhke/dhke.svg)

从非对称密码系统的角度理解，$p$ 和 $g$ 是公钥，可以在不安全的信道中传输，$a$ 是 Alice 的私钥，只有 Alice 知道，$b$ 是 Bob 的私钥，只有 Bob 知道。通过协议生成的密钥 $S$，Alice 和 Bob 都知道，但是其他人无法通过信道上传输的信息计算得到 $S$。

攻击者想要得到密钥 $S$，就需要计算 $S \equiv g^{ab} \pmod p$，攻击者可以从公共信道上获取 $p$ 和 $g$，但是由于 $a$ 和 $b$ 分别是 Alice 和 Bob 私钥，攻击者无法直接获得。不过攻击者可以从信道上获取 $A$ 和 $B$，通过 $A \equiv g^a \pmod p$ 来计算得到 $a$，同理也可以得到 $b$。

已知 $g$、$p$、$A$，通过 $A \equiv g^a \pmod p$ 求解得到 $a$，就是在群 $\mathbb Z_p^*$ 上解离散对数问题。当 $p$ 足够大，且子群 $\langle g \rangle$ 的阶也为够大的质数时（例如 1024 比特的大数），求解这个离散对数将会非常困难。因此攻击者想要通过公共信息计算得到密钥 $S$ 会非常困难，求解离散对数的复杂度保证了 DHKE 的安全。

离散对数当前的破解记录是由法国的数学家团队于 2019 年 12 月 2 日发布的，该团队破解了在 $p$ 的大小为 240 个十进制位（795 比特位）的离散对数问题。以 Intel Xeon Gold 6130 CPU（运行于2.1GHz）为参考，他们方法计算离散对数需要消耗 3100 个内核年（core-year）。鉴于此，目前建议使用 2048 比特位的 DHKE。

**参考文献：**

[1] Discrete logarithm: https://en.wikipedia.org/wiki/Discrete_logarithm
[2] Discrete logarithm records: https://en.wikipedia.org/wiki/Discrete_logarithm_records
[3] Diffie–Hellman key exchange: https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
[4] 数论概论（原书第4版），约瑟夫H.西尔弗曼，第 16 章: https://book.douban.com/subject/26863822/
