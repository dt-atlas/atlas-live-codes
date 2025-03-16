CC		:= gcc
CFLAGS	:= -Wall -Werror -Wextra -pedantic
CSTD	:= gnu99
SRCDIR	:= src
BINDIR	:= build

.PHONY	:= clean signal_syscall sigaction_syscall

signal_syscall : $(BINDIR)/signal_syscall

sigaction_syscall : $(BINDIR)/sigaction_syscall

$(BINDIR)/% : $(SRCDIR)/%.c | $(BINDIR)
	@$(CC) -o $@ $< $(CFLAGS) -std=$(CSTD)

$(BINDIR) :
	@mkdir -p $@

clean :
	@rm -rf $(BINDIR)
