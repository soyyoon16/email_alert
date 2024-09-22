from argparse import ArgumentParser
from mailer import send_email


def setup_args(parser):
    """
    Adds command-line arguments for the email alert system to the provided argument parser.

    Args:
        parser (argparse.ArgumentParser): The argument parser object to which the command-line arguments will be added.

    Returns:
        argparse.ArgumentParser: The updated argument parser with the added arguments for sender, recipient, subject, and body.
    """
    parser.add_argument("-s", "--sender", type=str, required=True)
    parser.add_argument("-r", "--recipient", type=str, required=True)
    parser.add_argument("-j", "--subject", type=str, default="Subject")
    parser.add_argument("-b", "--body", type=str, default="Body")
    return parser


def main():
    """
    Parse command-line arguments and send an email using the provided details.
    """
    parser = ArgumentParser()
    args = setup_args(parser).parse_args()

    send_email(
        sender=args.sender,
        recipient=args.recipient,
        subject=args.subject,
        body=args.body,
    )


if __name__ == "__main__":
    main()
