# cryptography-project

Tasked with writing code to test with popular cryptographic algorithms using crypto libraries in Python. We calculate hashes, derive keys from passwords, encrypt and decrypt messages, sign messages and verify message signatures, We also need to derive blockchain addresses from ECC private keys.

## Written with:

<p align="center">
    <img src="https://datawider.com/wp-content/uploads/2019/11/How-to-Learn-Python.jpg" width="600px" alt="python"/>
</p>

## Routes & Desired Inputs/ Outputs
***
### SHA256
#### Route: /crypto1/sha256
`Input- "msg": "exercise-cryptography"`
`Output- "hash": "04d3a0ee287c29c7c78792bfb1af722adcd8996ab3be0780b33e1a907115dff5"`
***
### SHA512
#### Route: /crypto1/sha512
`Input- "msg": "exercise-cryptography"`
`Output- "hash": "87f608f74f0927367b8f6eba375f71599837e0bc146117fdfa8fb577fa33f9780cd6b71a486a9ed4a882ab382240ab693ae77533ee3f12729565cee2277c6a6e"`
***
### RIPEMD160
#### Route: /crypto1/ripemd160
`Input- "msg": "exercise-cryptography"`
`Output- "hash": "e645f7787c1cd9fc8b34c9252f221742c40aaaee"`
***
### HMAC
#### Route: /crypto1/hmac
`Input- "msg": "exercise-cryptography", "key": "secret"`
`Output- "hmac": "9ef1be869d4e20cfa81c2948fdb958521320becb7648d99374115d6f6bcfdd91"`
***
### SCrypt
#### Route: /crypto1/scrypt
`Input- "password": "secret", "salt": "mysalt"`
`Output- "key": "0x2efc82e60de98522ca503e3f79ae0dea906780c263276667ddbe5fd5cb518dd62711d4abe0593274ba893341eb921c6a7cc90f5cb38dce631e3c4bee1086c134"`
***

<p align="center">
    <img src="https://i.pinimg.com/originals/d6/73/46/d673466492dd1d0284008bf8ee19c502.gif" width="600px" alt="python"/>
</p>