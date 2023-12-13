filename = "./RESULT.txt"


def isValid(line: str) -> bool:
    line = line.strip()
    if not line:
        return False

    if line.strip() == 'rawbank':
        return False
    if line.strip == 'j\'aime':
        return False
    new_line = (
        line.replace("sem", "").replace("commentaires", "").replace("j", "").strip()
    )
    if new_line.isnumeric():
        return False
    restricted_keywords = [
        "facebook",
        "réactions",
        "learn more",
        "en voir plus",
        "m.me",
        "en ligne",
        "commenter",
        "plus de commentaires",
        " sem",
        "auteur",
        "répondre",
        "compte vérifié",
        "écrivez un commentaire",
        "   j’aime",
        "photos de la publication",
        "   ",
        "+",
        "partage",
        "partagé avec public",
        "#",
        "réactions",
        "grace",
        "http",
        "/",
        ":",
        "·",
        "…",
    ]
    for keyword in restricted_keywords:
        if keyword in line:
            return False
    return True


def process_file(filename: str):
    lines = []
    with open(filename, "r+", encoding="utf-8") as myFile:
        lines = myFile.readlines()
    valid_lines = [line for line in lines if isValid(line)]
    with open("VALID_RESULTS.txt", "w+", encoding="utf-8") as out:
        for line in valid_lines:
            out.writelines(line.strip() + "\n\n")


if __name__ == "__main__":
    process_file(filename=filename)
