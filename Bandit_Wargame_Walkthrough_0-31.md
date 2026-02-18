# Bandit Wargame Walkthrough (Level 0 - 31)

This guide contains step-by-step solutions for the Bandit wargame from OverTheWire, covering Level 0 to Level 31. Each level is explained with its goal, steps, and command explanations.

## Level 0

### Goal
Log in to the game using SSH. The host to contact is `bandit.labs.overthewire.org` on port 2220. The username is `bandit0` and the password is `bandit0`.

### Steps
1.  Open your terminal.
2.  Run the following command to login via SSH:
    ```bash
    ssh bandit0@bandit.labs.overthewire.org -p 2220
    ```
3.  Enter the password `bandit0` when prompted.

### Command Explanation
*   `ssh`: Secure Shell, a protocol for secure remote login.
*   `-p 2220`: Specifies the destination port (default SSH is 22, Bandit uses 2220).

---

## Level 0 -> 1

![Level 0 Output](images/bandit0_step.png)

### Goal
The password for the next level is stored in a file called `readme` located in the home directory.

### Steps
1.  Check directory contents with `ls`.
2.  Read the `readme` file using `cat`.
    ```bash
    cat readme
    ```
3.  Password obtained: `ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If`
4.  Logout with `exit` and login to Level 1 as `bandit1`.

### Command Explanation
*   `ls`: List directory contents.
*   `cat`: Concatenate and display content.

---

## Level 1 -> 2

![Level 1 Output](images/bandit1_step.png)

### Goal
The password is stored in a file named `-` located in the home directory.

### Steps
1.  A file named `-` cannot be read directly with `cat -` because `-` is interpreted as stdin.
2.  Use a relative path `./` or absolute path.
    ```bash
    cat ./-
    ```
3.  Password obtained: `263JGJPfgU6LtdEvgfWU1XP5yac29mFx`
4.  Logout and login to Level 2.

### Command Explanation
*   `./`: Refers to the current directory, helping distinguish filenames from command options.

---

## Level 2 -> 3

![Level 2 Output](images/bandit2_step.png)

### Goal
The password is stored in a file named `spaces in this filename` located in the home directory.

### Steps
1.  Check directory contents with `ls`. There is a file with spaces in its name.
2.  Read the file by quoting the name or escaping spaces.
    ```bash
    cat "spaces in this filename"
    ```
    Or:
    ```bash
    cat spaces\ in\ this\ filename
    ```
3.  Password obtained: `MNk8KNH3U8DUnzkUi6obeux76kpq4Wqa`
4.  Logout and login to Level 3.

