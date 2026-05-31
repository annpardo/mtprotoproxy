# Async MTProto Proxy 中文说明

English: [README.en.md](README.en.md)

这是一个使用 Python 编写的异步 MTProto Proxy，部署简单，适合用于搭建 Telegram MTProxy。

## 功能说明

* 支持 MTProto Proxy 常用模式：classic、secure、tls

* 默认启用 tls 模式，兼容性和隐蔽性更好

* 支持通过 `config.py` 配置端口、用户密钥和广告 tag

* 支持 Docker / docker-compose 部署

* 也支持不使用 Docker，直接运行 Python 脚本

* 支持多个实例运行，客户端会自动在实例之间均衡

* 支持 Prometheus 运行统计导出

## 快速开始

1. 克隆仓库：

```bash
git clone https://github.com/annpardo/mtprotoproxy.git
cd mtprotoproxy
```

2. 修改 `config.py`

建议至少修改：

* `PORT`：代理监听端口
* `USERS`：用户名称和 32 位十六进制密钥
* `AD_TAG`：频道推广 tag，可选

3. 使用 Docker 启动：

```bash
docker-compose up -d
```

4. 查看日志和代理链接：

```bash
docker-compose logs
```

安装演示：

![安装演示](https://camo.githubusercontent.com/a6cc16b9bf53c16579b45c8d29d270a63e9d70fd698cfd0fb4dcb25295ecf022/68747470733a2f2f616c6578626572732e636f6d2f6d7470726f746f70726f78792f696e7374616c6c5f64656d6f5f76322e676966)

## 不使用 Docker 运行

也可以直接运行：

```bash
python3 mtprotoproxy.py
```

如果需要指定配置文件：

```bash
python3 mtprotoproxy.py config.py
```

## 配置说明

`PORT`：MTProxy 对外监听端口。

`USERS`：用户和 secret 配置。secret 需要是 32 位十六进制字符串，例如：

```python
USERS = {
    "tg": "0123456789abcdef0123456789abcdef",
}
```

`MODES`：启用的代理模式。

```python
MODES = {
    "classic": False,
    "secure": False,
    "tls": True,
}
```

`TLS_DOMAIN`：tls 模式使用的伪装域名。默认配置中可以不写，程序会使用默认值。

`AD_TAG`：频道推广 tag，可从 `@MTProxybot` 获取。不做频道推广时可以不配置。

## 频道推广

如果需要给 Telegram 频道做推广，先向 `@MTProxybot` 获取 tag，然后填入 `config.py` 的 `AD_TAG`。

## 性能说明

原项目说明中提到，在 1 核 CPU、1024MB 内存的 VDS 上，性能大约可以支撑 4000 个同时在线用户。实际效果取决于服务器网络、CPU、系统限制和代理使用情况。

## 高级用法

项目还支持：

* 使用自定义配置文件启动

* 同时运行多个实例

* 安装 `uvloop` 获得额外性能提升

* 将运行统计导出到 Prometheus

更多高级配置可以参考原项目 Wiki。
