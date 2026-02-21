PORT = 443

# name -> secret (32 hex chars)
USERS = {
    "tg":  "f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6"
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
TLS_DOMAIN = "www.google.com"
