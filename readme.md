我的博客使用了 [HEXO](https://hexo.io/) 框架。主题使用的是 [Apollo](https://github.com/pinggod/hexo-theme-apollo)。

当前部署状态：[![Build Status](https://travis-ci.org/leonfancy/leonfancy.github.io.svg?branch=hexo)](https://travis-ci.org/leonfancy/leonfancy.github.io)

## Setup
安装 hexo 命令：
```
npm install -g hexo-cli
```

下载我的博客源代码，并且安装依赖
```
git clone git@github.com:leonfancy/blog.git
cd blog
npm install 
```

## 写博客

创建新博客：
```
hexo new post <title>
```
这将会在`source/_posts`目录下创建新的博客文件。然后就可以在这个文件里面编辑博客正文了。

本地预览博客，执行如下命令：
```bash
hexo server 
```

### 博客元信息

在每篇博客的开头部分写入元信息（指定标题、日期、类别等等），例如：

```
---
title: Ogg容器格式
date: 2020-03-14 22:34:12
categories:
- Audio Tech
tags:
- Ogg
---
```

### LaTex 数学公式

使用了 [hexo-filter-mathjax](https://github.com/stevenjoezhang/hexo-filter-mathjax) 插件，在服务端渲染 LaTex 公式。如果文章需要渲染公式，则在元信息部分添加`mathjax: true`参数。

为了更好的渲染公式，把渲染引擎从 hexo-renderer-marked 改成了 hexo-renderer-pandoc。

## 发布

直接提交代码，触发 travis 自动部署。自动将生成的博客静态文件发布到 GitHub
 repo:  [leonfancy.github.io](https://github.com/leonfancy/leonfancy.github.io)。
 
## Todo

- 支持设置图片标题，改变图片尺寸和对齐方式。
