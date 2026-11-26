import socket


def check_port(target_host, port):
    """Checks if a specific TCP port is open or closed on a given host."""
    # Create a TCP socket (AF_INET = IPv4, SOCK_STREAM = TCP)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Set a timeout so the script doesn't hang on filtered/unresponsive ports
        sock.settimeout(2.0)
        result = sock.connect_ex((target_host, port))
        return result == 0


def main():
    print("--- Port Status Checker ---")
    target = (
        input(
            "Enter target IP or hostname (press Enter for 127.0.0.1 / localhost): "
        ).strip()
        or "127.0.0.1"
    )

    try:
        port_input = input("Enter port number to check (1-65535): ").strip()
        port = int(port_input)

        if not (1 <= port <= 65535):
            print("Error: Port number must be between 1 and 65535.")
            return

        print(f"\nScanning {target} on port {port}...")
        if check_port(target, port):
            print(f"[+] Status: Port {port} is OPEN on {target}.")
        else:
            print(f"[-] Status: Port {port} is CLOSED on {target}.")

    except ValueError:
        print("Error: Invalid input. Please enter a numeric port number.")
    except socket.gaierror:
        print(f"Error: Could not resolve hostname '{target}'.")
    except socket.error as e:
        print(f"Socket error occurred: {e}")


if __name__ == "__main__":
    main()
