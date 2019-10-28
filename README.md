# Usage
```
$ python ./auth.py --help
usage: ./auth.py [-h] [--name NAME]

optional arguments:
  --name NAME  Name of AWS account (default: ALL)
```

```
$ python ./auth.py
DNS 646248
WEB 396959
DX 920731
```

```
$ python ./auth.py --name DNS
031876
```
## Appendix
```
$ scripts_require_MFA.sh < python ./auth.py --name DNS
```

# Setting
```yml
$ cat keys.yml
---
DNS:
  name: DNS
  key: MfaSecretKeyDNS
WEB:
  name: WEB
  key: MfaSecretKeyWEB
DX:
  name: DX
  key: MfaSecretKeyDXX
```