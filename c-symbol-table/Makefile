CC			:= gcc
CFLAGS		:= -Wall -Werror -Wextra -pedantic
TEST_EXE	:= test-symbolreader
SRC_FILES	:= $(wildcard src/*.c)
OBJ_FILES	:= $(patsubst src/%.c, build/%.o, $(SRC_FILES))

.PHONY := all clean

all: build/test-symbolreader

build/test-symbolreader: $(OBJ_FILES)
	@$(CC) $(CFLAGS) -o $@ $^

build/%.o: src/%.c | build
	@$(CC) -c -o $@ -Iinclude $(CFLAGS) $<

build:
	@mkdir -p $@

clean:
	@rm -rf build
