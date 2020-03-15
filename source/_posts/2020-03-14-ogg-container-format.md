---
title: Ogg容器格式
date: 2020-03-14 22:34:12
categories:
- Audio Tech
tags:
- Ogg
---

Ogg是[Xiph.Org](https://xiph.org/)基金会推出的一种开源免费的多媒体容器格式。Ogg容器格式可以用于封装音频、视频、字幕、以及多媒体元信息。它既适用于流媒体传输，又能作为文件格式存储多媒体。

<!--more-->

> 容器格式和编码格式有区别。编码指的是将原始多媒体数据按照规定的算法将原始数据进行压缩编码，使其占用的空间更小，方便传输和存储。这个压缩编码的算法就叫做编码格式，例如视频的编码格式有：H.264、H.265（又叫做HEVC）、Theora等等，音频的编码格式有：Vorbis、ACC、FLAC、Opus等等。实现这些压缩编码算法的软件叫做编码器。而容器格式是用来封装编码之后的数据，容器格式提供了分包机制和元信息可以帮助解码器解码，而且容器可以将多种不同的编码数据复合在一起，例如视频、音频、字幕可以封装到一个容器格式里面。常用的容器格式有：MKV、MP4、AVI等等，Ogg也是容器格式一种。

## 1. Ogg 二进制流

多媒体编码器输出的是一串二进制包（Packet），包通常是解码器解码的最小单位。这些包之间通常没有分割标志，如果直接把这些包拼接在一起形成一个二进制流，那么没有任何解码器可以读出其中的包并进行解码，因为解码器将找不到每个包从哪里开始，从哪里结束。

<img src="/images/ogg_container_format/1.png" style="width: 100%; max-width: 500px"/>

Ogg容器格式将多媒体编码器产生的二进制包进行封装，并且提供分割信息，这样解码器就可以通过读取Ogg格式的封装信息，将二进制包一个一个拆出来进行解码。

我们将编码器生成的二进制流称为**逻辑流**（Logical Bitstream），把Ogg封装之后二进制流称为**物理流**（Physical Bitstream）。之所以这么称呼是因为编码生成的裸二进制流实际上无法被任何工具处理，只能存在于逻辑概念，而 Ogg 封装过后的流却是可以被实际操作处理的。

<img src="/images/ogg_container_format/2.png" style="width: 100%; max-width: 500px"/>

Ogg物理流的基本组成单位是 **Ogg 页**（Ogg Page）。编码器输出的二进制包就是按照Ogg格式的规则放到Ogg页中的。Ogg的规范十分灵活，一个Ogg页可以存放一个包、多个包、甚至是一包的一部分。正因为Ogg格式对编码器输出的包大小没有要求，使得Ogg格式可以用于多种视频、音频编码格式的封装。

一个Ogg物理流中可以包含多个逻辑流，例如一个Ogg文件中包含了视频、音频以及字幕三个逻辑流。如果一个Ogg流只有一个逻辑流，那么它称为一个**基础流** （Elementary Bitstream），如果包含多个逻辑流，那么它称为**复合流**（Multiplexed Bitstream）。

多个基础流通过Ogg页交错的方式组合成一个复合流，也就是将不同基础流中同样时间点的Ogg页放到一起。

<img src="/images/ogg_container_format/3.png" style="width: 100%; max-width: 500px"/>

## 2. Ogg 页的格式

Ogg页是Ogg物理流的基本单位。一个Ogg页由头和负载两部分组成，并且总是由`OggS`四个字节开头，这四个字节称为捕获标志（Capture Pattern）。当客户端解码器从中途开始接收服务端推送的流媒体比特流时，搜索到比特流中的第一个`OggS`标志，就可以从这里开始进行比特流的解码。

Ogg页头部格式如下图所示：

<img src="/images/ogg_container_format/4.png" style="width: 100%; max-width: 400px"/>

### 2.1 捕获标志（Capture）

```plain
byte value
 0   0x4f  'O'
 1   0x67  'g'
 2   0x67  'g'
 3   0x53  'S'
```

固定值`OggS`。

### 2.2 版本号（Version）
```plain
byte value
 4   0x4f 
```

Ogg格式的版本号，目前固定为0。

### 2.3 头类型标志（Header Type）

```plain
byte value
 5   bitflags: 0x01: 置0 = 从新的包开始
                     置1 = 这个页里面的包接着上一个页里面的包
               0x02: 置0 = 不是逻辑流的第一个Ogg页
                     置1 = 逻辑流的第一个Ogg页（bos）
               0x04: 置0 = 不是逻辑流的最后一个Ogg页
                     置1 = 逻辑流的最后一个Ogg页（eos） 
```

占一个字节，根据最低的三个比特位是否设置为1表示不同的信息。

这里特别说明一下最低位`0x01`的意义，当一个包太大，导致一个Ogg页放不下，或者Ogg页已经放了很多个包，剩下的位置不够再放一个包，那么一个包就可能横跨两个连续的Ogg页。这个包开头的部分在第一页，后半部分在第二页。这种情况下，第二页的头类型标志的最低位就会置为1。

### 2.4 位置数（Granule Position）

```plain
byte value
 6   0xXX LSB
 7   0xXX
 8   0xXX
 9   0xXX
10   0xXX
11   0xXX
12   0xXX
13   0xXX MSB
```

从上面的字节序可以看出位置数采用小端字节序，这也是Ogg的默认字节序。

每个Ogg页上的位置数表示从这个逻辑流开始，到这个Ogg页上最后一个完结的包所包含的样本数。如果一个包只有开头或中间的一部分在这个Ogg页里面，那么这部分的包含的样本数不计算在位置数里面。

如果这个值为`-1`（以补码表示），那么说明这个页里面没有任何完结的包。

下面用一个例子来说明位置数。一个逻辑流由6个包组成，这个包按照下图的方式封装在4个Ogg页里面形成一个Ogg物理流。
- Ogg页1里面包2是这个页里面最后一个完结的包，从开头的包1开始算起，到这个包2一共有40个样本，因此Ogg页1的位置数为40。
- Ogg页2里面没有任何一个包是在该页结束的，因此位置数为-1。
- Ogg页3里面最后一个完结的包是包4，从开始到包4结尾一共有120个样本数，因此Ogg页3的位置数为120。
- Ogg页4里面最后一个完结的包是包6，从开始到包6结尾一共有160个样本数，因此Ogg页4的位置数为160。

<img src="/images/ogg_container_format/5.png" style="width: 100%; max-width: 600px"/>

对于不同类型的多媒体和编解码器，位置数的含义不一样，例如对于视频来说，它表示帧数，对于音频来说，它表示采样数。

### 2.5 逻辑流编号（Bitstream Serial Number）

```plain
byte value
14   0xXX LSB
15   0xXX
16   0xXX
17   0xXX MSB
```

当多个逻辑流复合在一个Ogg物理流里面时，每个逻辑流都会有一个独特的编号，其对应的Ogg页都打上对应编号，用于区分这个Ogg页属于哪一个逻辑流。


### 2.6 页序列号（Page Sequence No）

```plain
byte value
18   0xXX LSB
19   0xXX
20   0xXX
21   0xXX MSB
```

Ogg流里面每个Ogg页都有一个按顺序增长的序号，这样如果在传输的时候有一页丢失了，解码器可以通过检查序号很快发现丢失的页。

如果一个Ogg物理流里面有多个逻辑流，那么每个逻辑流的Ogg页序列号是独立增长的。

### 2.7 校验和（Checksum）

```plain
byte value
22   0xXX LSB
23   0xXX
24   0xXX
25   0xXX MSB
```

当前整个Ogg页的CRC校验和，计算包括头部数据，只是在计算前将校验和字段的四个字节置为0，计算后将得到的值再设置进去。

计算时，初始值和最后的XOR值为0，generator polynomial 为 0x04c11db7。

### 2.8 分段个数（Page Segments）、分段表（Segment Table）

```plain
byte value
26   0x00-0xff (0-255)
```

```plain
byte value
27   0x00-0xff (0-255)
[...]
n    0x00-0xff (0-255, n=page_segments+26)
```

Ogg格式规定将一个包看成由多个大小为255字节的分段和最后一个可能小于255字节分段组成。例如一个包的大小为702字节，那么可以看是由三个分段组成大小分别为：255、255、192。如果将这个包封装到Ogg页中，那么Ogg头里面的**分段个数**值为3，**分段表**将有三个字节，值分别为：255、255、192。

**分段个数**占一个字节，表示这个Ogg页里面有多少个包的分段。**分段表**的大小由**分段个数**决定，其中每个字节的值代表了对应分段的大小。

这个分段机制为解码器提供了区分包边界的方法，如果分段表中一个值小于255，那么代表这个包已经结束了，下一个分段就代表一个新的包开始。

用一个例子来说明这个机制，下图有三个包存储在了两个Ogg页中。

<img src="/images/ogg_container_format/6.png" style="width: 100%; max-width: 350px"/>

- 包1大小为702字节，可以分成三个段：255、255、192。
- 包2大小为574字节，可以分成三个段：255、255、64。
- 包3大小为638字节，可以分成三个段：255、255、128。

Ogg页1包含整个包1和包2的前两个分段，因此Ogg页1头里面的分段个数字段的值为5，分段表有5个字节，5个字节的值分别为：255、255、192、255、255。当解码器读到分段表中192这个数时，就知道这个包已经结束，可以开始解码包1的数据了。

Ogg页2包含整个包3和包2的最后一个分段，因此Ogg页2头里面的分段个数字段的值为4，分段表有4个字节，4个字节的值分别为：64、255、255、128。并且由于Ogg页2开头的数据是接着上一个Ogg页的，因此它头类型标志最低位将会设置为1。

有种特殊情况，如果一个包大小恰好为255的倍数，例如包大小为510，如果按照上面的分段方法，那么应该分成两段：255、255。但是这样依赖，解码器在分段表里面读到第二个255，并不能判断这个包是不是结束了。为了解决这个问题，Ogg规定在分段表里面插入一个0值，也就是说这个包可以看成分成三个段：255、255、0。解码器读到这个0的时候就知道这个包结束了。这个0值只存在于分段表中，不会真的在负载的包中插入数据。

从上面的分析可以看出Ogg格式对包的分段只是逻辑上的，只是用于计算分段个数和分段表中的值，并不会在负载中的包里面插入任何分隔符。

由于分段个数只占一个字节，它的最大值为255，分段表中每个分段值也只占一个字节，对应的分段大小最大为255字节。因此一个Ogg页的最大有效负载为 255 * 255 = 65025 字节，这种情况下，Ogg页的头大小为 ：27（固定大小） + 255（分段表大小） = 282 字节。整个Ogg页最大的长度为 65025 + 282 = 65307。

这个逻辑上的分段机制可以看出，虽然Ogg页的大小有限制，但是对于多媒体编码器输出的包大小没有限制，大于65025字节的包可以分开在多个连续的Ogg页里面存储，分段机制保证了解码器可以识别到包的开始和结尾。

## 3. Ogg 媒体类型定义

针对Ogg格式，Xiph.Org在IANA注册了三种MIME类型。分别是：
- application/ogg
- video/ogg
- audio/ogg

在标准制定的早期，Ogg专门用来封装Vorbis编码格式的语音，并且在[RFC3534](https://tools.ietf.org/html/rfc3534)中定义了`application/ogg`类型来指代封装在Ogg格式中的Vorbis语音。不过随着技术的发展，Ogg被单独提出来作为一种可以封装任意媒体类型的容器格式。于是[RFC3534](https://tools.ietf.org/html/rfc3534)草案被废弃，在新的草案[RFC5334](https://tools.ietf.org/html/rfc5334)中重新定义了`application/ogg`的意义，并且定义了`video/ogg`和`audio/ogg`两种新的类型。

**video/ogg**

当一个Ogg流的主要信息是视频（可能包括音频和字幕），那么传输的时候应当使用`video/ogg`类型。存储成文件时应当使用`.ogv`扩展名。

**audio/ogg**

当一个Ogg流的主要信息是音频（可能包括字幕），那么传输的时候应当使用`audio/ogg`类型。存储成文件时应当使用`.oga`扩展名。

因为历史原因，Ogg格式的音频数据存储成文件时，也可以使用`.ogg`和`.spx`扩展名。`.ogg`表示音频编码格式是Vorbis；`.spx`表示音频编码格式是Speex。

**application/ogg**

当一个Ogg流非常复杂，不是单纯的视频或者音频，例如传输多路视频信号，这种情况下就建议使用`application/ogg`类型。存储文件使用`.ogx`扩展名。

对于这些MIME类型，还可以指定`codec`参数来表示Ogg流中的数据编码格式。例如传输Opus格式语音就可以使用：`audio/ogg; codecs=opus`。目前支持的codec可以参考https://wiki.xiph.org/index.php/MIMETypesCodecs。

-------------------

**参考文献：**
[1] Ogg bitstream overview: https://www.xiph.org/ogg/doc/oggstream.html
[2] Ogg logical bitstream framing: https://www.xiph.org/ogg/doc/framing.html
[3] Ogg: https://en.wikipedia.org/wiki/Ogg
[4] Ogg Media Types: https://tools.ietf.org/html/rfc5334
[5] Specification of MIME types and respective codecs parameter: https://wiki.xiph.org/index.php/MIMETypesCodecs
[6] The application/ogg Media Type: https://tools.ietf.org/html/rfc3534
[7] The Ogg Encapsulation Format Version 0: https://tools.ietf.org/html/rfc3533









