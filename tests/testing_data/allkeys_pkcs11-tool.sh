pkcs11-tool --module ./librtpkcs11ecp.so --keypairgen --key-type GOSTR3410-2001:A --pin 12345678 --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --hash --id 10 --mechanism GOSTR3411 -i in.txt -o hash.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410-WITH-GOSTR3411 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410-WITH-GOSTR3411 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type pubkey --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type privkey --id 10

pkcs11-tool --module ./librtpkcs11ecp.so --keypairgen --key-type GOSTR3410-2001:B --pin 12345678 --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --hash --id 10 --mechanism GOSTR3411 -i in.txt -o hash.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410-WITH-GOSTR3411 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410-WITH-GOSTR3411 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type pubkey --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type privkey --id 10

pkcs11-tool --module ./librtpkcs11ecp.so --keypairgen --key-type GOSTR3410-2001:C --pin 12345678 --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --hash --id 10 --mechanism GOSTR3411 -i in.txt -o hash.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410-WITH-GOSTR3411 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410-WITH-GOSTR3411 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type pubkey --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type privkey --id 10

pkcs11-tool --module ./librtpkcs11ecp.so --keypairgen --key-type GOSTR3410:A --pin 12345678 --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --hash --id 10 --mechanism GOSTR3411 -i in.txt -o hash.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410-WITH-GOSTR3411 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410-WITH-GOSTR3411 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type pubkey --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type privkey --id 10

pkcs11-tool --module ./librtpkcs11ecp.so --keypairgen --key-type GOSTR3410:B --pin 12345678 --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --hash --id 10 --mechanism GOSTR3411 -i in.txt -o hash.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410-WITH-GOSTR3411 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410-WITH-GOSTR3411 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type pubkey --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type privkey --id 10

pkcs11-tool --module ./librtpkcs11ecp.so --keypairgen --key-type GOSTR3410:C --pin 12345678 --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --hash --id 10 --mechanism GOSTR3411 -i in.txt -o hash.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410-WITH-GOSTR3411 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410-WITH-GOSTR3411 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type pubkey --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type privkey --id 10

pkcs11-tool --module ./librtpkcs11ecp.so --keypairgen --key-type GOSTR3410-2012-256:A --pin 12345678 --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --hash --id 10 --mechanism GOSTR3411-12-256 -i in.txt -o hash.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410-WITH-GOSTR3411-12-256 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410-WITH-GOSTR3411-12-256 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type pubkey --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type privkey --id 10

pkcs11-tool --module ./librtpkcs11ecp.so --keypairgen --key-type GOSTR3410-2012-256:B --pin 12345678 --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --hash --id 10 --mechanism GOSTR3411-12-256 -i in.txt -o hash.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410-WITH-GOSTR3411-12-256 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410-WITH-GOSTR3411-12-256 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type pubkey --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type privkey --id 10

pkcs11-tool --module ./librtpkcs11ecp.so --keypairgen --key-type GOSTR3410-2012-256:C --pin 12345678 --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --hash --id 10 --mechanism GOSTR3411-12-256 -i in.txt -o hash.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410-WITH-GOSTR3411-12-256 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410-WITH-GOSTR3411-12-256 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type pubkey --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type privkey --id 10

pkcs11-tool --module ./librtpkcs11ecp.so --keypairgen --key-type GOSTR3410-2012-256:D --pin 12345678 --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --hash --id 10 --mechanism GOSTR3411-12-256 -i in.txt -o hash.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410-WITH-GOSTR3411-12-256 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410-WITH-GOSTR3411-12-256 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type pubkey --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type privkey --id 10

pkcs11-tool --module ./librtpkcs11ecp.so --keypairgen --key-type GOSTR3410-2012-512:A --pin 12345678 --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --hash --id 10 --mechanism GOSTR3411-12-512 -i in.txt -o hash.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410_512 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410_512 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410-WITH-GOSTR3411-12-512 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410-WITH-GOSTR3411-12-512 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type pubkey --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type privkey --id 10

pkcs11-tool --module ./librtpkcs11ecp.so --keypairgen --key-type GOSTR3410-2012-512:B --pin 12345678 --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --hash --id 10 --mechanism GOSTR3411-12-512 -i in.txt -o hash.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410_512 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410_512 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410-WITH-GOSTR3411-12-512 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410-WITH-GOSTR3411-12-512 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type pubkey --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type privkey --id 10

pkcs11-tool --module ./librtpkcs11ecp.so --keypairgen --key-type GOSTR3410-2012-512:C --pin 12345678 --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --hash --id 10 --mechanism GOSTR3411-12-512 -i in.txt -o hash.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410_512 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410_512 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --sign --id 10 --mechanism GOSTR3410-WITH-GOSTR3411-12-512 -i hash.txt -o sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 --verify  --id 10 --mechanism GOSTR3410-WITH-GOSTR3411-12-512 --input-file  hash.txt --signature-file sign.txt
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type pubkey --id 10
pkcs11-tool --module ./librtpkcs11ecp.so --pin 12345678 -b --type privkey --id 10
