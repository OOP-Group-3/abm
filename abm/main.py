import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Get parameters for the ABM Simulation"
    )

    # Name and seed
    parser.add_argument("--name", help="experiment name", required=True)
    parser.add_argument("--seed", help="seed for reproducibility", type=int, default=42)

    return parser.parse_args()


if __name__ == "__main__":
    config = parse_args()
