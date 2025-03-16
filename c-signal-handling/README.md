# POSIX signal handling in C

This live-code covers usage of the `signal` and `sigaction` system-call wrappers in C (GNU libc/Linux).

## `signal(2)`

(See source code in `./src/signal_syscall.c`)

Note: Usage of this system call is not portable and `sigaction` should be preferred.

To build this example, run:
```bash
$ make signal_syscall
```

Example usage:
```bash
$ build/signal_syscall 'Thanks for the Ctrl+C!'
```

The output will look something like this when you send `SIGINT` from your terminal.
```
^CUser message: Thanks for the Ctrl+C!
^CUser message: Thanks for the Ctrl+C!
^CUser message: Thanks for the Ctrl+C!
^Z
[1]+  Stopped                 build/01-signal_syscall 'Thanks for the Ctrl+C!'
```

(Just click `Ctrl+Z` to send `SIGKILL` and that will stop the process)

## `sigaction(2)`

Coming soon!
