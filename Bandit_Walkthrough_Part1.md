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
