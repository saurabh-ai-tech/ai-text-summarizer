from summarizer import summarize

def main():
    print("=== AI Text Summarizer ===")

    text = input("\nEnter the text to summarize:\n")

    print("\nSelect summary length:")
    print("1. Short")
    print("2. Medium")
    print("3. Detailed")

    length_choice = input("Choice: ")

    lengths = {
        "1": "short",
        "2": "medium",
        "3": "detailed",
    }

    length = lengths.get(length_choice, "medium")

    print("\nSelect summary style:")
    print("1. Paragraph")
    print("2. Bullet points")
    print("3. Key takeaways")

    style_choice = input("Choice: ")

    styles = {
        "1": "paragraph",
        "2": "bullet points",
        "3": "key takeaways",
    }

    style = styles.get(style_choice, "paragraph")

    print("\nGenerating summary...\n")

    summary = summarize(
        text=text,
        length=length,
        style=style,
    )

    print("Summary:")
    print(summary)


if __name__ == "__main__":
    main()