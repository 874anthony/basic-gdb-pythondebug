# Basic GDB Python Debug Script

This is a small Python script that integrates with GDB to automate folder creation during dynamic analysis of binaries — specifically designed for reverse engineering challenges like **Hack The Box - Graverobber**.

## 🔍 What It Does

The script sets a breakpoint at a specific address in the binary (`*main+0xb5`), reads the memory address containing a folder path during a `stat` call, and automatically creates the required directory on your filesystem.

## 🧠 Why

This was built to automate the folder-creation process needed to progress through certain RE challenges where directory structure affects program flow. It's also a good example of how to integrate Python scripting within GDB using its native API.

## 🛠️ Usage

1. Clone this repo or copy the script:

```bash
git clone https://github.com/874anthony/basic-gdb-pythondebug.git
cd basic-gdb-pythondebug
```

2. Launch GDB with your binary:

```bash
gdb -q robber
```

3. Inside GDB, source the script and run:

```bash
source directoryExtraction.py
run
```

The script will handle directory creation automatically as the program runs.

📁 Example

```bash
stat@plt (
   $rdi = 0x00007fffffffdb30 → 0x000000002f542f48 ("H/T/")
)
```

The script will extract H/T/ and ensure it exists on disk.

📎 Related Blog Post

📝 Read the full write-up here: [HTB Graverobber Challenge by 874anthony](https://www.874anthony.com/reversing-htb-challenge)