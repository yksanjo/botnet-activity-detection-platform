from datetime import datetime, timezone


def main() -> None:
    print("botnet-activity-detection-platform initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