### Command Explanation
*   `"..."`: Quotes arguments so the shell treats them as a single string.
*   `\`: Escape character to treat spaces as literal characters.

---

## Level 3 -> 4

![Level 3 Output](images/bandit3_step.png)

### Goal
The password is stored in a hidden file in the `inhere` directory.

### Steps
1.  Enter the `inhere` directory.
    ```bash
    cd inhere
    ```
2.  Use `ls -a` to see hidden files (starting with a dot).
    ```bash
    ls -a
    ```
3.  Read the `.hidden` file (or similar name).
    ```bash
    cat ...Hiding-From-You
    ```
4.  Password obtained: `2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ`

### Command Explanation
*   `cd`: Change directory.
*   `ls -a`: Lists all files including hidden ones.

---

## Level 4 -> 5

![Level 4 Output](images/bandit4_step.png)

### Goal
The password is stored in the `inhere` directory and has the following properties: human-readable, 1033 bytes in size, not executable.

### Steps
1.  Enter `inhere` directory.
    ```bash
    cd inhere
    ```
2.  Use `ls` to list files (`-file00` to `-file09`).
3.  Check file types one by one with `file ./*` or read the suspicious one (`-file07` is often the only ASCII text).
    ```bash
    file ./*
    cat ./-file07
    ```
4.  Password obtained: `4oQYVPkxZOOE005pTW81FB8j81xXGUQw`

### Command Explanation
*   `file`: Determines file type based on content (magic numbers).

---

## Level 5 -> 6

![Level 5 Output](images/bandit5_step.png)

### Goal
The password is stored in `inhere` directory with the following properties: human-readable, 1033 bytes in size, not executable.

### Steps
1.  Enter `inhere`.
2.  Use `find` to search for a file with size 1033 bytes.
    ```bash
    find . -size 1033c
    ```
3.  The result is `./maybehere07/.file2`. Read it.
    ```bash
    cat ./maybehere07/.file2
    ```
4.  Password obtained: `HWasnPhtq9AVKe0dmk45nxy20cvUa6EG`

### Command Explanation
*   `find`: Search for files in a directory hierarchy.
*   `-size 1033c`: Search for files with exactly 1033 bytes.

---

## Level 6 -> 7

![Level 6 Output](images/bandit6_step.png)

### Goal
The password is stored somewhere on the server and has all of the following properties: owned by user `bandit7`, owned by group `bandit6`, 33 bytes in size.

### Steps
1.  Use `find` from the root directory `/` with ownership and size criteria.
    ```bash
    find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
    ```
2.  `2>/dev/null` is used to suppress "Permission denied" messages.
3.  The found file is usually `/var/lib/dpkg/info/bandit7.password`.
4.  Read the file.
    ```bash
    cat /var/lib/dpkg/info/bandit7.password
    ```
5.  Password obtained: `morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj`

### Command Explanation
*   `-user`, `-group`: Filter search by ownership.
*   `2>/dev/null`: Redirects standard error to null device (discards error messages).

---

## Level 7 -> 8

![Level 7 Output](images/bandit7_step.png)

### Goal
The password is stored in `data.txt` next to the word "millionth".

### Steps
1.  Use `grep` to search for lines containing "millionth".
    ```bash
    grep "millionth" data.txt
    ```
2.  Password obtained: `dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc`

### Command Explanation
*   `grep`: Search for text patterns in files.

---

## Level 8 -> 9

![Level 8 Output](images/bandit8_step.png)

### Goal
The password is stored in `data.txt` and is the only line of text that occurs only once.

### Steps
1.  Use a combination of `sort` and `uniq -u`.
    ```bash
    sort data.txt | uniq -u
    ```
2.  `uniq` only works on sorted input, so `sort` is required first.
3.  Password obtained: `4CKMh1JI91bUIZZPXDqGanal4xvAg0JM`

### Command Explanation
*   `sort`: Sort lines of text files.
*   `uniq -u`: Report only unique lines.

---

## Level 9 -> 10

![Level 9 Output](images/bandit9_step.png)

### Goal
The password is stored in `data.txt` in one of the few human-readable strings, preceded by several `=` characters.

### Steps
1.  The file `data.txt` is binary. Use `strings` to extract readable text.
2.  Use `grep` to filter for the `=` sign.
    ```bash
    strings data.txt | grep "="
    ```
3.  Find the string that looks like a password (e.g., `========== the*password`).
4.  Password obtained: `FGUW5ilLVJrxX9kMYMm1N4MgbpfMiqey`

### Command Explanation
*   `strings`: Print printable characters strings in files.

---

## Level 10 -> 11

![Level 10 Output](images/bandit10_step.png)

### Goal
The password is stored in `data.txt`, which contains base64 encoded data.

### Steps
1.  Use `base64` with the decode option.
    ```bash
    base64 -d data.txt
    ```
2.  Password obtained: `dtR173fZKb0RRsDFSGsg2RWnpWPjqlND`

### Command Explanation
*   `base64 -d`: Decode data from Base64 format.

---
## Level 11 -> 12

![Level 11 Output](images/bandit11_step.png)

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

![Level 12 Output](images/bandit12_step.png)

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

![Level 13 Output](images/bandit13_step.png)

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

![Level 14 Output](images/bandit14_step.png)

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

![Level 15 Output](images/bandit15_step.png)

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

![Level 16 Output](images/bandit16_step.png)

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

![Level 17 Output](images/bandit17_step.png)

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

![Level 18 Output](images/bandit18_step.png)

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

![Level 19 Output](images/bandit19_step.png)

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

![Level 20 Output](images/bandit20_step.png)

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
## Level 21 -> 22

![Level 21 Output](images/bandit21_step.png)

### Goal
The password for the next level can be obtained by examining a running cron job.

### Steps
1.  Check the `/etc/cron.d/` directory.
    ```bash
    ls /etc/cron.d/
    ```
2.  Read the file `cronjob_bandit22`. It points to the script `/usr/bin/cronjob_bandit22.sh`.
    ```bash
    cat /usr/bin/cronjob_bandit22.sh
    ```
3.  The script copies the password to a temporary file in `/tmp`. Read that file.
    ```bash
    cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
    ```
4.  Password obtained: `tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q`

### Command Explanation
*   `cron`: Daemon to execute scheduled commands.
*   `/etc/cron.d`: Directory for cron job configuration files.

---

## Level 22 -> 23

![Level 22 Output](images/bandit22_step.png)

### Goal
The password is stored in a temporary file whose name is generated from the MD5 hash of the target username.

### Steps
1.  Check `cronjob_bandit23` and read its script `/usr/bin/cronjob_bandit23.sh`.
2.  The script uses the command:
    ```bash
    echo I am user $myname | md5sum | cut -d ' ' -f 1
    ```
3.  We need to know the filename for user `bandit23`.
    ```bash
    echo I am user bandit23 | md5sum | cut -d ' ' -f 1
    ```
4.  The hash result is `8ca319486bfbbc3663ea0fbe81326349`.
5.  Read the password file at `/tmp/HASH_RESULT`.
    ```bash
    cat /tmp/8ca319486bfbbc3663ea0fbe81326349
    ```
6.  Password obtained: `0Zf11ioIjMVN551jX3CmStKLYqjk54Ga`

### Command Explanation
*   `md5sum`: Computes MD5 hash.

---

## Level 23 -> 24

![Level 23 Output](images/bandit23_step.png)

### Goal
The password is stored in `/etc/bandit_pass/bandit24`. We need to create our own script that will be executed by the `bandit24` cron job.

### Steps
1.  Create a working directory in `/tmp` (e.g., `/tmp/exploityoga`).
2.  Create a script `copy.sh`:
    ```bash
    #!/bin/bash
    cat /etc/bandit_pass/bandit24 > /tmp/exploityoga/password
    ```
3.  Give execution permissions and ensure the destination directory is writable (chmod 777).
    ```bash
    chmod 777 copy.sh
    chmod 777 /tmp/exploityoga
    ```
4.  Copy the script to `/var/spool/bandit24/foo`.
    ```bash
    cp copy.sh /var/spool/bandit24/foo/
    ```
5.  Wait up to 1 minute for the cron job to run.
6.  Check the file `/tmp/exploityoga/password`.
    ```bash
    cat /tmp/exploityoga/password
    ```
7.  Password obtained: `gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8`

### Command Explanation
*   `/var/spool`: Directory for data awaiting processing (like cron jobs or mail).

---

## Level 24 -> 25

![Level 24 Output](images/bandit24_step.png)

### Goal
The password is stored by a daemon listening on port 30002. The daemon asks for the `bandit24` password and a secret 4-digit PIN.

### Steps
1.  We need to brute-force the PIN from 0000 to 9999.
2.  Use a one-line bash script to send all possibilities.
    ```bash
    for i in {0000..9999}; do echo "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 $i"; done | nc localhost 30002
    ```
3.  Filter the output to find the correct answer ("Correct!").
    ```bash
    ... | nc localhost 30002 | grep -v "Wrong"
    ```
4.  Password obtained: `iCi86ttT4KSNe1armKiwbQNmB3YJP3q4`

### Command Explanation
*   `for loop`: Loop to iterate through numbers.

---

## Level 25 -> 26

![Level 25 Output](images/bandit25_step.png)

### Goal
Login to `bandit25`. The shell is `/usr/bin/showtext`, which is restricted.

### Steps
1.  Login to `bandit25`.
2.  The `showtext` shell displays the content of `bandit26.sshkey` using `more`.
3.  Resize your terminal window so the text doesn't fit on one screen, forcing `more` to pause and show `--More--`.
4.  Press `v` to launch `vi`.
5.  Inside `vi`, run commands to spawn a shell:
    ```vim
    :set shell=/bin/bash
    :shell
    ```
6.  Now you have a shell! Read the key file.
    ```bash
    cat bandit26.sshkey
    ```
7.  Save this key to `bandit26.private` on your local machine and set permission `600`.

### Command Explanation
*   `vi`: Text editor that allows shell command execution.

---

## Level 26 -> 27

![Level 26 Output](images/bandit26_step.png)

### Goal
Login to `bandit26` and run the setuid binary `bandit27-do`. The shell is also restricted.

### Steps
1.  Use the private key to login to `bandit26`.
    ```bash
    ssh -i bandit26.private bandit26@bandit.labs.overthewire.org -p 2220
    ```
2.  Immediately after login, the shell runs `more`. Do the same trick (press `v`, then `:set shell=/bin/bash` in vi, then `:shell`).
3.  Run the `bandit27-do` binary to read the password.
    ```bash
    ./bandit27-do cat /etc/bandit_pass/bandit27
    ```
4.  Password obtained: `upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB`

### Command Explanation
*   `bandit27-do`: Special binary to escalate privileges to the next user.

---

## Level 27 -> 28

![Level 27 Output](images/bandit27_step.png)

### Goal
The password is obtained by cloning a git repository.

### Steps
1.  The repository is at `ssh://bandit27-git@localhost:2220/home/bandit27-git/repo`.
2.  User `bandit27-git` cannot login via SSH, but can clone via git.
3.  Clone the repo to a directory in `/tmp`.
    ```bash
    mkdir /tmp/gitrepo
    cd /tmp/gitrepo
    git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo
    ```
4.  Enter the password `upsNCc...` when prompted.
5.  Read the `README` file.
    ```bash
    cat repo/README
    ```
6.  Password obtained: `Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN`

### Command Explanation
*   `git clone`: Clones a git repository.

---

## Level 28 -> 29

![Level 28 Output](images/bandit28_step.png)

### Goal
The password is stored in the git log (commit history).

### Steps
1.  Clone repo `bandit28-git` (password same as previous level).
2.  Check git log showing patches.
    ```bash
    git log -p
    ```
3.  Look at the diff of the commit that removed the password.
4.  Password obtained: `4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7`

### Command Explanation
*   `git log -p`: Shows commit logs along with file changes (patches).

---

## Level 29 -> 30

![Level 29 Output](images/bandit29_step.png)

### Goal
The password is stored in a different git branch.

### Steps
1.  Clone repo `bandit29-git`.
2.  List all branches.
    ```bash
    git branch -a
    ```
3.  Switch to the development branch (`dev` or similar).
    ```bash
    git checkout dev
    ```
4.  Read `README.md`.
5.  Password obtained: `qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL`

### Command Explanation
*   `git branch`: Lists branches.
*   `git checkout`: Switches branches.

---

## Level 30 -> 31

![Level 30 Output](images/bandit30_step.png)

### Goal
The password is stored in a git tag.

### Steps
1.  Clone repo `bandit30-git`.
2.  List tags.
    ```bash
    git tag
    ```
3.  Show the content of tag `secret`.
    ```bash
    git show secret
    ```
4.  Password obtained: `fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy`

### Command Explanation
*   `git tag`: Lists tags.
*   `git show`: Shows details of a git object.

---

## Conclusion
Congratulations! You have solved the Bandit challenges up to Level 31. The next level might involve `git push`, but this guide ends here. Always remember to note down passwords and learn from every new command used.
