/**
 * Paraphrased by DT from `signal(2)` of the Linux Programmer's Manual...
 *   Invocation of this system call is only portable when setting a signal 
 *   handler to the default handler or setting the "ignore" handler, 
 *   so its usage is discouraged in favor of `sigaction(2)`
 */

#include <errno.h>
#include <signal.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

/// @brief Function pointer type matching the signal callback prototype
typedef void (*sighandler_t)(int);

/// @brief Static pointer for storing user-defined SIGINT message
static const char *sigint_message = NULL; 

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
	/// Function-pointer variable to store previously set SIGINT handler
	sighandler_t old_handler = NULL;

	/// Enforcing usage
	if (argc != 2) {
		fprintf(stderr, "Usage: %s SIGINTMSG\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	/// Setting SIGINT message from command-line argument
	sigint_message = argv[1];

	/// Function prototype for `signal` syscall wrapper
	/// sighandler_t signal(int signum, sighandler_t handler);
	errno = 0;
	old_handler = signal(SIGINT, danielles_signal_handler);

	/// `signal` syscall wrapper returns `SIG_ERR` on error
	if (old_handler == SIG_ERR) {
		perror("signal");
		exit(EXIT_FAILURE);
	}

	/// Awaiting SIGINT to print the user-defined message
	while (1)
		;

	return 0;
}
