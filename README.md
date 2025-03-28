# BookBot

**BookBot** is a Python-powered command-line tool for interactively analyzing books. It can extract word counts, character frequencies, top word lists, and more—all through a dynamic REPL interface.

Originally built as my first project on [Boot.dev](https://www.boot.dev), BookBot has evolved beyond its guided origin. It now features a modular, extensible design that supports dynamic pipelines, custom command sequences, and future NLP expansion.

This is no longer just a script—this is the foundation of a language-aware engine.

## Features

- Run commands in a REPL-style interface
- Count characters or words in any `.txt` book
- Clean and normalize text dynamically
- Omit stop words
- Sort and extract top-N words
- Stack commands to build analysis pipelines
- Modular architecture (CLI, parser, stats, pipeline)

## Getting Started

```bash
python main.py path_to_book
```
Then inside the RELP example flow:
>> lower_text
>> clean_text
>> count_words
>> sort
>> top 10
>> run

## Translation by Frequency (Coming Soon)

BookBot isn’t just a tool for analyzing books. It’s evolving into a new kind of translation engine—one that respects how people *actually learn*.

Traditional translation works line-by-line. BookBot will offer something different:

**Frequency-first translation.**

## How It Works

- Analyze a text and extract the **most common words**
- Automatically locate **sentences** where each word appears
- Translate those sentences first, starting with the **highest-frequency words**
- Work your way down the frequency ladder
- Re-read the book as it becomes more and more familiar

Instead of hitting a wall of unknown text, you’ll:

- Learn in **natural context**
- Translate **what matters most**
- Build **understanding through repetition**, not guesswork
- *Watch the book unlock itself*—sentence by sentence, layer by layer

This method supports:
- Language learners
- Translators
- Readers exploring texts slightly beyond their fluency

No major tool uses this method yet. It aligns with language acquisition theory, but gives you **total control**, **offline**.

---

## Why It’s Different

- 100% **offline** — no cloud, no surveillance, no data leaks
- Works with **any text** — books, documents, notes
- **Portable** — runs on your machine, not theirs
- **Extendable** — fully under your control

> Translate by frequency.  
> Learn with power.  
> Stay offline.  
> Control your text.

BookBot isn't just a project—it's the beginning of a new way to read.
