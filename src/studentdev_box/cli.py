from studentdev_box.docker_manager import get_docker_client
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="devbox",
        description="Manage isolated development environments for students"
    )

    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser(
        "list",
        help="List available development environments"
    )

    start_parser = subparsers.add_parser(
        "start",
        help="Start a development environment"
    )

    start_parser.add_argument(
        "template",
        help="Environment to start"
    )

    args = parser.parse_args()

    if args.command == "list":
        print("Available environments:")
        print("1) cpp")
        print("2) python-data-science")
        print("3) postgresql")

    elif args.command == "start":
        client = get_docker_client()
        client.ping()

        print("Docker connection successful!")
        print(f"Starting environment: {args.template}")