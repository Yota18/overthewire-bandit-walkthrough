## Level 11 -> 12

### Goal
The password is stored in `data.txt`, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions (ROT13).

### Steps
1.  Use `cat` to view `data.txt`.
2.  Use `tr` to perform ROT13 translation (A-Z -> N-Z, A-M, and same for lowercase).
    ```bash
    cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
    ```
3.  Password obtained: `7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4`

### Command Explanation
*   `tr`: Translate characters. `tr 'A-Za-z' 'N-ZA-Mn-za-m'` swaps each letter with the one 13 positions away.

---

## Level 12 -> 13

### Goal
The password is stored in `data.txt`, which is a hexdump of a file that has been repeatedly compressed.

### Steps
1.  Create a working directory in `/tmp` (e.g., `/tmp/yourname123`).
    ```bash
    mkdir /tmp/yoga123 && cp data.txt /tmp/yoga123 && cd /tmp/yoga123
    ```
2.  Use `xxd -r` to revert the hexdump to binary.
    ```bash
    xxd -r data.txt > data.bin
    ```
3.  Use `file` to check the compression type (`gzip`, `bzip2`, `tar`).
4.  Decompress repeatedly based on the file type.
    *   If gzip: `mv file file.gz` then `gunzip file.gz`.
    *   If bzip2: `mv file file.bz2` then `bunzip2 file.bz2`.
    *   If tar: `tar -xMf file`.
5.  Repeat until you get ASCII text.
6.  Password obtained (Level 13): `FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn`
7.  Logout and login as `bandit13`.

### Command Explanation
*   `xxd -r`: Converts hexdump back to binary.
*   `gzip`, `bzip2`, `tar`: Compression/decompression tools.

---

## Level 13 -> 14

### Goal
The password for the next level is stored in `/etc/bandit_pass/bandit14` and can only be read by user `bandit14`. You are provided with a private SSH key to login as `bandit14` without a password.

### Steps
1.  In the home directory, you will find `sshkey.private`.
2.  Use this key to login to `bandit14` (localhost).
    ```bash
    ssh -i sshkey.private bandit14@localhost -p 2220
    ```
3.  Once logged in, read the password from `/etc/bandit_pass/bandit14`.
    ```bash
    cat /etc/bandit_pass/bandit14
    ```
4.  Password obtained: `fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq`

### Command Explanation
*   `-i keyfile`: Specifies the identity file (private key) for SSH authentication.

---

## Level 14 -> 15

### Goal
The password is retrieved by submitting the password of the current level to port 30000 on localhost.

### Steps
1.  Use `nc` (netcat) to connect to port 30000.
    ```bash
    nc localhost 30000
    ```
2.  Send the current password (`fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq`).
3.  The server will respond with the new password.
4.  Password obtained: `jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt`

### Command Explanation
*   `nc`: Utility to read and write data across network connections (TCP/UDP).

---

## Level 15 -> 16

### Goal
The password is retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption.

### Steps
1.  Use `openssl s_client` for SSL connection.
    ```bash
    openssl s_client -connect localhost:30001
    ```
2.  Send the current password (`jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt`).
3.  The server responds with the new password.
4.  Password obtained: `JQttkNJtISi6doDnLC3qFCTCNJ905e6b`

### Command Explanation
*   `openssl s_client`: Generic SSL/TLS client for debugging.

---

## Level 16 -> 17

### Goal
The password is retrieved by submitting the password of the current level to a port between 31000 and 32000 that uses SSL.

### Steps
1.  Scan for open ports using `nmap`.
    ```bash
    nmap -p 31000-32000 localhost
    ```
2.  Find the open port (usually 31790).
3.  Connect using SSL.
    ```bash
    openssl s_client -connect localhost:31790
    ```
4.  Send the current password. The server will return a new SSH Private Key, not a regular password.
5.  Save this key to a file (e.g., `key17.private`) and set permissions to 600 (`chmod 600 key17.private`).
6.  Use the key to login to `bandit17`.

### Command Explanation
*   `nmap`: Network Mapper, used for port scanning.
*   `chmod 600`: Sets permissions so only the owner can read/write (required for SSH keys).

---

## Level 17 -> 18

### Goal
The password is stored in a file `passwords.new`, which is the only line that has been changed between `passwords.old` and `passwords.new`.

### Steps
1.  Use `diff` to compare the two files.
    ```bash
    diff passwords.old passwords.new
    ```
2.  The output shows the difference. The line marked with `>` is the new one.
3.  Password obtained: `x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO` (example value).

### Command Explanation
*   `diff`: Compares files line by line.

---

## Level 18 -> 19

### Goal
The password is stored in a file `readme` in the home directory. However, `.bashrc` is configured to log you out immediately upon login.

### Steps
1.  When running SSH, append the command you want to execute directly at the end. This bypasses the interactive shell startup script.
    ```bash
    ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"
    ```
2.  Password obtained: `cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8`

### Command Explanation
*   `ssh user@host "cmd"`: Executes a remote command without opening a full interactive shell.

---

## Level 19 -> 20

### Goal
Use the setuid binary `bandit20-do` to read a password file that cannot be read by the current user.

### Steps
1.  The binary `bandit20-do` runs with `bandit20` privileges.
2.  Use it to read the password file.
    ```bash
    ./bandit20-do cat /etc/bandit_pass/bandit20
    ```
3.  Password obtained: `0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO`

### Command Explanation
*   `setuid`: A special bit on binary files that allows users to run the file with the permissions of the file owner (in this case, `bandit20`).

---

## Level 20 -> 21

### Goal
The setuid binary `suconnect` will connect to a local port and verify the current password before giving the new one.

### Steps
1.  Run `nc` (netcat) as a listener in one terminal (or in background).
    ```bash
    echo -n 'CURRENT_PASSWORD' | nc -l -p 1234 &
    ```
2.  Run `./suconnect` pointing to that port.
    ```bash
    ./suconnect 1234
    ```
3.  `suconnect` connects to your listener, verifies the password you sent, and sends back the new password.
4.  Password obtained: `EeoULMCra2q0dSkYj561DX7s1CpBuOBt`

### Command Explanation
*   `nc -l -p`: Listen mode on a specific port.

---
