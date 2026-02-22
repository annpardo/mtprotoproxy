import os

# 端口，默认 443
PORT = int(os.environ.get("PORT", 443))

# 用户配置：环境变量 USERS 格式为 "name:secret;name2:secret2"
users_env = os.environ.get("USERS", "tg:00000000000000000000000000000001")
USERS = {}
for item in users_env.split(";"):
    if ":" in item:
        name, secret = item.split(":")
        USERS[name.strip()] = secret.strip()

# 模式配置：通过 CLASSIC / SECURE / TLS 三个布尔环境变量控制
MODES = {
    "classic": os.environ.get("CLASSIC", "False").lower() == "true",
    "secure": os.environ.get("SECURE", "False").lower() == "true",
    "tls": os.environ.get("TLS", "True").lower() == "true",
}

# TLS 域名，默认 None
TLS_DOMAIN = os.environ.get("TLS_DOMAIN", None)

# 广告标签，必须是字符串，默认空字符串，避免 None 报错
AD_TAG = os.environ.get("AD_TAG", "")
