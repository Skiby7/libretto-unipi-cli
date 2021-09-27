
class COLORS:
	BOLD = "\033[1m"
	ITALIC = "\033[3m"
	RED = "\033[31m"
	GREEN = "\033[32m"
	BLUE = "\033[33m"
	YELLOW = "\033[34m"
	MAGENTA = "\033[35m"
	CYAN = "\033[36m"
	RED = "\033[31m"
	ALT_GREEN = "\033[92m"
	ALT_BLUE = "\033[93m"
	ALT_YELLOW = "\033[94m"
	ALT_MAGENTA = "\033[95m"
	ALT_CYAN = "\033[96m"
	CLEAR_SCREEN = "\033[2J\033[H"
	UP_ONE_LINE = "\033[1A"
	RESET = "\033[0m"

def print_color(msg, color):
	print(color + msg + COLORS.RESET)

	