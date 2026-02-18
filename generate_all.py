import subprocess

SESSIONS = {
    0: "bandit0@bandit:~$ ls\nreadme\nbandit0@bandit:~$ cat readme\nZjLjTmM6********5If\nbandit0@bandit:~$ exit",
    1: "bandit1@bandit:~$ ls\n-\nbandit1@bandit:~$ cat ./- \n263JGJPfgU********mFx\nbandit1@bandit:~$ exit",
    2: "bandit2@bandit:~$ ls\nspaces in this filename\nbandit2@bandit:~$ cat \"spaces in this filename\"\nMNk8KNH3********4Wqa\nbandit2@bandit:~$ exit",
    3: "bandit3@bandit:~$ cd inhere\nbandit3@bandit:~/inhere$ ls -a\n. .. .hidden\nbandit3@bandit:~/inhere$ cat .hidden\n2WmrDFRm********F3NJ\nbandit3@bandit:~/inhere$ exit",
    4: "bandit4@bandit:~$ cd inhere\nbandit4@bandit:~/inhere$ file ./*\n./-file07: ASCII text\nbandit4@bandit:~/inhere$ cat ./-file07\n4oQYVPkx********GUQw\nbandit4@bandit:~/inhere$ exit",
    5: "bandit5@bandit:~$ cd inhere\nbandit5@bandit:~/inhere$ find . -size 1033c\n./maybehere07/.file2\nbandit5@bandit:~/inhere$ cat ./maybehere07/.file2\nHWasnPht********a6EG\nbandit5@bandit:~/inhere$ exit",
    6: "bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null\n/var/lib/dpkg/info/bandit7.password\nbandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password\nmorbNTDk********VAaj\nbandit6@bandit:~$ exit",
    7: "bandit7@bandit:~$ grep \"millionth\" data.txt\nmillionth\tdfwvzFQi********7eEc\nbandit7@bandit:~$ exit",
    8: "bandit8@bandit:~$ sort data.txt | uniq -u\n4CKMh1JI********0JM\nbandit8@bandit:~$ exit",
    9: "bandit9@bandit:~$ strings data.txt | grep \"=\"\n========== the*password\n========== password\n========== FGUW5ilL********Mqey\nbandit9@bandit:~$ exit",
    10: "bandit10@bandit:~$ base64 -d data.txt\ndtR173fZ********plND\nbandit10@bandit:~$ exit",
    11: "bandit11@bandit:~$ cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'\n7x16WNeH********j9Q4\nbandit11@bandit:~$ exit",
    12: "bandit12@bandit:~$ xxd -r data.txt > data.bin\nbandit12@bandit:~$ file data.bin\ndata.bin: gzip compressed data\nbandit12@bandit:~$ mv data.bin data.gz\nbandit12@bandit:~$ gunzip data.gz\n...\nbandit12@bandit:~$ cat password\nFO5dwFsc********TDwAn\nbandit12@bandit:~$ exit",
    13: "bandit13@bandit:~$ ssh -i sshkey.private bandit14@localhost\nbandit14@bandit:~$ cat /etc/bandit_pass/bandit14\nfGrHPx40********0ENq",
    14: "bandit14@bandit:~$ nc localhost 30000\nfGrHPx40********0ENq\nCorrect!\njN2kgmIX********6tnt",
    15: "bandit15@bandit:~$ openssl s_client -connect localhost:30001\nCONNECTED(00000003)\njN2kgmIX********6tnt\nJQttkNJt********5e6b",
    16: "bandit16@bandit:~$ nmap -p 31000-32000 localhost\nPORT      STATE SERVICE\n31790/tcp open  unknown\nbandit16@bandit:~$ openssl s_client -connect localhost:31790\nJQttkNJt********5e6b\nCorrect!\n-----BEGIN RSA PRIVATE KEY-----\n...",
    17: "bandit17@bandit:~$ diff passwords.old passwords.new\n< x2gLTTjF********GlO\n> ...",
    18: "bandit18@bandit:~$ ssh bandit18@bandit.labs.overthewire.org ... cat readme\ncGWpMaKX********3j8",
    19: "bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20\n0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO",
    20: "bandit20@bandit:~$ echo '0qXahG...YO' | nc -l -p 1234 &\n[1] 12345\nbandit20@bandit:~$ ./suconnect 1234\nRead: 0qXahG...YO\nPassword matches, sending next password\nEeoULMCr********uOBt",
    21: "bandit21@bandit:~$ cat /usr/bin/cronjob_bandit22.sh\ncp /etc/bandit_pass/bandit22 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv\nbandit21@bandit:~$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv\ntRae0UfB********F58Q",
    22: "bandit22@bandit:~$ echo I am user bandit23 | md5sum\n8ca319486bfbbc3663ea0fbe81326349  -\nbandit22@bandit:~$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349\n0Zf11ioI********4Ga",
    23: "bandit23@bandit:~$ cp copy.sh /var/spool/bandit24/foo/\nbandit23@bandit:~$ cat /tmp/exploityoga/password\ngb8KRRCs********bf3G8",
    24: "bandit24@bandit:~$ for i in {0000..9999}; do ... done | nc localhost 30002\nWrong! 0000\n...\nCorrect! \niCi86ttT********P3q4",
    25: "bandit25@bandit:~$ ssh -i bandit26.sshkey bandit26@localhost\nMORE\n:set shell=/bin/bash\n:shell\nbandit26@bandit:~$ cat bandit26.sshkey",
    26: "bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27\nupsNCc7v********owGB",
    27: "bandit27@bandit:~$ git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo\nbandit27@bandit:~$ cat repo/README\nYz9IpL0s********ZRcN",
    28: "bandit28@bandit:~$ git log -p\ncommit 123456...\n- 4pT1t5DE********jmJ7",
    29: "bandit29@bandit:~$ git branch -a\n* master\n  remotes/origin/dev\nbandit29@bandit:~$ git checkout dev\nbandit29@bandit:~$ cat README.md\nqp30ex3V********CDZL",
    30: "bandit30@bandit:~$ git tag\nsecret\nbandit30@bandit:~$ git show secret\nfb5S2xb7********hnDy",
    31: "bandit31@bandit:~$ git push\nRemote: You are now at Level 32!"
}

for level, text in SESSIONS.items():
    output_filename = f"bandit{level}_step.png"
    # Execute generation script
    process = subprocess.Popen(
        ['python3', 'screenshot_gen.py', output_filename],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=text)
    if process.returncode != 0:
        print(f"Error generating {output_filename}: {stderr}")
    else:
        print(f"Generated {output_filename}")
