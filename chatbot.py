    rows = load_faqs()

    if not rows:
        return None

    questions = [
        normalize(str(question))
        for question, answer in rows
        if question and answer
    ]

    valid_rows = [
        (question, answer)
        for question, answer in rows
        if question and answer
    ]

    if not questions:
        return None

    try:
        vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            sublinear_tf=True,
            strip_accents=None,
        )

        matrix = vectorizer.fit_transform(
            questions + [normalize(user_text)]
        )

        similarities = cosine_similarity(
            matrix[-1],
            matrix[:-1],
        ).flatten()

        best_index = int(similarities.argmax())
        best_score = float(similarities[best_index])

        if best_score >= 0.18:
            answer = str(valid_rows[best_index][1])

            # Avoid showing the abbreviation ECCS in answers
            answer = re.sub(
                r"\bECCS\b",
                "Excel College for Commerce and Science",
                answer,
                flags=re.IGNORECASE,
            )

            return answer

    except ValueError as error:
        print("FAQ matching error:", error)

    return None


# =========================================================
# MAIN RESPONSE FUNCTION
# =========================================================

def get_response(user_message):
    text = normalize(user_message)

    if not text:
        return "Please enter a question."

    # 1. Institution list (check before FAQ similarity so the bot
    #    returns the full list instead of a generic website-link answer).
    if is_institution_list_question(text):
        return institution_list_answer()

    # 2. Greetings
    answer = greeting_response(text)
    if answer:
        return answer

    # 3. 12th completed guidance
    answer = twelfth_guidance(text)
    if answer:
        return answer

    # 4. Direct responses
    answer = direct_answer(text)
    if answer:
        return answer

    # 5. FAQ database + TF-IDF
    answer = faq_answer(text)
    if answer:
        return answer

    # 6. Unknown question
    return (
        "🤖 I couldn't find a reliable answer for that question "
        "in my Excel Group database.\n\n"
        "Try asking about courses, BCA, admission, eligibility, "
        "hostel, placement, scholarship or institution details.\n\n"
        "You can also ask in Tamil or Tanglish."
    )


# =========================================================
# TEST LOCALLY
# =========================================================

if __name__ == "__main__":
    print("EXCEL GROUP AI CHATBOT")
    print("Type 'exit' to stop.")

    while True:
        question = input("\nYou: ").strip()

        if question.lower() in {"exit", "quit"}:
            break

        print("\nBot:", get_response(question))
