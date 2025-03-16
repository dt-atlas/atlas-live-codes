///
/// Same as `./signal_syscall.c` but refactored to use `sigaction(2)`
///

#include <errno.h>
#include <signal.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

/// @brief Function pointer type matching the signal callback prototype
typedef void (*sighandler_t)(int);

/// @brief Static pointer for storing user-defined SIGINT message
static const char *sigint_message = NULL;

/// @brief Static structure for configuring signal behavior
static struct sigaction new_sa;

/// @brief Static structure for retrieving current signal behavior
static struct sigaction old_sa;

/// @brief Prints the user error message when this process receives SIGINT
/// @param signal_number 
static void danielles_signal_handler(int signal_number)
{
	(void)signal_number;
	fprintf(stderr, "User message: %s\n", sigint_message);
}

/// @brief Program entry point
/// @param argc Command-line argument count
/// @param argv Pointer to command-line argument vector
/// @return Unlikely
int main(int argc, char **argv)
{
	/// Enforcing usage
	if (argc != 2) {
		fprintf(stderr, "Usage: %s SIGINTMSG\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	/// Setting SIGINT message from command-line argument
	sigint_message = argv[1];

	/// Set signal handler on the sigaction config
	new_sa.sa_handler = danielles_signal_handler;
	/// Call sigaction, returns -1 on error
	errno = 0;
	if (sigaction(SIGINT, &new_sa, &old_sa) == -1) {
		perror("sigaction");
		exit(EXIT_FAILURE);
	}

	/// Awaiting SIGINT to print the user-defined message
	while (1)
		;

	return 0;
}
