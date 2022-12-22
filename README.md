## 自建API

### 简介

​		自用API，

### 壁纸API

#### 获取今日壁纸

```shell
https://api.panghai.top/today?w=1920&h=1080&mkt=zh-CN
```

| 参数名 |   类型   | 是否必要 |        备注        |
| :----: | :------: | :------: | :----------------: |
|   w    |  `Int`   |    否    | 图片宽度，默认1920 |
|   h    |  `Int`   |    否    | 图片高度，默认1080 |
|  uhd   |  `Bool`  |    否    | 是否4k，默认False  |
|  mkt   | `String` |    否    |  地区，默认zh-CN   |

#### 获取随机壁纸

```shell
https://api.panghai.top/random?w=1920&h=1080&mkt=zh-CN
```

| 参数名 |   类型   | 是否必要 |        备注        |
| :----: | :------: | :------: | :----------------: |
|   w    |  `Int`   |    否    | 图片宽度，默认1920 |
|   h    |  `Int`   |    否    | 图片高度，默认1080 |
|  uhd   |  `Bool`  |    否    | 是否4k，默认False  |
|  mkt   | `String` |    否    |  地区，默认zh-CN   |

#### 获取壁纸JSON数据

```shell
https://api.panghai.top/all?page=1&order=asc&limit=10&w=1920&h=1080&mkt=zh-CN
```

| 参数名 |   类型   | 是否必要 |              备注               |
| :----: | :------: | :------: | :-----------------------------: |
|  page  |  `Int`   |    否    |           页数，默认1           |
| limit  |  `Int`   |    否    |   每页数据量，默认10（1-20）    |
|   w    |  `Int`   |    否    |       图片宽度，默认1920        |
|   h    |  `Int`   |    否    |       图片高度，默认1080        |
| order  | `string` |    否    | 排序，默认降序`desc`，升序`asc` |
|  mkt   | `String` |    否    |         地区，默认zh-CN         |

```markdown
// 已知分辨率
resolutions: [
    '1920x1200',
    '1920x1080',
    '1366x768',
    '1280x768',
    '1024x768',
    '800x600',
    '800x480',
    '768x1280',
    '720x1280',
    '640x480',
    '480x800',
    '400x240',
    '320x240',
    '240x320'
]
// 已知国家地区
locations: [
    "de-DE",
    "en-CA",
    "en-GB",
    "en-IN",
    "en-US",
    "fr-FR",
    "it-IT",
    "ja-JP",
    "zh-CN"
]
```

#### 获取壁纸数量

```shell
https://api.panghai.top/total?mkt=zh-CN
```

| 参数名 |   类型   | 是否必要 |      备注       |
| :----: | :------: | :------: | :-------------: |
|  mkt   | `String` |    否    | 地区，默认zh-CN |

### 微博热搜API

#### 获取热搜json数据

```shell
https://api.panghai.top/weibo
```

| 参数名 | 类型 | 是否必要 |  备注   |
| :----: | :--: | :------: | :-----: |
|   无   |  无  |    无    | 无参API |

### B站热搜API

#### 获取热搜json数据

```shell
https://api.panghai.top/bili
```

| 参数名 | 类型 | 是否必要 |  备注   |
| :----: | :--: | :------: | :-----: |
|   无   |  无  |    无    | 无参API |

### 60秒新闻API

#### 获取json数据

```shell
https://api.panghai.top/60s
```

| 参数名 | 类型  | 是否必要 |                             备注                             |
| :----: | :---: | :------: | :----------------------------------------------------------: |
| offset | `int` |    否    | 偏移量（可选参数：0,1,2,3）默认0表示今天，1表示昨天，2表示前天，3表示大前天 |

### OCRAPI

#### 在线识别

```shell
https://api.panghai.top/ocr
```

| 参数名 |   类型   | 是否必要 |                             备注                             |
| :----: | :------: | :------: | :----------------------------------------------------------: |
|  url   | `String` |    是    | 图片地址，要求大小不可以超过512KB，例如：[示例图片](http://i0.hdslb.com/bfs/activity-plat/static/20221213/eaf2dd702d7cc14d8d9511190245d057/lrx9rnKo24.png) |

#### 在线识别

```shell
https://api.panghai.top/ocr/file
```

|     参数名     |   类型   | 是否必要 |                             备注                             |
| :------------: | :------: | :------: | :----------------------------------------------------------: |
|      file      |  `file`  |    是    | 图片文件，要求大小不可以超过512KB，例如：[示例图片](http://i0.hdslb.com/bfs/activity-plat/static/20221213/eaf2dd702d7cc14d8d9511190245d057/lrx9rnKo24.png) |
| content-length | `String` |    否    |       文件字节大小，随便填，但不能超过512*1024=524288        |

### 部署

1、在 [MongoDB](https://www.mongodb.com/cloud/atlas/register) 申请 MongoDB 帐号，具体可查看我的博客教程：[如何申请一个永久免费的 Mongodb 数据库 - 详细版](https://blog.panghai.top/posts/b267/)

2、在[Vercel](https://vercel.com/signup)申请 Vercel帐号

3、创建数据库用户名和密码，在IPAccess List添加`0.0.0.0`（代表允许所有 IP 地址的连接），在 Clusters 页面点击 CONNECT，选择第二个：Connect your application，并记录数据库连接字符串，请将连接字符串中的 `user`修改为数据库用户，`<password>` 修改为数据库密码

3、点击部署<a href="https://vercel.com/import/project?template=https://github.com/flow2000/bing-wallpaper-api/tree/master" target="_blank" rel="noopener noreferrer"><img src="https://vercel.com/button" alt="vercel deploy"></a>

4、进入 Settings - Environment Variables，添加环境变量 `MONGODB_URI`，值为第 3 步的数据库连接字符串

5、进入 Overview，点击 Domains 下方的链接，添加一个子域名，并在域名解析添加一个`CNAME`解析：`cname.vercel-dns.com.`，等待刷新完成即可获得一个`https`的接口