from services.post_generator import LinkedInPostGenerator

def main():
    generator = LinkedInPostGenerator(role="AI Engineer")
    topic = input("Enter LinkedIn post topic: ")
    post = generator.generate(topic)
    print("\nGenerated Post:\n")
    print(post)

if __name__ == "__main__":
    main()
