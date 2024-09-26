const crypto = require('crypto')
import crypto1 from 'crypto'
const crypto2 = require('crypto').createCipheriv

import { createCipheriv } from 'crypto'

// ruleid: weak-symmetric-mode
crypto2('AES-128-CBC', key, iv)
// ok: weak-symmetric-mode
crypto.createCipheriv('AES-128-GCM', key, iv)
// ruleid: weak-symmetric-mode
crypto.createCipheriv('AES-128-ECB', key, iv)
// ok: weak-symmetric-mode
crypto.createCipheriv('abf', key, iv)
// ruleid: weak-symmetric-mode
crypto.createDecipheriv("DES-EDE3-CBC", key, iv);

// ruleid: weak-symmetric-mode
crypto2('AES-128-CBC', key, iv)
// ok: weak-symmetric-mode
crypto1.createCipheriv('AES-128-GCM', key, iv)
// ruleid: weak-symmetric-mode
crypto1.createCipheriv('AES-128-ECB', key, iv)
// ruleid: weak-symmetric-mode
crypto1.createDecipheriv("DES-EDE3-CBC", key, iv);

// ruleid: weak-symmetric-mode
createCipheriv('AES-128-ECB', key, iv)
// ruleid: weak-symmetric-mode
createCipheriv('DES-EDE3-CBC', key, iv)
// ok: weak-symmetric-mode
createCipheriv('AES-128-GCM', key, iv)
